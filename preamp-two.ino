#include "SPI.h"

bool debugEnabled = false;

// Arduino Uno SPI pins
// Pin 11 = SDI
// Pin 13 = CLK

// Arduino Pro Micro SPI pins
// Pin 16 = Serial data out
// Pin 15 = CLK

// Input selector stuff
int selectedInput = 0;
const int inputSelectorCSPin = A1;
long muteDelay = 1000;
bool muteEnabled = true;
int inputSelectorEncoderCounter = 0;
int inputSelectorEncoderSensitivity = 4;

// MDAC attenuator stuff
const int mdacCSPin = A0;
float currentDbLevel;
float max_dbLevel = -0.0001;
float min_dbLevel = -96.5;
float currentChangeVolumeIncrement;
unsigned int currentDacR2Rvalue;

// IR stuff
#include "IRremote.h"
int RECV_PIN = A9;  // IR Receiver pin
const int IRGroundPin = A8;
const int IRPowerPin = 7;
IRrecv irrecv(RECV_PIN);
decode_results results;
int lastIRoperation;
int IRsignal;
float iRIncrement = 2;
unsigned long timeOfLastIRChange;

// Encoder stuff
int encoder0PinA = 2;
int encoder0PinB = 3;
int encoder0Pos = 0;
int encoder0PinALast = HIGH;
int encoder0n = LOW;
int encoder1PinA = 4;
int encoder1PinB = 5;
int encoder1Pos = 0;
int encoder1PinALast = HIGH;
int encoder1n = LOW;
float volumeEncoderIncrement = 0.5;

//////////////////////////////////////////////////////////////////////////////////////////////
// Setup
//////////////////////////////////////////////////////////////////////////////////////////////

void setup() {
  // Serial
  if (debugEnabled) {
    Serial.begin (9600);
  }
  // set the inputSelectorCSPin as an output:
  pinMode(inputSelectorCSPin, OUTPUT);
  digitalWrite(inputSelectorCSPin,HIGH);
  pinMode(mdacCSPin, OUTPUT);
  digitalWrite(mdacCSPin,HIGH);
  // Start SPI
  if (debugEnabled) {
    Serial.println ("Starting SPI...");
  }
  SPI.begin();
  // Set SPI selector IO direction to output for all pinds
  if (debugEnabled) {
    Serial.println ("Setting input selector IO direction control registers..");
  }
  // Set IO direction to output for all bank 0 (I/O pins 0-7)
  digitalWrite(inputSelectorCSPin,LOW);
  SPI.transfer(B01000000); // Send Device Opcode
  SPI.transfer(0);         // Select IODIR register for bank 0
  SPI.transfer(0);         // Set register
  digitalWrite(inputSelectorCSPin,HIGH);
  // Set IO direction to output for all bank 1 (I/O pins 8-17)
  digitalWrite(inputSelectorCSPin,LOW);
  SPI.transfer(B01000000); // Send Device Opcode
  SPI.transfer(1);         // Select IODIR register for bank 1
  SPI.transfer(0);         // Set register
  digitalWrite(inputSelectorCSPin,HIGH);
  // IR
  irrecv.enableIRIn(); // Start the receiver
  pinMode(IRPowerPin, OUTPUT);
  pinMode(IRGroundPin, OUTPUT);
  digitalWrite(IRPowerPin, HIGH); // Power for the IR
  digitalWrite(IRGroundPin, LOW); // GND for the IR
  // Set up pins for encoder:
  pinMode (encoder0PinA,INPUT);
  pinMode (encoder0PinB,INPUT);
  pinMode (encoder1PinA,INPUT);
  pinMode (encoder1PinB,INPUT);
  // Set intial min volume level
  SetDac88812Volume(min_dbLevel);
  // Disable mute after startup delay
  delay(400);
  changeMute();
}

//////////////////////////////////////////////////////////////////////////////////////////////
// Function to change to next input
int changeInput(int change) {
  selectedInput = selectedInput + change;
  if (selectedInput > 6) { selectedInput = 1; }
  if (selectedInput < 1) { selectedInput = 6; }
  switch (selectedInput) {
    case 1:
      setMCP23S17Gpio(B11010101, B01001000);
      break;
    case 2:
      setMCP23S17Gpio(B11010101, B00110000);
      break;
    case 3:
      setMCP23S17Gpio(B11010100, B11010000);
      break;
    case 4:
      setMCP23S17Gpio(B11010011, B01010000);
      break;
    case 5:
      setMCP23S17Gpio(B11001101, B01010000);
      break;
    case 6:
      setMCP23S17Gpio(B10110101, B01010000);
    break;
  }
  setRelayToZero();
  muteEnabled = false;
  if (debugEnabled) {
    Serial.print("Selected Input: ");
    Serial.println(selectedInput);
  }
  delay(400);
}

int changeMute() {
  if (muteEnabled) {
    setMCP23S17Gpio(B10000000, B00000000);
    muteEnabled = false;
  } else {
    setMCP23S17Gpio(B00000000, B00000000);
    muteEnabled = true;
  }
  if (debugEnabled) {
    Serial.print("Mute enabled: ");
    Serial.println(muteEnabled);
  }
}

// Function to reset all all GPIO pins to 0 except for mute pinß
int setRelayToZero() {
  delay(3);
  setMCP23S17Gpio(B10000000, B00000000);
}

