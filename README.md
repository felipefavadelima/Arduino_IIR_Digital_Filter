# Arduino IIR Digital Filter code generator

Automatic Arduino Code Generator for IIR Filters 

### This repository contains the following main programs:

"scr\butter.py" - program that automatically generates Arduino code for Butterworth filter  (Low-pass, High-Pass, Band-pass, Stop-Band)
 
"scr\filterFromTF.py" - program that automatically generates Arduino filter code from a transfer function 
 
### Python Prerequisites:

[Python >= 3.0](https://www.python.org/)
 
[python scipy package](https://www.scipy.org/install.html)
 
[python numpy package](https://numpy.org/install/)
 
[python matplotlib package](https://matplotlib.org/stable/users/installing.html)
 
### Arduino Prerequisites:

[Arduino IDE](https://www.arduino.cc/en/software)

[TimerOne library](https://www.arduino.cc/reference/en/libraries/timerone/)

#### The exemple codes were tested on Arduino NANO.

### Examples:

Within the examples folder there is a short instruction file 'ReadMe.txt' on how to generate the '.ino' files for each type of filter. 

The generated '.ino' file has a function of type 'xxx_Update (float x)' which is responsible for updating the filter output. In the examples, the 'Main.ino' files give an example of how to use it. 

In the 'Main.INO' examples, the analog input signal of the filter is obtained from the A0 port of the arduino. Both the filter output and the input can be displayed by the serial plotter. 

### Filter Testing:

The electronic circuit shown in 'PCAudioCircuit / Schematic.jpg' can be used to connect the sound card output of a computer to the Arduino in order to test the projected filters. It is worth remembering that in an Arduino Nano, for an eighth-order filter, the maximum sampling frequency that can be used is 1000Hz. Thus, the signals that can be injected into the filter input must have components up to 500Hz, according to the Nyquist-Shannon sampling theorem.

An [online](https://www.szynalski.com/tone-generator/) tone generator can be used for testing. 

#### After designing the desired filter always check the execution time of the function 'xxx_Update ()' in order to verify that the configured sampling frequency is being obtained correctly 

### Basic Usage

##Butterworth filters:

Low Pass fourth order, 150Hz cutoff frequency, 1000Hz samplig frequency: 
#### "python butter.py low LP 4 150 1000"

High Pass fourth order, 150Hz cutoff frequency, 1000Hz samplig frequency: 
#### "python butter.py high HP 4 150 1000"

Band-pass fourth order, 150Hz to 200Hz band-pass frequency, 1000Hz samplig frequency: 
#### "python butter.py pass BP 4 150 200 1000"

Stop-band fourth order, 150Hz to 200Hz stop-band frequency, 1000Hz samplig frequency
#### "python butter.py stop SB 4 150 200 1000"


##Filter from tranfer function:

It is possible to obtain code for Arduino from the transfer function of the desired filter using a program "filterFromTF.py". See examples "Examples/filterFromTF/RCFilterLowPass" and "Examples/filterFromTF/PolesZerosRessonator"



