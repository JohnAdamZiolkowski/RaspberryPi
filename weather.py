import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

red_pin = 12
green_pin = 32
blue_pin = 36

gpio.setup(red_pin, gpio.OUT)
gpio.setup(green_pin, gpio.OUT)
gpio.setup(blue_pin, gpio.OUT)


def rgb(red_on, green_on, blue_on):
    gpio.output(red, red_on)
    gpio.output(green, green_on)
    gpio.output(blue, blue_on)


full = 255


def render_color(red_level, green_level, blue_level, length):
    ticks = length * 100

    for t in range(ticks):
        tick = t & full

        red_on = tick < red_level
        green_on = tick < green_level
        blue_on = tick < blue_level

        gpio.output(red_pin, red_on)
        gpio.output(green_pin, green_on)
        gpio.output(blue_pin, blue_on)


red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
miku = (0, 255, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)

white = (255, 255, 255)
half_white = (128, 128, 128)
off = (0, 0, 0)


def pad_number(number):
    if number == 0:
        return 1
    else:
        return (1 + number * 0.25) / number


def display(color, number):
    red_level = color[0]
    green_level = color[1]
    blue_level = color[2]

    time_each = pad_number(number) / 2

    render_color(red_level, green_level, blue_level, number)
    time.sleep(time_each)

    render_color(0, 0, 0, number)
    time.sleep(time_each)


def render_weather(weather):
    print("rendering weather")
    render_temp(weather)
    render_wet(weather)
    render_wind(weather)
    render_alert(weather)
    display(off, 1)


def render_temp(weather):
    print("rendering temp")
    time.sleep(1)
    temp = int(weather["temp"])
    negative = temp < 0
    temp = abs(temp)
    temp_string = str(temp)

    if temp == 0:
        display(yellow, 1)
        return

    for digit in range(len(temp_string)):
        value = int(temp_string[digit])
        for i in range(value):
            if negative:
                display(miku, value)
            else:
                display(orange, value)

        time.sleep(0.5)


def render_wet(weather):
    print("rendering wet")
    time.sleep(1)
    type_of_wet = weather["wet"]["type"]
    chance = int(weather["wet"]["chance"]) / 10

    if chance <= 0:
        display(yellow, 1)

    else:
        for i in range(chance):
            if type_of_wet == "rain":
                display(blue, chance)
                time.sleep(pad_number(chance))
            elif type_of_wet == "snow":
                display(white, chance)

            time.sleep(0.5)


def render_wind(weather):
    print("rendering wind")
    time.sleep(1)
    wind_level = int(weather["wind"])
    if wind_level <= 0:
        return

    for i in range(wind_level):
        display(white, wind_level)


def render_alert(weather):
    print("rendering alert")
    time.sleep(1)
    alert = weather["alert"]
    if not alert:
        return

    for i in range(9):
        display(red, 9)


def set_rgb(red_level, green_level, blue_level):
    print("setting to:", red_level, green_level, blue_level)


example_weather = dict()
example_weather["temp"] = "-26"

example_weather["wet"] = dict()
example_weather["wet"]["type"] = "rain"
example_weather["wet"]["chance"] = "90"

example_weather["wind"] = "4"

example_weather["alert"] = True

render_weather(example_weather)
