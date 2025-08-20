# basic script to send keystrokes from a rp2040 based device.
import usb_hid
from adafruit_hid import keyboard, keyboard_layout_us


keyboard = keyboard.Keyboard(usb_hid.devices)
layout = keyboard_layout_us.KeyboardLayoutUS(keyboard)


def string(text):
    layout.write(text)

    
string("Hello, World")
