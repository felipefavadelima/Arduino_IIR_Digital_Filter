//Second order 150Hz Ressonator
//Filter Name:Ress150Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte Ress150Hz_a_bytes[8]={
	0x93,0x52,0x96,0xbf,
	0xfe,0x7c,0x7f,0x3f};
const float* Ress150Hz_a = (float*) Ress150Hz_a_bytes;

const byte Ress150Hz_b_bytes[12]={0xa6,0x9b,0xc4,0x3b,
	0xb8,0xe6,0xb8,0xbb,
	0x82,0xa8,0x7b,0x3b};
const float* Ress150Hz_b = (float*) Ress150Hz_b_bytes;

//Delay Variables
float Ress150Hz_w[2]={0,0};



//*******************Update function
//This function must be called every 0.001s (1000.0Hz)
//Input: float x, Filter Input
//Return: float, Filter Output
float Ress150Hz_Update(float x)
{
	float y;
	float w;
	//Section 0
	w = x-Ress150Hz_w[0]*Ress150Hz_a[0]-Ress150Hz_w[1]*Ress150Hz_a[1];
	y = w*Ress150Hz_b[0]+Ress150Hz_w[0]*Ress150Hz_b[1]+Ress150Hz_w[1]*Ress150Hz_b[2];
	Ress150Hz_w[1]=Ress150Hz_w[0];
	Ress150Hz_w[0]=w;
	return y;
}