import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

red = 12
green = 32
blue = 36

gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)
gpio.setup(blue, gpio.OUT)

gpio.output(red, True)
gpio.output(green, True)
gpio.output(blue, True)
