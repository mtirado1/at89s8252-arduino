# at89s8252-arduino

This is a programmer for the Atmel AT89S8252 microcontroller through Arduino's SPI port from an intel hex file.

# Installation

## Hardware

Upload `progammer.ino` to your Arduino board.

Connect the target microcontroller to VCC and GND, and add a crystal between XTAL1 and XTAL2. Make the following connections between the Arduino and the AT89S8252.


| AT89S8252     | Arduino |
|---------------|---------|
| RESET (Pin 9) | Pin 9   |
| MOSI  (Pin 6) | Pin 11  |
| MISO  (Pin 7) | Pin 12  |
| SCK (Pin 8)   | Pin 13  |

## Software

Install PySerial and IntelHex modules for Python.

```
python3 -m pip install pyserial intelhex
```

# Usage

Edit `writeprogram.py` to change the path to the hex file and select the serial port.

In the blink directory there is blinky.hex that is a sample program.

Program the microcontroller by running the script.

If you want erase the chip run `eraser.py` it erase both program and data space.

If you want dump the program on chip run `readprogram.py`

If you want check the chip program from a file run `verifyprogram.py`

Edit scripts for changing file hex names and comm port settings.

The same is for data space with:

writedata.py

readdata.py

verifydata.py
