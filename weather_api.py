import pyowm
owm = pyowm.OWM('95edbf7c5c5f60fafcc08d79cc9ee124')
forecaster = owm.daily_forecast('Toronto,ON')
forecast = forecaster.get_forecast()

wind_levels = [2, 5, 11, 19, 29, 39, 50, 61, 74, 87]
rain_levels = [0, 2, 5, 10, 15, 20, 35, 50, 65, 75]
snow_levels = [0, 5, 10, 20, 30, 50, 75, 100, 150, 200]


def rank(amount, levels):
    level = 0
    for l in range(len(levels)):
        if amount < levels[l] / 8:
            level = l
            break
    return level

for weather in forecast.get_weathers():
    # print("weather:")
    print("date:", weather.get_reference_time('iso'))

    temp_for_day = weather.get_temperature(unit='celsius')
    temp = int((temp_for_day["min"] + temp_for_day["max"]) / 2)

    rain = weather.get_rain()
    snow = weather.get_snow()

    if rain:
        wet = {
            "type": "rain",
            "level": rank(rain["all"], rain_levels),
            "mm": rain["all"]
        }
    elif snow:
        wet = {
            "type": "snow",
            "level": rank(snow["all"], snow_levels),
            "mm": snow["all"]
        }
    else:
        wet = {
            "type": "none",
            "level": 0
        }

    wind_for_day = weather.get_wind()
    speed = wind_for_day["speed"]
    wind = rank(speed, wind_levels)

    # print("  temp:", temp)
    # print("   wet:", wet)
    # print("  wind:", wind)

    report = {
        "temp": temp,
        "wet": wet,
        "wind": wind
    }

    print(report)

    # print()

