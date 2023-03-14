import serial.tools.list_ports
import time
import re
from pick import pick


comlist = serial.tools.list_ports.comports()

port = []
name = []
for element in comlist:

    port.append(element.device)  # Device : COM name full length
    name.append(element.description)  # Description : Full description of port

indicator: str = "=>"

title = "Select COM port :"

# Exit with error code 1 if no ports found
if not port:
    print("No COM ports found.")
    exit()

options = []

for i in range(0, len(port)):
    options.append(port[i] + " : " + name[i])

option, index = pick(options, title, indicator)

ser = serial.Serial(port[index], 115200, timeout=1)
time.sleep(1)

def get_serial_data():
    # Send command to device
    ser.write("AT+RUNIMPULSE\r\n".encode())
    time.sleep(1)

    # Continuously extract number data from response
    while True:
        response = ""
        while True:
            data = ser.readline()
            if not data:
                break
            decoded_data = data.decode("utf-8")
            response += decoded_data
            match = re.search(r"VALUE: ([0-9]*\.[0-9]+)", decoded_data)
            if match:
                number_data = match.group(1)
                return number_data
                
    ser.close()
