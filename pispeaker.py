#object:-if card matches it will speak Permission Granted
#sudo apt-get install espeak         ...to install espeak
import serial
from time import sleep
ser = serial.Serial("/dev/serial0",9600,timeout=1)
from os import system
i = 0
while True:
        val = ser.read(12)
        sleep(.1)
        if len( val.strip() ) == 12:
                if val== "0200107EDCB0":
                        system("espeak -v +f3 \"Permision, Granted\"")
                else:
                        system("espeak -v +f3 \"Permision, Denied\"")




