import serial
import time
from intelhex import IntelHex
from config import *

# Path to hex file
f = data_targetFile
# Serial port name
p = serialPort

# Read hex file
ih = IntelHex()

ih.fromfile(f, format='hex')

if ih.addresses()[len(ih.addresses()) - 1]  > 0x7FF:
    a = input('The data is too large, max data is 2048 bytes, continue? y/n: ')
    if  a != 'Y' and a != 'y':
        quit()

with serial.Serial(p, 9600) as ser:
    time.sleep(2)
    print(ser.readline().decode('utf-8'))
    ser.write(b'\x50') # Enable programming
    ih.dump()
#    print('Programming...')
    print(ser.readline().decode('utf-8'))
    # conta = 0
    # for i in range(0, len(ih.addresses())):
    #     addr = ih.addresses()[i]
    #     if conta == 256:
    #         conta = 0
    #         print(hex(addr))
    #     conta += 1
    #     ser.write(b'\x51')
    #     ser.write(bytes([addr//256])) # high address byte
    #     ser.write(bytes([addr%256]))  # low address byte
    #     ser.write(bytes([ih[addr]]))  # data byte
    #     #time.sleep(0.05)
    #     ser.readline()

#    a = input('Programming done. Do you wish to verify? y/n: ')
    conta = 0
    #if  a == 'Y' or a == 'y':
    print('Verifying...')
    err = False
    for i in range(0, len(ih.addresses())):
        addr = ih.addresses()[i]
        if addr <= 0x7FF:
            if conta == 256:
                conta = 0
                print(hex(addr))
            conta += 1
            ser.write(b'\x54')
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
    print(ser.readline().decode('utf-8'))
    print('Done.')
