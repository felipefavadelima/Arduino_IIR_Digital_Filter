//ButterWorth Stop Band Filter
//Filter Name:SB
//Filter Order:4.0
//Filter cutoff frequency 1 (-3dB):150.0Hz
//Filter cutoff frequency 2 (-3dB):200.0Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte SB_a_bytes[32]={
	0x83,0x8c,0x33,0xbf,
	0xbf,0xf,0x3d,0x3f,
	0xc7,0xe7,0x65,0xbf,
	0x4e,0xab,0x40,0x3f,
	0x26,0x5f,0x1a,0xbf,
	0x9d,0x4d,0x61,0x3f,
	0x99,0x8f,0x8c,0xbf,
	0xb0,0x5b,0x65,0x3f};
const float* SB_a = (float*) SB_a_bytes;

const byte SB_b_bytes[48]={0xdf,0x79,0x29,0x3f,
	0x45,0xc8,0x1b,0xbf,
	0x94,0x82,0x29,0x3f,
	0x0,0x0,0x80,0x3f,
	0x61,0x69,0x6b,0xbf,
	0x15,0x7,0x80,0x3f,
	0x0,0x0,0x80,0x3f,
	0xff,0x44,0x6b,0xbf,
	0xd9,0xf1,0x7f,0x3f,
	0x0,0x0,0x80,0x3f,
	0xb5,0x5d,0x6b,0xbf,
	0xd7,0xf2,0x7f,0x3f};
const float* SB_b = (float*) SB_b_bytes;

//Delay Variables
float SB_w[8]={0,0,0,0,0,0,0,0};



//*******************Update function
//This function must be called every 0.001s (1000.0Hz)
//Input: float x, Filter Input
//Return: float, Filter Output
float SB_Update(float x)
{
	float y;
	float w;
	//Section 0
	w = x-SB_w[0]*SB_a[0]-SB_w[1]*SB_a[1];
	y = w*SB_b[0]+SB_w[0]*SB_b[1]+SB_w[1]*SB_b[2];
	SB_w[1]=SB_w[0];
	SB_w[0]=w;
	//Section 1
	w = y-SB_w[2]*SB_a[2]-SB_w[3]*SB_a[3];
	y = w*SB_b[3]+SB_w[2]*SB_b[4]+SB_w[3]*SB_b[5];
	SB_w[3]=SB_w[2];
	SB_w[2]=w;
	//Section 2
	w = y-SB_w[4]*SB_a[4]-SB_w[5]*SB_a[5];
	y = w*SB_b[6]+SB_w[4]*SB_b[7]+SB_w[5]*SB_b[8];
	SB_w[5]=SB_w[4];
	SB_w[4]=w;
	//Section 3
	w = y-SB_w[6]*SB_a[6]-SB_w[7]*SB_a[7];
	y = w*SB_b[9]+SB_w[6]*SB_b[10]+SB_w[7]*SB_b[11];
	SB_w[7]=SB_w[6];
	SB_w[6]=w;
	return y;
}