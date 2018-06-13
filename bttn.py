from time import sleep
from Tkinter import *
class App:

  def _init_(self,master):
  frame = Frame(master) 
  frame.pack()
  Label(frame, text='Turn led on').grid(row=0, column=0)
  Label(frame, text='Turn led off').grid(row=1, column=0)

  button = Button()frame,text='lED 0 ON', command=self.convert0)
  button.grid(row=2,columnspan=2)

  def convert0(self,tog=[0]);
     tog[0] = not tog[0]
     if tog[0]:
     print('led 0 off')

     elif:
     print('led 0 ON')


root = Tk()
root.wm_title('LED on & off program')

app = App(root)
root.mainloop()