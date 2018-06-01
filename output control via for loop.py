
import RPi.GPIO as g
#import time
from time import sleep 
g.setmode(g.BOARD)
g.setup(3,g.OUT)
g.setup(8,g.OUT)

a=[3,8]

g.output(3,1)
g.output(8,1)

sleep(2)
for i in a:
        g.output(i,0)
        sleep(2)

                
