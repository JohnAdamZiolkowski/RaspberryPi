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

def rgb(red_on, green_on, blue_on):
	gpio.output(red, red_on)
	gpio.output(green, green_on)
	gpio.output(blue, blue_on)
	
full = 255

red_level = 64
green_level = 0
blue_level = 32

tick = 0
while True:
	tick += 1
	if tick > full:
		tick = 0
	
	red_on = tick < red_level
	green_on = tick < green_level
	blue_on = tick < blue_level
	
	gpio.output(red, red_on)
	gpio.output(green, green_on)
	gpio.output(blue, blue_on)
