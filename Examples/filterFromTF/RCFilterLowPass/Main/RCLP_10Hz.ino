//10Hz low pass RC
//Filter Name:RCLP_10Hz
//Filter samplig frequency:1000.0Hz

//*******************Global Variables

//Filter Coefficients
const byte RCLP_10Hz_a_bytes[8]={
	0x1f,0x7c,0x70,0xbf,
	0x0,0x0,0x0,0x0};
const float* RCLP_10Hz_a = (float*) RCLP_10Hz_a_bytes;

const byte RCLP_10Hz_b_bytes[12]={0x10,0x3e,0xf8,0x3c,
	0x10,0x3e,0xf8,0x3c,
	0x0,0x0,0x0,0x0};
const float* RCLP_10Hz_b = (float*) RCLP_10Hz_b_bytes;

//Delay Variables
float RCLP_10Hz_w[2]={0,0};



//*******************Update function
//This function must be called every 0.001s (1000.0Hz)
//Input: float x, Filter Input
//Return: float, Filter Output
float RCLP_10Hz_Update(float x)
{
	float y;
	float w;
	//Section 0
	w = x-RCLP_10Hz_w[0]*RCLP_10Hz_a[0]-RCLP_10Hz_w[1]*RCLP_10Hz_a[1];
	y = w*RCLP_10Hz_b[0]+RCLP_10Hz_w[0]*RCLP_10Hz_b[1]+RCLP_10Hz_w[1]*RCLP_10Hz_b[2];
	RCLP_10Hz_w[1]=RCLP_10Hz_w[0];
	RCLP_10Hz_w[0]=w;
	return y;
}