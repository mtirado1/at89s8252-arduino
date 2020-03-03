// AT89S8252 Programmer
// Author: mtirado

// Arduino Pin Connections

// MOSI: pin 11
// MISO: pin 12
// SCK:  pin 13
// RST:  pin 9



#include <SPI.h>

#define RSTPin 9

unsigned char pgm_instruction = 0;
unsigned int pgm_address = 0;
unsigned char pgm_data = 0;

// Programming Enable Instruction
void progEnable() {
  digitalWrite(RSTPin, HIGH);
  delay(50);
  SPI.transfer(0xac);
  SPI.transfer(0x53);
  SPI.transfer(0x00);
}

// Write to code memory
void writeCode(unsigned int addr, unsigned char data) {
  SPI.transfer(((addr & 0xff00) >> 5) + 0x02);
  SPI.transfer(addr & 0x00ff);
  SPI.transfer(data);
  delay(5);
}

// Read from code memory
unsigned char readCode(unsigned int addr) {
  SPI.transfer(((addr & 0xff00) >> 5) + 0x01);
  SPI.transfer(addr & 0x00ff);
  return SPI.transfer(0x00);
}

void setup() {
  Serial.begin(9600);
  SPI.setBitOrder (MSBFIRST);
  SPI.setClockDivider(SPI_CLOCK_DIV64);
  SPI.begin();

  pinMode(RSTPin, OUTPUT);
  delay(500);
  Serial.println("Programmer ready.");
}

void loop() {

  if (Serial.available() > 0) {
    pgm_instruction = Serial.read();
    switch (pgm_instruction) {
      case 0x50: // Programming enable
        progEnable();
        Serial.println("Programming mode enabled.");
      break;

      case 0x51: // Write to code memory
        pgm_address = Serial.read() << 8;
        pgm_address |= Serial.read();
        pgm_data = Serial.read();
        writeCode(pgm_address, pgm_data);
      break;

      case 0x52: // Read from code memory
        pgm_address = Serial.read() << 8;
        pgm_address |= Serial.read();
        Serial.println(readCode(pgm_address), HEX);
      break;

      case 0x40: // End programming
      digitalWrite(RSTPin, LOW);
      Serial.println("Programming mode disabled.");
      break;
    }
  }
}
