//Filter Name:Ress70Hz
//Sampling Frequency:1000.0 Hz

//*******************Global Variables

//Filter Coefficients
const byte Ress70Hz_a_bytes[8]={0x72,0x67,0xe7,0xbf,0xfe,0x7c,0x7f,0x3f};
const float* Ress70Hz_a = (float*) Ress70Hz_a_bytes;

const byte Ress70Hz_b_bytes[12]={0xa6,0x9b,0xc4,0x3b,0x26,0x51,0xe,0xbc,0x82,0xa8,0x7b,0x3b};
const float* Ress70Hz_b = (float*) Ress70Hz_b_bytes;

//Delay Variables
float Ress70Hz_w[2]={0,0};



//*******************Update function
//This function must be called with a sampling frequency of 1000.0Hz
//Input: float x, Filter Input
//Return: float, Filter Output
float Ress70Hz_Update(float x)
{
	float y;
	float w;
	//Biquad 0
	w = x-Ress70Hz_w[0]*Ress70Hz_a[0]-Ress70Hz_w[1]*Ress70Hz_a[1];
	y = w*Ress70Hz_b[0]+Ress70Hz_w[0]*Ress70Hz_b[1]+Ress70Hz_w[1]*Ress70Hz_b[2];
	Ress70Hz_w[1]=Ress70Hz_w[0];
	Ress70Hz_w[0]=w;
	return y;
}