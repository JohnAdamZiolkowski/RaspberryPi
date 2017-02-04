import time

example_weather = dict()
example_weather["temp"] = "-26"

example_weather["wet"] = dict()
example_weather["wet"]["type"] = "rain"
example_weather["wet"]["chance"] = "0"

example_weather["wind"] = "4"

example_weather["alert"] = True


def render_weather(weather):
    print("rendering weather")
    render_temp(weather)
    render_wet(weather)
    render_wind(weather)
    render_alert(weather)


def render_temp(weather):
    print("rendering temp")
    pass


def render_wet(weather):
    print("rendering wet")
    pass


def render_wind(weather):
    print("rendering wind")
    wind_level = int(weather["wind"])
    if wind_level <= 0:
        return

    for i in range(wind_level):
        set_rgb(128, 128, 128)
        time.sleep(1)


def render_alert(weather):
    print("rendering alert")
    alert = weather["alert"]
    if not alert:
        return

    set_rgb(255, 0, 0)
    time.sleep(1)


def set_rgb(red_level, green_level, blue_level):
    print("setting to:", red_level, green_level, blue_level)


render_weather(example_weather)