# Example of 150 Hz Detector

When a signal with a frequency of 150Hz is injected into the arduino NANO input A0, the arduino LED (pin 13) lights up. 

Signal Processing steps:
Step 1 - the signal is filtered through a resonator set to the frequency of 150Hz
Step 2 - the signal is rectified
Step 3 - the signal passes through a 0.5Hz low-pass filter
Step 4 - The output signal is tested, if it is higher than a certain threshold, the led on pin 13 lights up. 

To create "Ress150Hz.ino" check "Examples/filterFromTF/PolesZerosRessonator":

To create "LP.ino" check "Examples/LowPassFilter" (Running "python butter.py low LP 2 0.5 1000")







