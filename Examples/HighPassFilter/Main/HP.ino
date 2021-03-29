//ButterWorth High Pass Pass Filter
//Filter Name:HP
//Filter Order:4.0
//Filter pass frequency (-3dB):150.0Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte HP_a_bytes[16]={
	0xc0,0x38,0x2c,0xbf,
	0x9,0x1,0x14,0x3e,
	0xe9,0xcc,0x65,0xbf,
	0xb9,0xf5,0x6,0x3f};
const float* HP_a = (float*) HP_a_bytes;

const byte HP_b_bytes[24]={0xf8,0x2,0x8d,0x3e,
	0xf9,0x2,0xd,0xbf,
	0xf8,0x2,0x8d,0x3e,
	0x0,0x0,0x80,0x3f,
	0x0,0x0,0x0,0xc0,
	0x0,0x0,0x80,0x3f};
const float* HP_b = (float*) HP_b_bytes;

//Delay Variables
float HP_w[4]={0,0,0,0};



//*******************Update function
//This function must be called every 0.001s (1000.0Hz)
//Input: float x, Filter Input
//Return: float, Filter Output
float HP_Update(float x)
{
	float y;
	float w;
	//Section 0
	w = x-HP_w[0]*HP_a[0]-HP_w[1]*HP_a[1];
	y = w*HP_b[0]+HP_w[0]*HP_b[1]+HP_w[1]*HP_b[2];
	HP_w[1]=HP_w[0];
	HP_w[0]=w;
	//Section 1
	w = y-HP_w[2]*HP_a[2]-HP_w[3]*HP_a[3];
	y = w*HP_b[3]+HP_w[2]*HP_b[4]+HP_w[3]*HP_b[5];
	HP_w[3]=HP_w[2];
	HP_w[2]=w;
	return y;
}