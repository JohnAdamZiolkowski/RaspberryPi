import time

import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

red = 12
green = 32
blue = 36

gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)
gpio.setup(blue, gpio.OUT)

while True:
    gpio.output(red, True)
    gpio.output(green, False)
    gpio.output(blue, False)
    time.sleep(1)

    gpio.output(red, False)
    gpio.output(green, True)
    gpio.output(blue, False)
    time.sleep(1)

    gpio.output(red, False)
    gpio.output(green, False)
    gpio.output(blue, True)
    time.sleep(1)
