import RPi.GPIO as gpio

left = 11
right = 13
up = 15
down = 16
a = 18
b = 22
select = 29
start = 32
last_state = {
    "left": False,
    "right": False,
    "up": False,
    "down": False,
    "A": False,
    "B": False,
    "select": False,
    "start": False
}

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(left, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(right, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(up, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(down, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(a, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(b, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(select, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(start, gpio.IN, pull_up_down=gpio.PUD_DOWN)


while True:
    state = {
        "left": gpio.input(left),
        "right": gpio.input(right),
        "up": gpio.input(up),
        "down": gpio.input(down),
        "A": gpio.input(a),
        "B": gpio.input(b),
        "select": gpio.input(select),
        "start": gpio.input(start)
    }
    for button in state:
        if state[button] != last_state[button]:
            if state[button]:
                print("pressed " + button)
            else:
                print("released " + button)

    last_state = state
