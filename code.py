# Write your code here :-)
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull, DriveMode
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid

gate = DigitalInOut(board.D11)
gate.direction = Direction.OUTPUT
gate.value = False

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

btn = DigitalInOut(board.BUTTON)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

keyboard = Keyboard(usb_hid.devices)

while True:
    if not btn.value:
        led.value = False
        for i in range(20):
            time.sleep(1)
            keyboard.press(Keycode.F)
            keyboard.release(Keycode.F)
            gate.value = True
            time.sleep(0.001)
            gate.value = False
    else:
        led.value = True

