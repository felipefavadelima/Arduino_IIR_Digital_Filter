# Arduino IIR Digital Filter code generator

Automatic Arduino Code Generator for IIR Filters. 

Tutorial video (portuguese): https://youtu.be/HoFn65hA1ho

## **Main programs:**

- **butter.py** - program that automatically generates Arduino code for Butterworth filter  (Low-pass, High-Pass, Band-pass or Stop-Band).
 
- **filterFromTF.py** - program that automatically generates Arduino filter code from a filter transfer function.
 
## Python Prerequisites:

[Python >= 3.0](https://www.python.org/)
 
[python scipy package](https://www.scipy.org/install.html)
 
[python numpy package](https://numpy.org/install/)
 
[python matplotlib package](https://matplotlib.org/stable/users/installing.html)
 
## Arduino Prerequisites:

[Arduino IDE](https://www.arduino.cc/en/software)

[TimerOne library](https://www.arduino.cc/reference/en/libraries/timerone/)

**The example codes were tested on Arduino NANO.**

## Examples Folder:

Within the examples folder there is a short instruction file 'ReadMe.txt' on how to generate the '.ino' files for each type of filter. 

The generated '.ino' file has a function of type 'xxx_Update (float x)' which is responsible for updating the filter output. In the examples, the 'Main.ino' files give an example of how to use it. 

In the 'Main.INO' examples, the analog input signal of the filter is obtained from the A0 port of the arduino. Both the filter output and the input can be displayed by the serial plotter. 

## Filter Testing:

The electronic circuit shown in 'PCAudioCircuit / Schematic.jpg' can be used to connect the sound card output of a computer to the Arduino in order to test the projected filters. It is worth remembering that in an Arduino Nano, for an eighth-order filter, the maximum sampling frequency that can be used is 1000Hz. Thus, the signals that can be injected into the filter input must have components up to 500Hz, according to the Nyquist-Shannon sampling theorem.

An [online](https://www.szynalski.com/tone-generator/) tone generator can be used for testing. 

**After designing the desired filter always check the execution time of the function 'xxx_Update ()' in order to verify that the configured sampling frequency is being obtained correctly**

## Basic Usage

 **Butterworth filters desing:**

- (low-pass): "python butter.py low Name n Fc_Hz Fs_Hz"

- (high-pass): "python butter.py high Name n Fp_Hz Fs_Hz"

- (band-pass): "python butter.py pass Name n Fp1_Hz Fp2_Hz Fs_Hz"

- (stop-band): "python butter.py stop Name n Fc1_Hz Fs2_Hz Fs_Hz"

	**Name** - Filter Name (will determine the name of the final .ino file)

	**N**- Filter Order

	**Fc_Hz** - Cutoff Frequency (-3dB)

	**Fp_Hz** - Pass Frequency (-3dB)

	**Fp1_Hz Fp2_Hz** - Band-pass frequencies (-3dB)

	**Fc1_Hz Fc2_Hz** - Cutoff frequencies (-3dB)

## Butterworth filters desing Examples:

Low Pass fourth order, 150Hz cutoff frequency, 1000Hz samplig frequency:

**python butter.py low LP 4 150 1000**

High Pass fourth order, 150Hz cutoff frequency, 1000Hz samplig frequency: 

 **python butter.py high HP 4 150 1000**

Band-pass fourth order, 150Hz to 200Hz band-pass frequency, 1000Hz samplig frequency: 

**python butter.py pass BP 4 150 200 1000**

Stop-band fourth order, 150Hz to 200Hz stop-band frequency, 1000Hz samplig frequency:

**python butter.py stop SB 4 150 200 1000**


## Filter from tranfer function:

- It is possible to obtain code for Arduino from the transfer function of the desired filter using a program "filterFromTF.py".

**See examples:**

"Examples/filterFromTF/RCFilterLowPass"

"Examples/filterFromTF/PolesZerosRessonator"

## Filter implementation:

Filters are implemented as second-order cascade systems ([BIQUADS](https://en.wikipedia.org/wiki/Digital_biquad_filter)) using direct form II.


