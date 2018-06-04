import RPi.GPIO as io
io.setwarnings(False)

io.setmode(io.BOARD)

IR_INPUT1 = 3#level tester
IR_INPUT2 = 8#level tester


Led1 = 5#indicator 1
Led2 = 7#indicator 2


io.setup(IR_INPUT1,io.IN)
io.setup(IR_INPUT2,io.IN)

io.setup(Led1,io.OUT)
io.setup(Led2,io.OUT)

while True:

        c = io.input(IR_INPUT1)
        d = io.input(IR_INPUT2)
        
        print 
        
        print d
        
       
        
        if c==0 and d==0:
            io.output(Led1,True)
            io.output(Led2,True)
           
            print 'cd',c ,d 
            print 'null'
                         
        if c==0 and d==1:
            io.output(Led1,True)
            io.output(Led2,False)
            
            print "cd", c ,d 
            print 'med'

        if c==1 and d==0:
            io.output(Led1,False)
            io.output(Led2,True)
            
            print "cd", c ,d 
            print 'low'

        if c==1 and d==1:
            io.output(Led1,False)
            io.output(Led2,False)
            
            print "cd", c ,d 
            print 'high'
                                
                                       

