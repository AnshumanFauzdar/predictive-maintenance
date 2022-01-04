import serial
import time
from pick import pick
import serial.tools.list_ports

comlist = serial.tools.list_ports.comports()

port = []
name = []
for element in comlist:

    port.append(element.device) # Device : COM name full length
    name.append(element.description) # Description : Full description of port

indicator: str = "=>"

title = "Select COM port :"

options = [port[0]+ " : " + name[0], port[1] + " : " + name[1], port[2] + " : " + name[2]]

option, index = pick(options, title, indicator)

ser = serial.Serial(option, 9600, timeout=1)
time.sleep(1)

for i in range(100):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        print(string)

ser.close()
