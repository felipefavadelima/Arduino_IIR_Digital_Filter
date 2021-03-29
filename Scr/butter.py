###############################################
#author Felipe Fava de Lima
#date 03/2021
###############################################

import sys
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

def PrintArgumentsError():
    print('Arguments Error!\n',
              '(low-pass): "python butter.py low Name n Fc_Hz Fs_Hz"\n',
              '(high-pass): "python butter.py high Name n Fp_Hz Fs_Hz"\n',
              '(band-pass): "python butter.py pass Name n Fp1_Hz Fp2_Hz Fs_Hz"\n',
              '(stop-band): "python butter.py stop Name n Fc1_Hz Fs2_Hz Fs_Hz"\n',
              'Name - Filter Name (will determine the name of the final .ino file)\n',
              'N - Filter Order\n',
              'Fc_Hz - Cutoff Frequency (-3dB)\n',
              'Fp_Hz - Pass Frequency (-3dB)\n',
              'Fp1_Hz Fp2_Hz - Band-pass frequencies (-3dB)\n',
              'Fc1_Hz Fc2_Hz - Cutoff frequencies (-3dB)\n',
              'Example (low-pass): "python butter.py low LP 4 150 1000"\n',
              'Example (high-pass): "python butter.py high HP 4 150 1000"\n',
              'Example (band-pass): "python butter.py pass BP 4 150 200 1000"\n',
              'Example(stop-band): "python butter.py stop SB 4 150 200 1000"')

#****************************************** CODE GENERATOR ********************************************************
def genArduinoIno(sos32,InoHeader,Fs_Hz):
    print('\nGenerating .INO file....')
    CodeString  =INOHeader
    CodeString += '//*******************Global Variables\n\n'
    CodeString += '//Filter Coefficients\n'
    #Biquads
        #a coefs
    a= np.zeros(sos32.shape[0] *2)
    a = a.astype(np.float32)
    for Sec in range(0,sos32.shape[0]):
      a[Sec*2] = sos32[Sec,4]
      a[Sec*2+1] = sos32[Sec,5]
    a_coeff = 'const byte '+ FName +'_a_bytes[' + str(a.size*4) + ']={\n\t'
    BytesCount = 0
    for Byte in a.tobytes():
        a_coeff += hex(Byte) + ','
        BytesCount+= 1
        if(BytesCount >=4):
            a_coeff += '\n\t'
            BytesCount = 0
    a_coeff = a_coeff[0:-3]    
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
    BytesCount = 0
    for Byte in b.tobytes():
        b_coeff += hex(Byte) + ','
        BytesCount+= 1
        if(BytesCount >=4):
            b_coeff += '\n\t'
            BytesCount = 0
    b_coeff = b_coeff[0:-3]    
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
    CodeString += '//This function must be called every '+ str(1/Fs_Hz) +'s ('+ str(Fs_Hz)+'Hz)\n'
    CodeString += '//Input: float x, Filter Input\n'
    CodeString += '//Return: float, Filter Output\n'
    CodeString += 'float ' + FName + '_Update(float x)\n'
    CodeString += '{\n'
    CodeString += '\tfloat y;\n'
    CodeString += '\tfloat w;\n'

    for Sec in range(0,sos32.shape[0]): 
        CodeString += '\t//Section '+ str(Sec)+'\n'
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


