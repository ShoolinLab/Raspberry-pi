import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
   global count
   count = count+1
   print count

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()
