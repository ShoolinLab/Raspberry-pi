import RPi.GPIO as io
import time
from  time import sleep

io.setwarnings(False)

io.setmode(io.BOARD)

TRIG1=3
ECHO1=5
TRIG2=7
ECHO2=8
TRIG3=10
ECHO3=11
TRIG4=12
ECHO4=13   

maximum=50
minimum=5

io.setup(TRIG1,io.OUT)
io.setup(TRIG2,io.OUT)
io.setup(TRIG3,io.OUT)
io.setup(TRIG4,io.OUT)
io.setup(ECHO1,io.IN)
io.setup(ECHO2,io.IN)
io.setup(ECHO3,io.IN)
io.setup(ECHO4,io.IN)        

def ultra1():
    
    io.output(TRIG1,False)
    sleep(0.2)

    io.output(TRIG1,True)
    sleep(0.00001)

    io.output(TRIG1,False)

    while io.input(ECHO1)==0:
        pulse_start=time.time()

    while io.input(ECHO1)==1:
        pulse_end=time.time()

    t1=pulse_end-pulse_start

    d1= t1 * 17150
    d1=round(d1,2)

    return d1


def ultra2():
    
    io.output(TRIG2,False)
    sleep(0.2)

    io.output(TRIG2,True)
    sleep(0.00001)

    io.output(TRIG2,False)

    while io.input(ECHO2)==0:
        pulse_start=time.time()

    while io.input(ECHO2)==1:
        pulse_end=time.time()

    t2=pulse_end-pulse_start

    d2= t2 * 17150
    d2=round(d2,2)

    return d2

def ultra3():
    
    io.output(TRIG3,False)
    sleep(0.2)

    io.output(TRIG3,True)
    sleep(0.00001)

    io.output(TRIG3,False)

    while io.input(ECHO3)==0:
        pulse_start=time.time()

    while io.input(ECHO3)==1:
        pulse_end=time.time()

    t3=pulse_end-pulse_start

    d3= t3 * 17150
    d3=round(d3,2)

    print d3
    
def ultra4():
    
    io.output(TRIG4,False)
    sleep(0.2)

    io.output(TRIG4,True)
    sleep(0.00001)

    io.output(TRIG4,False)

    while io.input(ECHO4)==0:
        pulse_start=time.time()

    while io.input(ECHO4)==1:
        pulse_end=time.time()

    t4=pulse_end-pulse_start

    d4= t4 * 17150
    d4=round(d4,2)

    print d4

while True:
    c=ultra1()
    d=ultra2()
    e=ultra3()
    f=ultra4()
    if (c<maximum & c>minimum):
       print " c side Safe"
       
    if (d<maximum & d>minimum):
       print " d side Safe"

    if (e<maximum & e>minimum):
       print " e side Safe"
       
    if (f<maximum & f>minimum):
       print " f side Safe"   
       