// Function to set GPIO pins on the MCP23S17
int setMCP23S17Gpio(int register_gpioa, int register_gpiob) {
  digitalWrite(inputSelectorCSPin,LOW);
  SPI.transfer(B01000000);        // Send Device Opcode
  SPI.transfer(18);               // Select register
  SPI.transfer(register_gpioa);   // Set GPIOA register
  SPI.transfer(register_gpiob);   // Set GPIOB register
  digitalWrite(inputSelectorCSPin,HIGH);
}
//////////////////////////////////////////////////////////////////////////////////////////////
// Functions to change volume
int changeVolume(float increment) {
  currentChangeVolumeIncrement = 0;
  float newDbLevel = currentDbLevel + increment;
  if (newDbLevel < max_dbLevel && newDbLevel > min_dbLevel) {
    currentChangeVolumeIncrement = increment;
    SetDac88812Volume(newDbLevel);
  } else if (newDbLevel >= max_dbLevel && (max_dbLevel - currentDbLevel) > 0.01) {
    SetDac88812Volume(max_dbLevel);
  } else if (newDbLevel <= min_dbLevel && (currentDbLevel - min_dbLevel) > 0.01) {
    SetDac88812Volume(min_dbLevel);
  } else {
    if (debugEnabled) {
      Serial.println ("No volume change");
    }
  }
}

int SetDac88812Volume(float newDbLevel) {
  unsigned int newDacR2Rvalue = 65536*(pow(10, (newDbLevel/20)));
  currentDacR2Rvalue = 65536*(pow(10, (currentDbLevel/20)));
  if (currentDacR2Rvalue == newDacR2Rvalue && currentChangeVolumeIncrement) {
    // This skips volume level steps that are too small or identical.
    while (currentDacR2Rvalue == newDacR2Rvalue && newDbLevel > (min_dbLevel - currentChangeVolumeIncrement)) {
      newDbLevel = newDbLevel + currentChangeVolumeIncrement;
      newDacR2Rvalue = 65536*(pow(10, (newDbLevel/20)));
      if (debugEnabled) {
        Serial.println ("Auto skipping steps");
      }
    }
  }
  if (newDacR2Rvalue <= 65536 && newDacR2Rvalue >= 0) {
    currentDbLevel = newDbLevel;
    currentDacR2Rvalue = newDacR2Rvalue;
    byte highByte = newDacR2Rvalue >> 8;
    unsigned int lowBytetemp = newDacR2Rvalue << 8;
    byte lowByte = lowBytetemp >> 8;
    digitalWrite(mdacCSPin, LOW);
    SPI.transfer(3); // This is the address code for setting both DACs, ie left and right
    SPI.transfer(highByte);
    SPI.transfer(lowByte);
    digitalWrite(mdacCSPin, HIGH);\
    // Print levels
    if (debugEnabled) {
      Serial.print ("dB: ");
      Serial.print (newDbLevel, 7);
      Serial.print (" / DAC Attenuation Level: ");
      Serial.println (newDacR2Rvalue);
    }
  } else {
    if (debugEnabled) {
      Serial.println ("SetDac88812Volume level ERROR");
    }
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////
// Main loop
//////////////////////////////////////////////////////////////////////////////////////////////
void loop() {
  // Read encoder 0
  encoder0n = digitalRead(encoder0PinA);
  if ((encoder0PinALast == LOW) && (encoder0n == HIGH)) {
    if (digitalRead(encoder0PinB) == LOW) {
      inputSelectorEncoderCounter++;
    } else {
      inputSelectorEncoderCounter--;
    }
  }
  encoder0PinALast = encoder0n;
  // Change input
  if (inputSelectorEncoderCounter > inputSelectorEncoderSensitivity) {
    changeInput(1);
    inputSelectorEncoderCounter = 0;
  }
  if (inputSelectorEncoderCounter < -inputSelectorEncoderSensitivity) {
    changeInput(-1);
    inputSelectorEncoderCounter = 0;
  }
  // Read encoder 1
  encoder1n = digitalRead(encoder1PinA);
  if ((encoder1PinALast == LOW) && (encoder1n == HIGH)) {
    if (digitalRead(encoder1PinB) == LOW) {
      changeVolume(volumeEncoderIncrement);
    } else {
      changeVolume(-volumeEncoderIncrement);
    }
  }
  encoder1PinALast = encoder1n;
  // Decode the IR if recieved
  if (irrecv.decode(&results)) {
    if (results.value == 4294967295) {
      IRsignal = lastIRoperation;
    } else {
      IRsignal = lastIRoperation = results.value;
    }
    switch (IRsignal) {
      case 2011287694: case 2011287569:
        changeVolume(iRIncrement);
        break;
      case 2011279502: case 2011279377:
        changeVolume(-iRIncrement);
        break;
      case 2011291790: case 2011291665:
        changeInput(1);
        break;
      case 2011238542: case 2011238417:
        changeInput(-1);
        break;
      case 2011265678: case 2011250705:
        changeMute();
        break;
      default:
        if (debugEnabled) {
          Serial.print("Unknown IR code: ");
          Serial.println(IRsignal);
        }
      break;
    }
    irrecv.resume();
  }

}
