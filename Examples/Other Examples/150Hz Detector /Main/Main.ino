#include "TimerOne.h"

//Author:Felipe Fava de Lima
//03/2021

//150Hz detector example
//Signal Processing steps
//Step 1 - 150Hz ressonator
//Step 2 - Low pass Filter (Fc = 0.5Hz)
//Step 3 - rectify signal
//Step 4 - Threshold detector

//Input: Analog A0
//Input and Output shown on serial plotter

//Samplign Frequency 
const float Fs = 1000;
const float tus = (1 / Fs) * 1e6;

//Detector Threshold 
const float Threshold = 20;

//Filter Input/Output Variable
float x=0;
float y = 0;

//Update Flag
bool UpdateFlag = false;

//Filter Update function
void IIRUpdate()
{
  //Step 1
  y = Ress150Hz_Update(x);
  //Step2
  y = abs(y);
  //Step 3
  y = LP_Update(y);
  //Step 4
  if(y>Threshold) digitalWrite(13,HIGH);
  else digitalWrite(13,LOW);
  Serial.println(int(x));
  Serial.println(',');
  Serial.println(int(y));
  UpdateFlag = false;
}

//Timer Int
void TimerInt()
{
  x = float(analogRead(A0));
  UpdateFlag = true;
}


void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  analogReference(INTERNAL);
  Timer1.initialize(tus);
  Timer1.attachInterrupt(TimerInt);
  Serial.begin(1000000);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (UpdateFlag == true) IIRUpdate();
}
