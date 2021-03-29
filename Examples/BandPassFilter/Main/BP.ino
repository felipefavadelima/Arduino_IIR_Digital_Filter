//ButterWorth Band Pass Pass Filter
//Filter Name:BP
//Filter Order:4.0
//Filter pass frequency 1 (-3dB):150.0Hz
//Filter pass frequency 2 (-3dB):200.0Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte BP_a_bytes[32]={
	0x83,0x8c,0x33,0xbf,
	0xbf,0xf,0x3d,0x3f,
	0xc7,0xe7,0x65,0xbf,
	0x4e,0xab,0x40,0x3f,
	0x26,0x5f,0x1a,0xbf,
	0x9d,0x4d,0x61,0x3f,
	0x99,0x8f,0x8c,0xbf,
	0xb0,0x5b,0x65,0x3f};
const float* BP_a = (float*) BP_a_bytes;

const byte BP_b_bytes[48]={0x0,0x6b,0xda,0x39,
	0x0,0x6b,0x5a,0x3a,
	0x0,0x6b,0xda,0x39,
	0x0,0x0,0x80,0x3f,
	0x0,0x0,0x0,0x40,
	0x0,0x0,0x80,0x3f,
	0x0,0x0,0x80,0x3f,
	0x0,0x0,0x0,0xc0,
	0x0,0x0,0x80,0x3f,
	0x0,0x0,0x80,0x3f,
	0x0,0x0,0x0,0xc0,
	0x0,0x0,0x80,0x3f};
const float* BP_b = (float*) BP_b_bytes;

//Delay Variables
float BP_w[8]={0,0,0,0,0,0,0,0};



//*******************Update function
//This function must be called every 0.001s (1000.0Hz)
//Input: float x, Filter Input
//Return: float, Filter Output
float BP_Update(float x)
{
	float y;
	float w;
	//Section 0
	w = x-BP_w[0]*BP_a[0]-BP_w[1]*BP_a[1];
	y = w*BP_b[0]+BP_w[0]*BP_b[1]+BP_w[1]*BP_b[2];
	BP_w[1]=BP_w[0];
	BP_w[0]=w;
	//Section 1
	w = y-BP_w[2]*BP_a[2]-BP_w[3]*BP_a[3];
	y = w*BP_b[3]+BP_w[2]*BP_b[4]+BP_w[3]*BP_b[5];
	BP_w[3]=BP_w[2];
	BP_w[2]=w;
	//Section 2
	w = y-BP_w[4]*BP_a[4]-BP_w[5]*BP_a[5];
	y = w*BP_b[6]+BP_w[4]*BP_b[7]+BP_w[5]*BP_b[8];
	BP_w[5]=BP_w[4];
	BP_w[4]=w;
	//Section 3
	w = y-BP_w[6]*BP_a[6]-BP_w[7]*BP_a[7];
	y = w*BP_b[9]+BP_w[6]*BP_b[10]+BP_w[7]*BP_b[11];
	BP_w[7]=BP_w[6];
	BP_w[6]=w;
	return y;
}