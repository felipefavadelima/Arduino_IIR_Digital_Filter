//ButterWorth Low Pass Filter
//Filter Name:LP
//Filter Order:2.0
//Filter cutoff frequency (-3dB):0.5Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte LP_a_bytes[8]={0x6a,0x6e,0xff,0xbf,0x7a,0xdd,0x7e,0x3f};
const float* LP_a = (float*) LP_a_bytes;

const byte LP_b_bytes[12]={0xa3,0x37,0x25,0x36,0xa3,0x37,0xa5,0x36,0xa3,0x37,0x25,0x36};
const float* LP_b = (float*) LP_b_bytes;

//Delay Variables
float LP_w[2]={0,0};



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
	return y;
}