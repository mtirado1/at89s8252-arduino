import serial
import time
from intelhex import IntelHex
from config import *
import sys
import string

# Path to hex file
#f = code_targetFile
# Serial port name
#p = serialPort

# Read hex file
#ih = IntelHex()

#ih.fromfile(f, format='hex')

# if ih.addresses()[len(ih.addresses()) - 1]  > 0x1FFF:
#     a = input('The program is too large, max memory is 8192 bytes, continue? y/n: ')
#     if  a != 'Y' and a != 'y':
#         quit()

print('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
if len(sys.argv) != 2:
    print("Usage: writelock.py argument, the argument can be a number from 1 to 3.")
    quit()

print(sys.argv[1])
if sys.argv[1].isnumeric():
    fuses = int(sys.argv[1])
    print(fuses)
    error = 0
else:
    error=1
    print("error1")

if error == 0 and fuses <= 3 and fuses >= 1:
    print(fuses)
else:
    error = 1
    print("error2")

if error == 1:
    print("Fuses must be a nunmber between 1 and 3.")
    quit()

# Serial port name
p = serialPort

with serial.Serial(p, 9600) as ser:
    time.sleep(2)
    print(ser.readline().decode('utf-8'))
    ser.write(b'\x50') # Enable programming
    time.sleep(0.05)
    print(ser.readline().decode('utf-8'))
    print('Locking...')
    ser.write(b'\x56')
    ser.write(bytes(fuses))

    time.sleep(0.05)
    print(ser.readline().decode('utf-8'))

    ser.write(b'\x40') # End programming
    print('Done.')
