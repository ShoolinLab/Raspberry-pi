import RPi.GPIO as shoolin 
import time 
shoolin.setmode(shoolin.BOARD)
shoolin.setwarnings(False)
shoolin.setup(3,shoolin.OUT)
while True:

	shoolin.output(3,shoolin.HIGH)
	print 'led on'
	time.sleep(1)

	shoolin.output(3,shoolin.LOW)
	time.sleep(1)
	print 'led off'

