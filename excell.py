import xlrd
import xlwt
import requests
import RPi.GPIO as io
import time
from time import sleep

io.setwarnings(False)

io.setmode(io.BOARD)

TRIG=3
ECHO=5

io.setup(TRIG,io.OUT)
io.setup(ECHO,io.IN)

book=xlrd.open_workbook("list.xls")
sh=book.sheet_by_index(0)

print dir(sh)





def ultra():
         
        io.output(TRIG,False)
        sleep(0.2)

        io.output(TRIG,True)
        sleep(0.00001)

        io.output(TRIG,False)
        
            
        while io.input(ECHO)==0:
            pulse_start=time.time()
        

        while io.input(ECHO)==1:
            pulse_end=time.time()

        t=pulse_end-pulse_start

        d= t * 17150
        
        d= round(d, 2)

        print "d:",d,"cm"
        sleep(0.5)
        return str(d)



    
while True:

            
    ultra()    
    rb=xlwt.Workbook()
    sheet=rb.add_sheet("2")
    sheet.write(1,1,"d")
    rb.save("list.xls")
           
