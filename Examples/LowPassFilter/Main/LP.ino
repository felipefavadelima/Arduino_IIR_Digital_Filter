//ButterWorth Low Pass Filter
//Filter Name:LP
//Filter Order:4.0
//Filter cutoff frequency (-3dB):150.0Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte LP_a_bytes[16]={
	0xc0,0x38,0x2c,0xbf,
	0x9,0x1,0x14,0x3e,
	0xe9,0xcc,0x65,0xbf,
	0xb9,0xf5,0x6,0x3f};
const float* LP_a = (float*) LP_a_bytes;

const byte LP_b_bytes[24]={0x74,0x11,0x98,0x3c,
	0x74,0x11,0x18,0x3d,
	0x75,0x11,0x98,0x3c,
	0x0,0x0,0x80,0x3f,
	0x0,0x0,0x0,0x40,
	0x0,0x0,0x80,0x3f};
const float* LP_b = (float*) LP_b_bytes;

//Delay Variables
float LP_w[4]={0,0,0,0};



//*******************Update function
//This function must be called every 0.001s (1000.0Hz)
//Input: float x, Filter Input
//Return: float, Filter Output
float LP_Update(float x)
{
	float y;
	float w;
	//Section 0
	w = x-LP_w[0]*LP_a[0]-LP_w[1]*LP_a[1];
	y = w*LP_b[0]+LP_w[0]*LP_b[1]+LP_w[1]*LP_b[2];
	LP_w[1]=LP_w[0];
	LP_w[0]=w;
	//Section 1
	w = y-LP_w[2]*LP_a[2]-LP_w[3]*LP_a[3];
	y = w*LP_b[3]+LP_w[2]*LP_b[4]+LP_w[3]*LP_b[5];
	LP_w[3]=LP_w[2];
	LP_w[2]=w;
	return y;
}