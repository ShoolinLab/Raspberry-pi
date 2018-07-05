import RPi.GPIO as G
from Tkinter import * 
root=Tk()
root.title("Fan Rotation")
root.configure(bg="black")
root.geometry("240x120")

G.setmode(G.BCM)
G.setwarnings(False)
G.setup(14,G.OUT)
G.setup(15,G.OUT)
G.setup(18,G.OUT)
G.setup(23,G.OUT)
G.setup(24,G.IN)
G.setup(25,G.IN)


pin1=14
pin2=15
pin3=18
pin4=23
ir1=G.input(24)
ir2=G.input(25)

def forward():
	G.output(pin1,1)
	G.output(pin2,0)
	G.output(pin3,1)
	G.output(pin4,0)
	print('Forward')

def backward():
	G.output(pin1,0)
	G.output(pin2,1)
	G.output(pin3,0)
	G.output(pin4,1)
	print('Backward')

def stop():
	G.output(pin1,0)
	G.output(pin2,0)
	G.output(pin3,0)
	G.output(pin4,0)
def right():
	G.output(pin1,1)
	G.output(pin2,0)
	G.output(pin3,0)
	G.output(pin4,0)
def left():
	G.output(pin1,0)
	G.output(pin2,0)
	G.output(pin3,1)
	G.output(pin4,0)
"""
while True:
	ir1=G.input(24)
	ir2=G.input(25)
	if(ir1==1 and ir2==0):
		forward()
		print('Forward')

	elif(ir1==0 and ir2==1):
		backward()
		print('Backward')
	elif(ir1==0 and ir2==0):
		stop()
		print('Stop')
	elif(ir1==1 and ir2==1):
		print('error')
"""

btn=Button(root,text="clocwise",width=10,bg="silver",fg="black",command=forward)
btn.grid(row=1,column=1)
btn=Button(root,text="anticlockwise",width=10,bg="silver",fg="black",command=backward)
btn.grid(row=1, column=2)





root.mainloop()
   
