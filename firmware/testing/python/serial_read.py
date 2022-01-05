import sys
import serial
import time
from pick import pick
import serial.tools.list_ports
import re

def use_regex(input):
    pattern = re.compile(r"[+-]?([0-9]*[.])?[0-9]+")
    return pattern.search(input, re.IGNORECASE)

comlist = serial.tools.list_ports.comports()

port = []
name = []
for element in comlist:

    port.append(element.device)  # Device : COM name full length
    name.append(element.description)  # Description : Full description of port

indicator: str = "=>"

title = "Select COM port :"

# Exit with error code 1 if no ports found
if len(port) <= 0:
    print("No device connected")
    sys.exit(1)

options = []

for i in range(0, len(port)):
    options.append(port[i] + " : " + name[i])

option, index = pick(options, title, indicator)

ser = serial.Serial(port[index], 9600, timeout=1)
time.sleep(1)


# Print all serial port data
def print_serial_data():
    while(True):
        line = ser.readline()
        if line:
            string = line.decode()
            print(string)


while(True):
    line = ser.readline()
    if line:
        string = line.decode()
        # change "Pressure = " to any req word
        if "Pressure = " in string:
            num = int(use_regex(string).group(0))

            # add custome condition here
            print(num)

ser.close()
