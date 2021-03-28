//ButterWorth Low Pass Filter
//Filter Name:LP
//Filter Order:4.0
//Filter cutoff frequency (-3dB):50.0Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte LP_a_bytes[16]={0xf7,0x65,0xbd,0xbf,0x52,0x4a,0xe,0x3f,0x33,0xb9,0xd9,0xbf,0x1e,0xdb,0x49,0x3f};
const float* LP_a = (float*) LP_a_bytes;

const byte LP_b_bytes[24]={0x0,0x6b,0xda,0x39,0xff,0x6a,0x5a,0x3a,0x0,0x6b,0xda,0x39,0x0,0x0,0x80,0x3f,0x0,0x0,0x0,0x40,0x0,0x0,0x80,0x3f};
const float* LP_b = (float*) LP_b_bytes;

//Delay Variables
float LP_w[4]={0,0,0,0};



//*******************Update function
//This function must be called with a sampling frequency of 1000.0Hz
//Input: float x, Filter Input
//Return: float, Filter Output
float LP_Update(float x)
{
	float y;
	float w;
	//Biquad 0
	w = x-LP_w[0]*LP_a[0]-LP_w[1]*LP_a[1];
	y = w*LP_b[0]+LP_w[0]*LP_b[1]+LP_w[1]*LP_b[2];
	LP_w[1]=LP_w[0];
	LP_w[0]=w;
	//Biquad 1
	w = y-LP_w[2]*LP_a[2]-LP_w[3]*LP_a[3];
	y = w*LP_b[3]+LP_w[2]*LP_b[4]+LP_w[3]*LP_b[5];
	LP_w[3]=LP_w[2];
	LP_w[2]=w;
	return y;
}