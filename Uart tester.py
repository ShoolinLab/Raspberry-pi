#sudo systemctl disable hciuart

import serial
from time import sleep
ser = serial.Serial("/dev/serial0",9600,timeout=1)

i = 0
while True:
        i = i + 1 
        print ser.read()
        ser.write(str(i))
        sleep(1)
