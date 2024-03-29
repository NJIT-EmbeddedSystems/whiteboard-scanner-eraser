//2016.12.08
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
	Serial.begin(9600);
	Serial.print(F("\nbooted\n"));
	myservo.attach(13);  // attaches the servo on pin 9 to the servo object
}

void loop() {
	for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
		// in steps of 1 degree
		myservo.write(pos);              // tell servo to go to position in variable 'pos'
		delay(500);                       // waits 15ms for the servo to reach the position
		Serial.print(F("\nangle:"pos'\n'));
	}
	myservo.write(0);
}
