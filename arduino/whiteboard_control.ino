#include <Servo.h>  //include servo library 

Servo myservo;  //create servo object

#define  SERVOPIN        10 // PIN D9 , PWM PIN
#define  RELAY1 	 2  // PIN D2
#define  RELAY2 	 4  // PIN D4
#define  EXECUTE_BUTTON  7  // PIN D1
#define  LIMIT_SWITCH1   5  // PIN D5
#define  LIMIT_SWITCH2   9  // PIN D9

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

void statemachine(){
	switch(state) {
		case IDLE:
			if(digitalRead(EXECUTE_BUTTON) == LOW){
				Serial.print(F("state: IDLE->MOVE_FWD\n"));
				state = MOVE_FWD;
				erasersDown();
				delay(1000);
				ccw();	
			}
			break;

		case MOVE_FWD:
			if(digitalRead(LIMIT_SWITCH1) == LOW){
				Serial.print(F("state: MOVE_FWD->IDLE2\n"));
				state = IDLE2;
				stop();
			}
			else 
				state = MOVE_FWD;
			break;

		case IDLE2:
			if(digitalRead(EXECUTE_BUTTON) == LOW){
				Serial.print(F("state: IDLE->MOVE_BCK\n"));
				state = MOVE_BCK;
				cw();
			}
			else 
				state = IDLE2;
			break;

		case MOVE_BCK:
			if(digitalRead(LIMIT_SWITCH2) == LOW){
				delay(1000);
				erasersUp();
				delay(1000);
				Serial.print(F("state: MOVE_BCK->IDLE\n"));
				state = IDLE;
				stop();
			}
			else 
				state = MOVE_BCK;
			break;

		case default:
			state = IDLE;
			break;

	};
};

void setup() {
	Serial.begin(115200);
	Serial.print(F("\nbooted\n"));

	pinMode(RELAY1, OUTPUT);// set pin as output for relay 1
	pinMode(RELAY2, OUTPUT);// set pin as output for relay 2
	pinMode(LIMIT_SWITCH1, INPUT); // set pin as input for limit switch 1
	pinMode(LIMIT_SWITCH2, INPUT); // set pin as input for limit switch 2

	myservo.attach(SERVOPIN); //assign myservo object to a servoPin pin

	// keep the motor off by keeping both HIGH
	digitalWrite(RELAY1, HIGH); 
	digitalWrite(RELAY2, HIGH); 

}

void loop() {

	statemachine();
	delay(10);
	// Intially rotate in CCW direction
	//	ccw();

	//	if (digitalRead(LIMIT_SWITCH1) == LOW)
	//	{
	//		// stop the motor
	//		stop();
	//		delay(100);
	//		// Switch to CW direction
	//		cw();
	//
	//		endBoard = true;
	//	}
	//
	//	if (digitalRead(LIMIT_SWITCH2) == LOW && endBoard)
	//	{
	//		// stop the motor
	//		stop();
	//	}

}

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

void erasersDown(){
	Serial.print(F("erasers down\n"));
	myservo.write(0);
	delay(15);
}

void erasersUp(){
	Serial.print(F("erasers up\n"));
	myservo.write(180); //play with this number
	delay(15);
}

