###############################################
#author Felipe Fava de Lima
#date 03/2021
###############################################

from scipy import signal
import numpy as np
import cmath
import math
import matplotlib.pyplot as plt

#Desing from Bilinear transform

#Digital Filter specs
Fs_Hz = 1000

#Analog  RC low pass filter specs(Fc = 10Hz)
R = 1.6e3
C = 10e-6

# s transfer function
num = 1
den =[R*C, 1]

# s to z - Bilinear transform
[b,a] = signal.bilinear(num,den,Fs_Hz)

#Show Frequency response
w,h = signal.freqz(b,a,1000,fs=Fs_Hz);
#plot freq response
print('Filter frequency repsonse plot...');
plt.subplot(2,1,1)
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.grid()
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude(dB)')
plt.subplot(2,1,2)
plt.plot(w, 20 * np.angle(h), 'b')
plt.grid()
plt.xlabel('Frequency(Hz)')
plt.ylabel('Phase(degrees)')
plt.legend(['64bits','32bits'])
plt.show()

#Save TF
np.save('TF.npy',np.array([b,a]));