#****************************************** MAIN ********************************************************   
if __name__ == "__main__":
    Arguments = sys.argv
    if(len(Arguments) > 5):
        FType = Arguments[1]
        FName = Arguments[2]
        FN = float(Arguments[3])
        ArgError = False;
        if(FType == 'low'):
            if(len(Arguments) == 6):
                Fc_Hz = float(Arguments[4])
                Fs_Hz = float(Arguments[5])
                print('\nLow Pass Butterwoth Arguments:');
                print('Filter Name:', FName);
                print('Filter Order:', FN);
                print('Fc_Hz:', Fc_Hz , 'Hz');
                print('Fs_Hz:', Fs_Hz , 'Hz');
                #INO Header
                INOHeader = '//ButterWorth Low Pass Filter\n'
                INOHeader += '//Author:Felipe Fava de Lima\n'
                INOHeader += '//Filter Name:' + FName + '\n'
                INOHeader += '//Filter Order:' + str(FN) + '\n'
                INOHeader += '//Filter cutoff frequency (-3dB):' + str(Fc_Hz) + 'Hz\n'
                INOHeader += '//Filter samplig frequency:' + str(Fs_Hz) + 'Hz\n\n'
                #Low pass Filter desing
                Wn = Fc_Hz/(Fs_Hz/2)
                b, a = signal.butter(FN, Wn,'lowpass')
            else:
                ArgError = True;   
        elif(FType == 'high'):
            if(len(Arguments) == 6):
                Fp_Hz = float(Arguments[4])
                Fs_Hz = float(Arguments[5])
                print('\nHigh Pass Butterwoth Arguments:');
                print('Filter Name:', FName);
                print('Filter Order:', FN);
                print('Fp_Hz:', Fp_Hz , 'Hz');
                print('Fs_Hz:', Fs_Hz , 'Hz');
                #INO Header
                INOHeader = '//ButterWorth High Pass Pass Filter\n'
                INOHeader += '//Author:Felipe Fava de Lima\n'
                INOHeader += '//Filter Name:' + FName + '\n'
                INOHeader += '//Filter Order:' + str(FN) + '\n'
                INOHeader += '//Filter pass frequency (-3dB):' + str(Fp_Hz) + 'Hz\n'
                INOHeader += '//Filter samplig frequency:' + str(Fs_Hz) + 'Hz\n\n'
                #High pass Filter desing
                Wn = Fp_Hz/(Fs_Hz/2)
                b, a = signal.butter(FN, Wn,'highpass')
            else:
                ArgError = True;
        elif(FType == 'pass'):
            if(len(Arguments) == 7):
                Fp1_Hz = float(Arguments[4])
                Fp2_Hz = float(Arguments[5])
                Fs_Hz = float(Arguments[6])
                print('\nBand pass Butterwoth Arguments:');
                print('Filter Name:', FName);
                print('Filter Order:', FN);
                print('Fp1_Hz:', Fp1_Hz , 'Hz');
                print('Fp2_Hz:', Fp2_Hz , 'Hz');
                print('Fs_Hz:', Fs_Hz , 'Hz');
                #INO Header
                INOHeader = '//ButterWorth Band Pass Pass Filter\n'
                INOHeader += '//Author:Felipe Fava de Lima\n'
                INOHeader += '//Filter Name:' + FName + '\n'
                INOHeader += '//Filter Order:' + str(FN) + '\n'
                INOHeader += '//Filter pass frequency 1 (-3dB):' + str(Fp1_Hz) + 'Hz\n'
                INOHeader += '//Filter pass frequency 2 (-3dB):' + str(Fp2_Hz) + 'Hz\n'
                INOHeader += '//Filter samplig frequency:' + str(Fs_Hz) + 'Hz\n\n'
                #Band pass Filter desing
                Wn = np.array([Fp1_Hz, Fp2_Hz])
                Wn = Wn/(Fs_Hz/2)
                b, a = signal.butter(FN, Wn,'bandpass')
            else:
                ArgError = True;
        elif(FType == 'stop'):
            if(len(Arguments) == 7):
                Fc1_Hz = float(Arguments[4])
                Fc2_Hz = float(Arguments[5])
                Fs_Hz = float(Arguments[6])
                print('\nStop Band Butterwoth Arguments:');
                print('Filter Name:', FName);
                print('Filter Order:', FN);
                print('Fc1_Hz:', Fc1_Hz , 'Hz');
                print('Fc2_Hz:', Fc2_Hz , 'Hz');
                print('Fs_Hz:', Fs_Hz , 'Hz');
                #INO Header
                INOHeader = '//ButterWorth Stop Band Filter\n'
                INOHeader += '//Author:Felipe Fava de Lima\n'
                INOHeader += '//Filter Name:' + FName + '\n'
                INOHeader += '//Filter Order:' + str(FN) + '\n'
                INOHeader += '//Filter cutoff frequency 1 (-3dB):' + str(Fc1_Hz) + 'Hz\n'
                INOHeader += '//Filter cutoff frequency 2 (-3dB):' + str(Fc2_Hz) + 'Hz\n'
                INOHeader += '//Filter samplig frequency:' + str(Fs_Hz) + 'Hz\n\n'
                #Band stop Filter desing
                Wn = np.array([Fc1_Hz, Fc2_Hz])
                Wn = Wn/(Fs_Hz/2)
                b, a = signal.butter(FN, Wn,'stop')
            else:
                ArgError = True;
        if(ArgError == True):
             PrintArgumentsError()
        else:
                #print tranfer function
            print('\nFilter Tranfer Function:')
            print('Numerator:' + str(b));
            print('Denominator:' + str(a));
                #Convert filter to second-order sections
            sos = signal.tf2sos(b,a);
                #Print 32bits second-order tranfer functions
            sos32 = sos.astype(np.float32)
            print('\nSecond Order Sections 32bits Tranfer Functions:')
            for Sec in range(0,sos32.shape[0]):
                print('*Section '+str(Sec))
                TFstr = 'H(z)=\t'
                for k in range(0,3):
                    if(k==0):
                        TFstr += str(sos32[Sec,k])
                    else:
                        TFstr += ' + ' + str(sos32[Sec,k]) + '(z^-' + str(k) + ')'
                TFstr += '\n\t---------------------------------------------'
                TFstr += '\n\t'
                for k in range(3,6):
                    if(k==0):
                        TFstr += str(sos32[Sec,k])
                    else:
                        TFstr += ' + ' + str(sos32[Sec,k]) + '(z^-' + str(k-3) + ')'
                print( TFstr)       
                #Show Frequency response
            wd,hd = signal.freqz(b,a,1000,fs=Fs_Hz);
                #Convert coeffs to 32bits
            sos32 = sos.astype(np.float32);
            sos32 = sos32.astype(np.float64);
            b32,a32 = signal.sos2tf(sos32);
                #plot freq response
            ws,hs = signal.freqz(b32,a32,1000,fs=Fs_Hz);
            print('\nFilter frequency repsonse plot...');
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
            genArduinoIno(sos.astype(np.float32),INOHeader ,Fs_Hz)
    else:
        PrintArgumentsError()
    
    
    

    

        
 
