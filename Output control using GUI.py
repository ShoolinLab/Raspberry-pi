import RPi.GPIO as io
from time import sleep
from Tkinter import*
window=Tk()

window.title("LED ON/OFF")
window.geometry('360x480')
window.configure(background = 'blue')


io.setwarnings(False)

io.setmode(io.BOARD)

io.setup(3,io.OUT)
led=3

def clicked():
    
        io.output(led,False)      
             
        sleep(1)

        window.configure(background = 'black')
        window.title("LED OFF")
def clicked1():
    
        io.output(led,True)      
             
        sleep(1)        

        window.configure(background = 'white')
        window.title("LED ON")
              


    
btn = Button(window, text="LED OFF", bg = "silver", command=clicked)
btn.grid(column=2, row=2)

btn = Button(window, text="LED ON", bg = "gold", command=clicked1)
btn.grid(column=4, row=2)
            

window.mainloop()
