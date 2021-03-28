#include "TimerOne.h"

//Author:Felipe Fava de Lima
//03/2021

//70Hz detector example
//Ressonator 70Hz + Envelope detector 

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
  y = Ress70Hz_Update(x);
  y = abs(y);
  y = LP_Update(y);
  Serial.println(int(y));
  if(y>Threshold) digitalWrite(13,HIGH);
  else digitalWrite(13,LOW);
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
