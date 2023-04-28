#define  RELAY1 	 2  // PIN D2
#define  RELAY2 	 4  // PIN D4
#define  LIMIT_SWITCH1   5  // PIN D5
#define  LIMIT_SWITCH2   19 // PIN D19
bool endBoard = false; // set endBoard to false intially 

enum States {
	IDLE,
	MOVE_FWD,
	IDLE2,
	MOVE_BCK
};
enum Input {
	EXECUTE,
	LIMIT1,
	LIMIT2,
};

uint8_t state = IDLE;
/*
void controller(uint8_t Input){
	switch(state) {
		case IDLE:
		if () {
		}
		break;

		case MOVE_FWD:
		if () {
		}
		break;

		case IDLE2:
		if () {
		}
		break;

		case MOVE_BCK:
		if () {
		}
		break;

		case default:
		if () {
		}
		break;

};
*/

void setup() {
	Serial.begin(115200);
	Serial.print(F("\nbooted\n"));

	pinMode(RELAY1, OUTPUT);// set pin as output for relay 1
	pinMode(RELAY2, OUTPUT);// set pin as output for relay 2
	pinMode(LIMIT_SWITCH1, INPUT); // set pin as input for limit switch 1
	pinMode(LIMIT_SWITCH2, INPUT); // set pin as input for limit switch 2

	// keep the motor off by keeping both HIGH
	digitalWrite(RELAY1, HIGH); 
	digitalWrite(RELAY2, HIGH); 
}

void loop() {

	// Intially rotate in CCW direction
	ccw();

	if (digitalRead(LIMIT_SWITCH1) == LOW)
	{
		// stop the motor
		stop();
		delay(100);
		// Switch to CW direction
		cw();

		endBoard = true;
	}

	if (digitalRead(LIMIT_SWITCH2) == LOW && endBoard)
	{
		// stop the motor
		stop();
	}

}// loop end

void ccw() {
	Serial.print(F("move counter-clockwise\n"));
	digitalWrite(RELAY1, LOW);// turn relay 1 ON
	digitalWrite(RELAY2, HIGH);// turn relay 2 OFF  
}

void cw() {
	Serial.print(F("move clockwise\n"));
	digitalWrite(RELAY1, HIGH);// turn relay 1 OFF
	digitalWrite(RELAY2, LOW);// turn relay 2 ON  
}

void stop() {
	Serial.print(F("stopping\n"));
	digitalWrite(RELAY1, HIGH);// turn relay 1 OFF
	digitalWrite(RELAY2, HIGH);// turn relay 2 OFF    
}
