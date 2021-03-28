# Arduino IIR Digital Filter code generator

Generates Arduino code to implement IIR digital filter 

### This repository contains the following files:

"scr\LPButter.py" - python Low pass ButterWoth Arduino code generator
 
"scr\HPButter.py" - python High pass ButterWoth Arduino code generator
 
"scr\BPButter.py" - python Band pass ButterWoth Arduino code generator
 
"scr\BSButter.py" - python Stop Band ButterWoth Arduino code generator
 
"scr\FilterFromCoeffs.py" - python Filter code generator for Arduino by the coefficients (b, a) of the filter transfer function  
 
### Python Prerequisites:

Python >= 3.0
 
python scipy package (https://www.scipy.org/install.html)
 
python numpy package (https://numpy.org/install/)
 
python matplotlib package(https://matplotlib.org/stable/users/installing.html)
 
### Arduino Prerequisites:

TimerOne library (https://www.arduino.cc/reference/en/libraries/timerone/)

The sample codes were tested on Arduino nano.

### Examples:

Within the examples folder there is a short instruction on how to generate the '.ino' file for each type of filter. 

The generated '.ino' file has a function of type 'xxx_Update (float x)' which is responsible for updating the filter output. In the examples, the 'Main.ino' files give an example of how to use it. 

In the examples, the analog input signal of the filter is obtained from the A0 port of the arduino. Both the filter output and the input can be displayed by the serial plotter. 

### Filter Testing:

The electronic circuit shown in 'PCAudioCircuit / Schematic.jpg' can be used to connect the sound output of a computer to the Arduino in order to test the projected filters. It is worth remembering that in an Arduino Nano, for an eighth-order filter, the maximum sampling frequency that can be used is 1000Hz. Thus, the signals that can be injected into the filter input must have components up to 500Hz, according to the Nyquist-Shannon sampling theorem.

An online tone generator can be used for testing, such as: 
[links](https://www.szynalski.com/tone-generator/)

### Basic Usage
Briefly, the '.ino' files with the 'xxx_Update ()' function are generated as follows: 

#### python BSButter.py BS 4 50 100 1000

This command produces a 'BS.ino' file that has the function 'BS_Update ()'. This function is used to implement a Butterworth fourth-order bandpass filter with cutoff frequencies from 50Hz to 100Hz, and the filter data update rate will be 1000Hz (Sampling frequency). 



