import RPi.GPIO as gpio
import spidev
import time
import uinput

key_map = {
    "left": {"pin": 11, "uinput":uinput.KEY_LEFT},
    "right": {"pin": 13, "uinput":uinput.KEY_RIGHT},
    "up": {"pin": 15, "uinput":uinput.KEY_UP},
    "down": {"pin": 16, "uinput":uinput.KEY_DOWN},
    "A": {"pin": 18, "uinput":uinput.KEY_Z},
    "B": {"pin": 22, "uinput":uinput.KEY_X},
    "select": {"pin": 29, "uinput":uinput.KEY_P},
    "start": {"pin": 32, "uinput":uinput.KEY_ENTER}
}

device = uinput.Device([
    uinput.KEY_LEFT,
    uinput.KEY_RIGHT,
    uinput.KEY_UP,
    uinput.KEY_DOWN,
    uinput.KEY_X,
    uinput.KEY_Z,
    uinput.KEY_ENTER,
    uinput.KEY_P])

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

spi_clock = 19
spi_mosi = 21
spi_miso = 23
spi_tft_chip_select = 24
spi_data_command_select = 26

tft_reset = 33

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

gpio.setup(spi_clock, gpio.OUT)
gpio.setup(spi_mosi, gpio.OUT)
gpio.setup(spi_miso, gpio.OUT)
gpio.setup(spi_tft_chip_select, gpio.OUT)
gpio.setup(spi_data_command_select, gpio.OUT)

gpio.setup(tft_reset, gpio.OUT)

gpio.output(spi_clock, False)
gpio.output(spi_mosi, False)
gpio.output(spi_miso, False)
gpio.output(spi_tft_chip_select, False)
gpio.output(spi_data_command_select, False)

gpio.output(tft_reset, False)


#spi = spidev.SpiDev()
#spi.open(0, 0)
#spi.max_speed_hz = 24000000
#spi.xfer([value_8bit])

# Split an integer input into a two byte array to send via SPI
#def write_pot(input):
#    msb = 0x00
#    lsb = input
#    spi.xfer([msb, lsb])
 
# Repeatedly switch a MCP4151 digital pot off then on
#while True:
#    write_pot(0x1FF)
#    time.sleep(0.5)
#    write_pot(0x00)
#    time.sleep(0.5)

while True:
    time.sleep(1/120)
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
        #if state[button] != last_state[button]:
        if state[button]:
            #print("pressed " + button)
            device.emit_click(key_map[button]["uinput"])
            #else:
                #print("released " + button)

    last_state = state
