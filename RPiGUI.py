from tkinter import *
from gpiozero import LED
from functools import partial
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

# Hardware
g_led = LED(21)
b_led = LED(20)
r_led = LED(16)

# GUI
window = Tk()
window.title("5.2C")

# Functions
def toggle(clicked):
    if clicked == 1:
        g_led.on()
        b_led.off()
        r_led.off()
    elif clicked == 2:
        g_led.off()
        b_led.on()
        r_led.off()
    elif clicked == 3:
        g_led.off()
        b_led.off()
        r_led.on()
    else:
        print("Error?")
def close():
    GPIO.cleanup()
    window.destroy()

# Buttons
exit_button = Button(window, text = "Exit", command = close, bg = "bisque2", height = 1, width = 3)

# Partial() is used to pass an argument defining which buttons clicked as opposed to individual functions for each.
g_button = Button(window, text = "Green LED", command = partial(toggle, 1), bg = "lime green", height = 1, width = 12)
b_button = Button(window, text = "Blue LED", command = partial(toggle, 2), bg = "blue", height = 1, width = 12)
r_button = Button(window, text = "Red LED", command = partial(toggle, 3), bg = "red", height = 1, width = 12)

exit_button.grid(row = 0, column = 0)
g_button.grid(row = 1, column = 0)
b_button.grid(row = 2, column = 0)
r_button.grid(row = 3, column = 0)

window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()