import time
import math

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
half = 128

tick = 0
while True:
	tick += 1
	if tick > full:
		tick = 0
	
	time_now = time.time()
	
	time_red = math.cos(time_now) * half + half
	time_green = math.cos(time_now + math.pi / 3) * half + half
	time_blue = math.cos(time_now + 2 * math.pi / 3)  * half + half
	
	red_on = tick < time_red
	green_on = tick < time_green
	blue_on = tick < time_blue
	
	gpio.output(red, red_on)
	gpio.output(green, green_on)
	gpio.output(blue, blue_on)
