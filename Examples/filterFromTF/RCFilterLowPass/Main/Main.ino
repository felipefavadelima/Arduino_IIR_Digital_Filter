#include "TimerOne.h"

//Author:Felipe Fava de Lima
//03/2021


//150 Hz ressonator
//Input: Analog A0
//Input and Output shown on serial plott

//Samplign Frequency 
const float Fs = 1000;
const float tus = (1 / Fs) * 1e6;

//Filter Input/Output Variable
float x=0;
float y = 0;

//Update Flag
bool UpdateFlag = false;

//Filter Update function
void IIRUpdate()
{
  y = RCLP_10Hz_Update(x);
  //Print float is too slow 
  Serial.print(int(x));
  Serial.print(',');
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
  analogReference(INTERNAL);
  Timer1.initialize(tus);
  Timer1.attachInterrupt(TimerInt);
  Serial.begin(1000000);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (UpdateFlag == true) IIRUpdate();
}
