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
optionServo, indexServo = pick(options, "Select COM port for servo:", indicator)

ser = serial.Serial(port[index], 115200, timeout=1)
serServo = serial.Serial(port[indexServo], 9600, timeout=1)
time.sleep(1)

# Print all serial port data
def print_serial_data():
    while(True):
        line = ser.readline()
        if line:
            string = line.decode()
            print(string)

# One time function - Stackoverflow
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
def my_function():
    ser.write("AT+RUNIMPULSE".encode())
    # Enter Key
    ser.write("\r".encode())

action = run_once(my_function)

word, idx = pick(["Onion: 	", "Potato: 	", "Tomato: 	", "Unknown: 	"], "Select object of interest:", indicator)

def serial_data_findbystring():
    line = ser.readline()
    action()
    if line:
        string = line.decode()
        print(word)
        if word in string:
            num = float(use_regex(string).group(0))
            if num > 0.70:
                serServo.write("10".encode())
                serServo.write("\r".encode())
            elif num <= 0.70:
                serServo.write("90".encode())
                serServo.write("\r".encode())                
            return num

if __name__ == "__main__":
    # run python .\serial_read.py
    while(True):
        num = serial_data_findbystring()
        print(num)