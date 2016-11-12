#include "SPI.h"

// Arduino Uno SPI pins
// Pin 11 = SDI
// Pin 13 = CLK

// Arduino Pro Micro SPI pins
// Pin 16 = Serial data out
// Pin 15 = CLK

const int inputSelectorCSPin = A1;

void setup() {
  // set the inputSelectorCSPin as an output:
  pinMode (inputSelectorCSPin, OUTPUT);
  digitalWrite(inputSelectorCSPin,HIGH);
  Serial.begin (9600);
  Serial.println ("Starting SPI..");
  SPI.begin();
  Serial.println ("Setting control registers..");
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

int setRelayToZero() {
  delay(40);
  setMCP23S17Gpio(B10000000, B00000000);
  delay(1000);
}

void loop() {
  Serial.println ("Switching relay 1");
  setMCP23S17Gpio(B11010101, B01001000);
  setRelayToZero();
  Serial.println ("Switching relay 2");
  setMCP23S17Gpio(B11010101, B00110000);
  setRelayToZero();
  Serial.println ("Switching relay 3");
  setMCP23S17Gpio(B11010100, B11010000);
  setRelayToZero();
  Serial.println ("Switching relay 4");
  setMCP23S17Gpio(B11010011, B01010000);
  setRelayToZero();
  Serial.println ("Switching relay 5");
  setMCP23S17Gpio(B11001101, B01010000);
  setRelayToZero();
  Serial.println ("Switching relay 6");
  setMCP23S17Gpio(B10110101, B01010000);
  setRelayToZero();
  Serial.println ("Switching relay mute");
  setMCP23S17Gpio(B00000000, B00000000);
  delay(1000);
  setRelayToZero();
}
