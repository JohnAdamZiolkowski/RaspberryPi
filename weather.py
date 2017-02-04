import time

example_weather = dict()
example_weather["temp"] = "-26"

example_weather["wet"] = dict()
example_weather["wet"]["type"] = "rain"
example_weather["wet"]["chance"] = "90"

example_weather["wind"] = "4"

example_weather["alert"] = True

red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
miku = (0, 255, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)

white = (255, 0, 0)
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

    set_rgb(red_level, green_level, blue_level)
    time.sleep(time_each)

    set_rgb(0, 0, 0)
    time.sleep(time_each)


def render_weather(weather):
    print("rendering weather")
    render_temp(weather)
    render_wet(weather)
    render_wind(weather)
    render_alert(weather)


def render_temp(weather):
    print("rendering temp")
    temp = int(weather["temp"])
    negative = temp < 0
    temp = abs(temp)
    temp_string = str(temp)

    if temp == 0:
        set_rgb(255, 0, 255)
        time.sleep(1)
        return

    for digit in range(len(temp_string)):
        value = int(temp_string[digit])
        for i in range(value):
            if negative:
                display(miku, value)
            else:
                display(orange, value)


def render_wet(weather):
    print("rendering wet")
    type_of_wet = weather["wet"]["type"]
    chance = int(weather["wet"]["chance"]) / 10

    if chance <= 0:
        set_rgb(255, 255, 0)
        time.sleep(1)

    else:
        for i in range(chance):
            if type_of_wet == "rain":
                display(blue, chance)
                time.sleep(pad_number(chance))
            elif type_of_wet == "snow":
                display(white, chance)


def render_wind(weather):
    print("rendering wind")
    wind_level = int(weather["wind"])
    if wind_level <= 0:
        return

    for i in range(wind_level):
        display(half_white, wind_level)


def render_alert(weather):
    print("rendering alert")
    alert = weather["alert"]
    if not alert:
        return

    for i in range(10):
        display(red, 10)


def set_rgb(red_level, green_level, blue_level):
    print("setting to:", red_level, green_level, blue_level)


render_weather(example_weather)
