import serial
import time

# Serial port name
#p = '/dev/ttyACM0'
p = 'COM5'

with serial.Serial(p, 9600) as ser:
    time.sleep(2)
    print(ser.readline().decode('utf-8'))
    ser.write(b'\x50') # Enable programming
    time.sleep(0.05)
    print(ser.readline().decode('utf-8'))
    print('Erasing...')
    ser.write(b'\x53')
    time.sleep(0.05)
    print(ser.readline().decode('utf-8'))

    # a = input('Programming done. Do you wish to verify? y/n: ')
    # if  a == 'Y' or a == 'y':
    #     print('Verifying...')
    #     err = False
    #     for i in range(0, len(ih.addresses())):
    #         addr = ih.addresses()[i]
    #         ser.write(b'\x52')
    #         ser.write(bytes([addr//256])) # high address byte
    #         ser.write(bytes([addr%256]))  # low address byte
    #         k = int(ser.readline().decode('utf-8'), 16)
    #         if k != ih[addr]:
    #             print('Error at address' + hex(addr))
    #             print('Got %d, was %d' % (k, ih[addr]))
    #             err = True
    #     if not err:
    #         print('Verification complete.')

    ser.write(b'\x40') # End programming
    print('Done.')
