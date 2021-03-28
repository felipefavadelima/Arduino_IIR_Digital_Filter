###############################################
#author Felipe Fava de Lima
#date 03/2021
###############################################

from scipy import signal
import numpy as np
import cmath
import math
import matplotlib.pyplot as plt

#Desing Ressonator from zeros/poles location

#Specs
Fs_Hz = 1000;
Fress_Hz = 70;
Wress = Fress_Hz/(Fs_Hz/2);

#Poles desing
PoleRadius = 0.999
Poles = [cmath.exp(1j*math.pi*Wress)*PoleRadius , cmath.exp(-1j*math.pi*Wress )*PoleRadius]

#Zeros desing
ZeroRadius = 0.8
Zeros = [cmath.exp(1j*math.pi*Wress)*ZeroRadius , cmath.exp(-1j*math.pi*Wress )*ZeroRadius]

#Get TF
b = np.poly(Zeros)*0.6e-2
a = np.poly(Poles)

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

np.save('Coeffs.npy',np.array([b,a]));

