// Arduino Uno SPI pins
// Pin 11 = SDI
// Pin 13 = CLK

// Arduino Pro Micro SPI pins
// Pin 16 = Serial data out
// Pin 15 = CLK

// IR stuff
#include "IRremote.h"
int RECV_PIN = A9;  // IR Receiver pin
const int IRGroundPin = A8;
const int IRPowerPin = 7;
IRrecv irrecv(RECV_PIN);
decode_results results;
int lastIRoperation;
int IRsignal;

//////////////////////////////////////////////////////////////////////////////////////////////
// Setup
//////////////////////////////////////////////////////////////////////////////////////////////

void setup() {
  Serial.begin (9600);
  // IR
  irrecv.enableIRIn(); // Start the receiver
  pinMode(IRPowerPin, OUTPUT);
  pinMode(IRGroundPin, OUTPUT);
  digitalWrite(IRPowerPin, HIGH); // Power for the IR
  digitalWrite(IRGroundPin, LOW); // GND for the IR
}

//////////////////////////////////////////////////////////////////////////////////////////////
// Main loop
//////////////////////////////////////////////////////////////////////////////////////////////
void loop() {
  // Decode the IR if recieved
  if (irrecv.decode(&results)) {
    if (results.value == 4294967295) {
      IRsignal = lastIRoperation;
    } else {
      IRsignal = lastIRoperation = results.value;
    }
    switch (IRsignal) {
      case 2011287694: case 2011287569:
        Serial.println("UP");
        break;
      case 2011279502: case 2011279377:
        Serial.println("DOWN");
        break;
      case 2011291790: case 2011291665:
        Serial.println("RIGHT");
        break;
      case 2011238542: case 2011238417:
        Serial.println("LEFT");
        break;
      case 2011265678: case 2011250705:
        Serial.println("PLAY/PAUSE");
        break;
      default:
        Serial.print("Unknown IR code: ");
        Serial.println(IRsignal);
      break;
    }
    irrecv.resume();
  }

}
