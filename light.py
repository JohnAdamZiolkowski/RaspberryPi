import time
import math

import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(12, gpio.OUT)

tick = 0
while True:
	tick += 1
	if tick > 255:
		tick = 0
	
	time_now = time.time()
	time_cos = math.cos(time_now)
	time_cos = time_cos * 128 + 128
	
	on = tick < time_cos
	
	gpio.output(12, on)
