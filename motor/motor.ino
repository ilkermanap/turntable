#include <Stepper.h>

#define STEPS 100

Stepper stepper(STEPS, 8, 9, 10, 11);

bool turn;

void setup() {
  // put your setup code here, to run once:
  turn = false;
  stepper.setSpeed(60);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    if (Serial.available() > 0) {
    // read the incoming byte:
    String incoming = Serial.readString();
    incoming.trim();
    if (incoming == "turn")  {
      turn=true;    
    }
    if (incoming == "stop")  {
      turn=false;    
    }

      
  }
    
    if (turn) {
       Serial.println("clockwise");
	     stepper.step(20);
	     delay(500);
    
    }	
}
