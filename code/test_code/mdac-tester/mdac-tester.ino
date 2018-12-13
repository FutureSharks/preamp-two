#include "SPI.h"

// Arduino Uno SPI pins
// Pin 11 = SDI
// Pin 13 = CLK

// Arduino Pro Micro SPI pins
// Pin 16 = Serial data out
// Pin 15 = CLK

const int slaveSelectPin = 10;
int timedelay = 500;
unsigned int increment = 965;
// Address code 3 = Both A and B DACs
int addr_decode = 3;

void setup() {
  pinMode (slaveSelectPin, OUTPUT);
  Serial.begin (9600);
  delay(1000);
  Serial.print ("Starting SPI..");
  SPI.begin();
}

void loop() {
  for (unsigned int level = 0; level < 64568; level = level + increment) {
    DACWrite(addr_decode, level);
    delay(timedelay);
    Serial.print ("Level: ");
    Serial.print (level);
    Serial.print (" / ");
    Serial.println (level, BIN);
  }
}

void DACWrite(int addr_decode, unsigned int level) {
  digitalWrite(slaveSelectPin, LOW);
  SPI.transfer(addr_decode);
  int highByte = level >> 8;
  unsigned int lowBytetemp = level << 8;
  int lowByte = lowBytetemp >> 8;
  SPI.transfer(highByte);
  SPI.transfer(lowByte);
  digitalWrite(slaveSelectPin, HIGH);
}
