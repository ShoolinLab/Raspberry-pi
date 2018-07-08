import serial
from time import sleep
# For PiB+ 2, Zero use:
ser = serial.Serial('/dev/serial0', 9600, timeout=1)
# For Pi3 use
#ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
i = 0
a=''
while True:
    string = ser.read()
    #stringww = ser.write(str(i))
    #i = i + 1
    a = a + string
    #print a
    #print " : ", a.find("GPGGA")
    if(a.count("$") == 2):
	if(a.find("GPGGA")>-1):
		li_gps = a.split(",")
        	time_gps = int(li_gps[1][:6])
		print time_gps
                time_gps = time_gps + 053000
		print time_gps
        	hour_gps = time_gps / 10000
       		min_gps  = (time_gps % 10000) / 100
		sec_gps  = (time_gps % 100)
		hour_gps, min_gps, sec_gps = str((hour_gps )%24), str((min_gps)%60), str(sec_gps)
        	print "Lat : " + li_gps[2] , "Long : " + li_gps[4]
		print "Time : " + hour_gps + " : " + min_gps + " : " + sec_gps
        a = "$"
print a
"""
    if len(string) == 0:
        print "Please wave a tag"
    else:
        string = string[1:11]   # Strip header/trailer
        print "string",string
        if string == '650033A2E5':
            print "hello user 1"
"""
