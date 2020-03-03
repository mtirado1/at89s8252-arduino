# at89s8252-arduino

This is a programmer for the Atmel AT89S8252 microcontroller through Arduino's SPI port.

# Installation

## Hardware

Upload `progammer.ino` to your Arduino board.

Make the following connections between the Arduino and the AT89S8252.


| AT89S8252 | Arduino |
|-----------|---------|
| RESET     | Pin 9   |
| MOSI      | Pin 11  |
| MISO      | Pin 12  |
| SCK       | Pin 13  |

## Software

Install PySerial and IntelHex modules for Python.

```
python3 -m pip install pyserial intelhex
```

# Usage

Edit `programmer.py` to change the path to the hex file and select the serial port.

Program the microcontroller by running the script.
