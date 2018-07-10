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

device_keys = []
for button in key_map:
    device_keys.append(key_map[button]["uinput"])
device = uinput.Device(device_keys)

#spi_clock = 19
#spi_mosi = 21
#spi_miso = 23
#spi_tft_chip_select = 24
#spi_data_command_select = 26

#tft_reset = 33

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
for button in key_map:
    gpio.setup(key_map[button]["pin"], gpio.IN, pull_up_down=gpio.PUD_DOWN)

#gpio.setup(spi_clock, gpio.OUT)
#gpio.setup(spi_mosi, gpio.OUT)
#gpio.setup(spi_miso, gpio.OUT)
#gpio.setup(spi_tft_chip_select, gpio.OUT)
#gpio.setup(spi_data_command_select, gpio.OUT)

#gpio.setup(tft_reset, gpio.OUT)

#gpio.output(spi_clock, False)
#gpio.output(spi_mosi, False)
#gpio.output(spi_miso, False)
#gpio.output(spi_tft_chip_select, False)
#gpio.output(spi_data_command_select, False)

#gpio.output(tft_reset, False)


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
    for button in key_map:
        if gpio.input(key_map[button]["pin"]):
            device.emit_click(key_map[button]["uinput"])
