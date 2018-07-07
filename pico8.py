import RPi.GPIO as gpio

red = 16
button = 33

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(red, gpio.OUT)
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_DOWN)

gpio.output(red, True)

while True:
    light = gpio.input(button)
    gpio.output(red, light)
    
