import sys
import serial
import time
from pick import pick
import serial.tools.list_ports
import re
import time
from rpi_ws281x import PixelStrip, Color
import argparse
import requests

# defining the api-endpoint
API_ENDPOINT = "https://api.thingspeak.com/update.json"

# your API key here
API_KEY = "KEY"

# LED strip configuration:
LED_COUNT = 6        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(
                (int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
# REGEX STARTS

def use_regex(input):
    pattern = re.compile(r"[0-9]*\.[0-9]+")
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

ser = serial.Serial(port[index], 115200, timeout=1)
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

# Enter matching string
val = input("Enter value : ")

while(True):
    line = ser.readline()
    action()
    if line:
        string = line.decode()
        # change "none: 	" to any matching string
        if val in string:
            num = float(use_regex(string).group(0))
            # add custom condition here
            print(num)

            data = {'api_key':API_KEY,
                    'field4':num,
		    }

            r = requests.post(url = API_ENDPOINT, data = data)

            if num > 0.5:
                colorWipe(strip, Color(255, 0, 0))
            if num < 0.5:
                colorWipe(strip, Color(0, 255, 0))

ser.close()
