import serial
import time
from intelhex import IntelHex

# Path to hex file
f = 'code.hex'
# Serial port name
p = '/dev/ttyACM0'

# lee archivo hex
ih = IntelHex()
ih.fromfile(f, format='hex')


with serial.Serial(p, 9600) as ser:
    time.sleep(2)
    print(ser.readline())
    ser.write(b'\x50') # Enable programming
    print('Programming...')
    
    for i in range(0, len(ih)):
        ser.write(b'\x51')
        ser.write(bytes([i//256])) # high address byte
        ser.write(bytes([i%256]))  # low address byte
        ser.write(bytes([ih[i]]))  # data byte
    ser.write(b'\x40') # End programming
    print('Done.')

