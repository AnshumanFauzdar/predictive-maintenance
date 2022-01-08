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
def serial_data():
    line = ser.readline()
    if line:
        string = line.decode()
        return string

def serial_data_findbystring(word: str):
    line = ser.readline()
    if line:
        string = line.decode()
        if word in string:
            num = float(use_regex(string).group(0))
            return num

if __name__ == "__main__":
    # run python .\serial_read.py
    while(True):
        num = serial_data_findbystring("Pressure = ")
        print(num)
