# run with python .\gui.py
# install: https://lawsie.github.io/guizero/
# change value of THRESHOLD to change pass-fail criteria (input a decimal value)
# change string "Pressure = " any other requirement(s)

from serial_read import serial_data_findbystring
from guizero import App, Text, Picture

THRESHOLD = 300.0

# Action you would like to perform
def value_update():
    value = serial_data_findbystring("Pressure = ")
    text.value = value
    if (value and value > THRESHOLD):
        text.text_color = "#00ff00" # green
        #picture.value = "pass-min.png"
    else:
        text.text_color = "#ff3333" # red
        #picture.value = "fail-min.png"

app = App("Predictive Maintenance", bg = "#121212") # #121212: black

text = Text(app, text=value_update)
#picture = Picture(app)

text.repeat(100, value_update)  # Schedule call to every "n"ms(1s = 1000ms)

app.display()
