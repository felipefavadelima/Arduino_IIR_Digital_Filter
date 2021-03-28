# Example of 70 Hz Detector

When a signal with a frequency of 70Hz is injected into the arduino input A0, the arduino LED (pin 13) lights up. 

To create "Ress70Hz.ino":

Step 1:Create Coeffs.npy (See Example 'GenCoeffs.py')

Step 2: run

    python FilterFromCoeffs.py Ress70Hz Coeffs.npy 1000

To create "LP.ino" run:

python LPButter.py LP 2 0.5 1000




