###############################################
#author Felipe Fava de Lima
#date 03/2021
###############################################

import sys
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import struct


def genArduinoIno(sos32,FName, Fs_Hz):
    print('Generating .INO file....')
    #header
    CodeString = '//Filter Name:' + FName + '\n'
    CodeString += '//Sampling Frequency:' + str(Fs_Hz) + ' Hz\n\n'

    CodeString += '//*******************Global Variables\n\n'
    CodeString += '//Filter Coefficients\n'
    #Biquads
        #a coefs
    a= np.zeros(sos32.shape[0] *2)
    a = a.astype(np.float32)
    for Sec in range(0,sos32.shape[0]):
      a[Sec*2] = sos32[Sec,4]
      a[Sec*2+1] = sos32[Sec,5]
    a_coeff = 'const byte '+ FName +'_a_bytes[' + str(a.size*4) + ']={'
    for Byte in a.tobytes():
        a_coeff += hex(Byte) + ','
    a_coeff = a_coeff[0:-1]    
    a_coeff += '};\n'
    CodeString += a_coeff
    CodeString += 'const float* ' + FName + '_a = (float*) ' + FName+ '_a_bytes;\n\n'
       #b coefs
    b= np.zeros(sos32.shape[0] *3)
    b = b.astype(np.float32)
    for Sec in range(0,sos32.shape[0]):
      b[Sec*3] = sos32[Sec,0]
      b[Sec*3+1] = sos32[Sec,1]
      b[Sec*3+2] = sos32[Sec,2]
    b_coeff = 'const byte '+ FName +'_b_bytes[' + str(b.size*4) + ']={'
    for Byte in b.tobytes():
        b_coeff += hex(Byte) + ','
    b_coeff = b_coeff[0:-1]    
    b_coeff += '};\n'
    CodeString += b_coeff
    CodeString += 'const float* ' + FName + '_b = (float*) ' + FName+ '_b_bytes;\n\n' 
    #Delay Variable
    CodeString += '//Delay Variables\n'
    CodeString += 'float '+ FName +'_w[' + str(2*sos32.shape[0]) +']={'
    for n in range(0,2*sos32.shape[0]):
        CodeString += '0,'
    CodeString = CodeString[0:-1]
    CodeString += '};\n\n\n\n'
    #Update Function
    CodeString += '//*******************Update function\n'
    CodeString += '//This function must be called with a sampling frequency of '+ str(Fs_Hz) +'Hz\n'
    CodeString += '//Input: float x, Filter Input\n'
    CodeString += '//Return: float, Filter Output\n'
    CodeString += 'float ' + FName + '_Update(float x)\n'
    CodeString += '{\n'
    CodeString += '\tfloat y;\n'
    CodeString += '\tfloat w;\n'

    for Sec in range(0,sos32.shape[0]): 
        CodeString += '\t//Biquad '+ str(Sec)+'\n'
        #Eq 1 Direct Form II
        if(Sec == 0):
            CodeString += '\tw = x'
            CodeString += '-' + FName + '_w[' + str(Sec*2) + ']*' +FName+ '_a[' + str(Sec*2) +']'
            CodeString += '-' + FName + '_w[' + str(Sec*2+1) + ']*' +FName+ '_a[' + str(Sec*2+1) +'];\n'
        else:
            CodeString += '\tw = y'
            CodeString += '-' + FName + '_w[' + str(Sec*2) + ']*' +FName+ '_a[' + str(Sec*2) +']'
            CodeString += '-' + FName + '_w[' + str(Sec*2+1) + ']*' +FName+ '_a[' + str(Sec*2+1) +'];\n'
        #Eq 1 Direct Form II
        CodeString += '\ty = w*'  +FName+ '_b[' + str(Sec*3) +']'
        CodeString += '+' + FName + '_w[' + str(Sec*2) + ']*' +FName+ '_b[' + str(Sec*3+1) +']'
        CodeString += '+' + FName + '_w[' + str(Sec*2+1) + ']*' +FName+ '_b[' + str(Sec*3+2) +'];\n'
        CodeString += '\t'+ FName + '_w[' + str(Sec*2+1) + ']='+ FName + '_w[' + str(Sec*2) + '];\n'
        CodeString += '\t'+ FName + '_w[' + str(Sec*2) + ']=w;\n';
    CodeString += '\treturn y;\n'
    CodeString += '}'

    INO_file = open(FName+'.ino', "w")
    INO_file.write(CodeString)
    INO_file.close()


    
if __name__ == "__main__":
    Arguments = sys.argv;
    if(len(Arguments) == 4):
        FName = Arguments[1];
        FileName = Arguments[2];
        Fs_Hz = float(Arguments[3]);
        ab = np.load(FileName)
        a = ab[1,:]
        b = ab[0,:]
        #Convert filter to second-order sections
        sos = signal.tf2sos(b,a);
        
        #Show Frequency response
        wd,hd = signal.freqz(b,a,1000,fs=Fs_Hz);
            #Convert coeffs to 32bits
        sos32 = sos.astype(np.float32);
        sos32 = sos32.astype(np.float64);
        b32,a32 = signal.sos2tf(sos32);
        ws,hs = signal.freqz(b32,a32,1000,fs=Fs_Hz);
            #plot freq response
        print('Filter frequency repsonse plot...');
        plt.subplot(2,1,1)
        plt.plot(wd, 20 * np.log10(abs(hd)), 'b')
        plt.plot(ws, 20 * np.log10(abs(hs)), 'r')
        plt.grid()
        plt.xlabel('Frequency(Hz)')
        plt.ylabel('Amplitude(dB)')
        plt.legend(['64bits','32bits'])
        plt.subplot(2,1,2)
        plt.plot(wd, 20 * np.angle(hd), 'b')
        plt.plot(ws, 20 * np.angle(hs), 'r')
        plt.grid()
        plt.xlabel('Frequency(Hz)')
        plt.ylabel('Phase(degrees)')
        plt.legend(['64bits','32bits'])
        plt.show()

        #generate arduino INO
        header = ''
        genArduinoIno(sos.astype(np.float32),FName, Fs_Hz)

        
    else:
        print('Arguments Error!\n',
              'Example: "python FilterFromCoeffs.py Name PyFile Fs_Hz"\n',
              'Name - Filter Name\n',
              'PyFile - numpy file with a and b filter coeffs\n',
              'Fs_Hz - sampling Frequency\n',
              'Example: "python FilterFromCoeffs.py F1 Coeffs.npy 1000"');
