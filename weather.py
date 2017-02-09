import time
import RPi.GPIO as gpio
from weather_api import WeatherAPI

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

red_pin = 12
green_pin = 32
blue_pin = 36

gpio.setup(red_pin, gpio.OUT)
gpio.setup(green_pin, gpio.OUT)
gpio.setup(blue_pin, gpio.OUT)

# define colors
red = (255, 0, 0)
orange = (255, 32, 0)
yellow = (255, 96, 0)
green = (0, 255, 0)
miku = (0, 128, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)

white = (255, 255, 255)
half_white = (128, 128, 128)
off = (0, 0, 0)


def rgb(red_on, green_on, blue_on):
    gpio.output(red_pin, red_on)
    gpio.output(green_pin, green_on)
    gpio.output(blue_pin, blue_on)


full = 255


def render_color(red_level, green_level, blue_level, length):
    start_time = time.time()
    end_time = start_time + length

    tick = 0
    while time.time() < end_time:
        tick += 1
        if tick > full:
            tick = 0

        red_on = tick < red_level
        green_on = tick < green_level
        blue_on = tick < blue_level

        gpio.output(red_pin, red_on)
        gpio.output(green_pin, green_on)
        gpio.output(blue_pin, blue_on)


def pad_number(number):
    if number == 0:
        return 1
    else:
        return (1 + number * 0.5) / number


def display_count(color, number):
    time_each = pad_number(number)
    down_color = (color[0] / 8, color[1] / 8, color[2] / 8)

    display(down_color, 0.5)
    for i in range(number):
        display(color, time_each / 2)
        display(down_color, time_each / 2)
    display(down_color, 0.5)

    rgb(False, False, False)


def display(color, length):
    red_level = color[0]
    green_level = color[1]
    blue_level = color[2]

    render_color(red_level, green_level, blue_level, length)


def render_weather(weather):
    print("rendering weather")
    render_alert(weather)
    render_temp(weather)
    render_wet(weather)
    render_wind(weather)
    display(off, 1)


def render_alert(weather):
    print("rendering alert")
    display(off, 1)
    alert = weather["alert"]
    if not alert:
        return

    display_count(red, 9)


def render_temp(weather):
    print("rendering temp")
    display(off, 1)
    temp = int(weather["temp"])
    negative = temp < 0
    temp = abs(temp)
    temp_string = str(temp)

    if temp == 0:
        display_count(yellow, 1)
        return

    for digit in range(len(temp_string)):
        value = int(temp_string[digit])
        if negative:
            display_count(miku, value)
        else:
            display_count(orange, value)


def render_wet(weather):
    print("rendering wet")
    display(off, 1)
    type_of_wet = weather["wet"]["type"]
    level = int(weather["wet"]["level"])

    if level <= 0 or type_of_wet == "none":
        display_count(yellow, 1)

    else:
        if type_of_wet == "rain":
            display_count(blue, level)
        elif type_of_wet == "snow":
            display_count(white, level)


def render_wind(weather):
    print("rendering wind")
    display(off, 1)
    wind_level = int(weather["wind"])
    if wind_level <= 0:
        return

    display_count(purple, wind_level)


def set_rgb(red_level, green_level, blue_level):
    print("setting to:", red_level, green_level, blue_level)


example_weather = {
    "alert": True,
    "temp": "-26",
    "wet": {
        "type": "snow",
        "level": "90"
    },
    "wind": "4"
}

example_weather2 = {
    "alert": False,
    "temp": "31",
    "wet": {
        "type": "rain",
        "level": "10"
    },
    "wind": "1"
}

example_weather3 = {
    "alert": False,
    "temp": "70",
    "wet": {
        "type": "none",
        "level": "0"
    },
    "wind": "0"
}

# render_weather(example_weather)
# render_weather(example_weather2)
# render_weather(example_weather3)

api = WeatherAPI()
weather = api.get_forecast()
print(weather)

render_weather(weather)
