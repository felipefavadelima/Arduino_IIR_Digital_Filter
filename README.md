# Arduino IIR Digital Filter code generator

# This repository contains the following files:


 -"scr\LPButter.py" - Low pass ButterWoth Arduino code generator
 
 -"scr\HPButter.py" - High pass ButterWoth Arduino code generator
 
 -"scr\BPButter.py" - Band pass ButterWoth Arduino code generator
 
 -"scr\BSButter.py" - Stop Band ButterWoth Arduino code generator
 
 -"scr\FilterFromCoeffs.py" - Filter code generator for Arduino by the coefficients (b, a) of the filter transfer function  
 
 
 
 
 
 
# Python Prerequisites:

- Python >= 3.0
 
 - python scipy package (https://www.scipy.org/install.html)
 
 - python numpy package (https://numpy.org/install/)
 
 - python matplotlib package(https://matplotlib.org/stable/users/installing.html)
 
 
 
 
 
Arduino Prerequisites:

 TimerOne library (https://www.arduino.cc/reference/en/libraries/timerone/)

The sample codes were tested on Arduino nano.

Within the examples folder there is a short instruction on how to generate the '.ino' file for each type of filter. 

The generated '.ino' file has a function of type 'xxx_Update (float x)' which is responsible for updating the filter output. In the examples, the 'Main.ino' files give an example of how to use it. 

Briefly, the '.ino' files with the 'xxx_Update ()' function are generated as follows: 
