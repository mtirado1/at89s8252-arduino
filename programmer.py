import serial
import time
from intelhex import IntelHex

# Path to hex file
f = 'test/aaa.hex'
# Serial port name
p = '/dev/ttyACM0'

# Read hex file
ih = IntelHex()
ih.fromfile(f, format='hex')


with serial.Serial(p, 9600) as ser:
    time.sleep(2)
    print(ser.readline())
    ser.write(b'\x50') # Enable programming
    ih.dump()
    print('Programming...')
    for i in range(0, len(ih.addresses())):
        addr = ih.addresses()[i]
        ser.write(b'\x51')
        ser.write(bytes([addr//256])) # high address byte
        ser.write(bytes([addr%256]))  # low address byte
        ser.write(bytes([ih[addr]]))  # data byte
        time.sleep(0.05)
    ser.readline()
   
    a = input('Programming done. Do you wish to verify? y/n: ')
    if  a == 'Y' or a == 'y':
        print('Verifying...')
        err = False
        for i in range(0, len(ih.addresses())):
            addr = ih.addresses()[i]
            ser.write(b'\x52')
            ser.write(bytes([addr//256])) # high address byte
            ser.write(bytes([addr%256]))  # low address byte
            k = int(ser.readline().decode('utf-8'), 16)
            if k != ih[addr]:
                print('Error at address' + hex(addr))
                print('Got %d, was %d' % (k, ih[addr]))
                err = True
        if not err:
            print('Verification complete.')
    
    ser.write(b'\x40') # End programming
    print('Done.')

