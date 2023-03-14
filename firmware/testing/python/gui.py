import tkinter as tk
from serial_read import get_serial_data

def update_color():
    value = float(get_serial_data())
    print(value)
    if value < 0.7:
        canvas.config(bg="green")
    elif value > 0.7:
        canvas.config(bg="red")
    else:
        canvas.config(bg="black")
    root.after(1000, update_color)

root = tk.Tk()
root.title("Serial Data Monitor")

# Create canvas to show color
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack()

# Update color periodically based on serial data
root.after(1000, update_color)
root.mainloop()
