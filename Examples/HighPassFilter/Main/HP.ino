//ButterWorth high Pass Filter
//Filter Name:HP
//Filter Order:4.0
//Filter cutoff frequency (-3dB):50.0Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte HP_a_bytes[16]={0xf7,0x65,0xbd,0xbf,0x52,0x4a,0xe,0x3f,0x33,0xb9,0xd9,0xbf,0x1e,0xdb,0x49,0x3f};
const float* HP_a = (float*) HP_a_bytes;

const byte HP_b_bytes[24]={0xdf,0x79,0x29,0x3f,0xdf,0x79,0xa9,0xbf,0xdf,0x79,0x29,0x3f,0x0,0x0,0x80,0x3f,0x0,0x0,0x0,0xc0,0x0,0x0,0x80,0x3f};
const float* HP_b = (float*) HP_b_bytes;

//Delay Variables
float HP_w[4]={0,0,0,0};



//*******************Update function
//This function must be called with a sampling frequency of 1000.0Hz
//Input: float x, Filter Input
//Return: float, Filter Output
float HP_Update(float x)
{
	float y;
	float w;
	//Biquad 0
	w = x-HP_w[0]*HP_a[0]-HP_w[1]*HP_a[1];
	y = w*HP_b[0]+HP_w[0]*HP_b[1]+HP_w[1]*HP_b[2];
	HP_w[1]=HP_w[0];
	HP_w[0]=w;
	//Biquad 1
	w = y-HP_w[2]*HP_a[2]-HP_w[3]*HP_a[3];
	y = w*HP_b[3]+HP_w[2]*HP_b[4]+HP_w[3]*HP_b[5];
	HP_w[3]=HP_w[2];
	HP_w[2]=w;
	return y;
}