import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

######for ultrasonic
import RPi.GPIO as io

import time
from time import sleep

io.setwarnings(False)

io.setmode(io.BOARD)

io.setup(3,io.OUT)
io.setup(5,io.IN)
io.setup(10,io.OUT)

#### SMTP

fromaddr = "raj.rohit19931996@gmail.com"
toaddr = "rohit.razza@gmail.com"
  
# instance of MIMEMultipart
msg = MIMEMultipart()
 
# storing the senders email address  
msg['From'] = fromaddr
 
# storing the receivers email address 
msg['To'] = toaddr
 
# storing the subject 
msg['Subject'] = "hi this rohit"
 
# string to store the body of the mail
body = "Pls SEE THE SMS"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login(fromaddr,"123456")
 
# Converts the Multipart msg into a string
text = msg.as_string()

## ULTRASONIC

while(1):
        io.output(3,False)
        sleep(0.2)

        io.output(3,True)
        sleep(0.00001)

        io.output(3,False)
        
            
        while io.input(5)==0:
            pulse_start=time.time()
        

        while io.input(5)==1:
            pulse_end=time.time()

        t=pulse_end-pulse_start

        d1= t * 17150
        
        d1= round(d1, 2)
        print("distanc1:",d1)

        if(d1>10):
            io.output(10,True)
            # sending the mail
            s.sendmail(fromaddr, toaddr, text)
             
            # terminating the session
            #s.quit()
            print("Congratulations")
        else:
            io.output(10,False)
s.quit()
print("Congratulations")

