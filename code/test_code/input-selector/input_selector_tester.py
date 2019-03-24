import time
import board
import busio
import digitalio
from adafruit_bus_device.spi_device import SPIDevice

cs = digitalio.DigitalInOut(board.A4)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
device = SPIDevice(spi, cs, baudrate=1000000, polarity=0, phase=0)


def set_reg(register, value):
    with device as d:
        d.write(bytearray([64]))
        d.write(bytearray([register]))
        d.write(bytearray([value]))


def set_gpio(gio_a, gio_b):
    with device as d:
        d.write(bytearray([64]))
        d.write(bytearray([18]))
        d.write(bytearray([gio_a]))
        d.write(bytearray([gio_b]))


def reset_relays():
    time.sleep(0.04)
    set_gpio(64, 0)

print('init')
set_reg(0, 0)
set_reg(1, 0)

time_delay = 1

# | gpioa |  | gpiob |
# 0000 0000  0000 0000
#
# last bit of each gpio bank is NC
# -000 0000  -000 0000
#
# All relays off
# 0010 1010 0101 0100
#
# All relays off with mute disabled
# 0110 1010 0101 0100
#
# mute
# 0*00 0000 0000 0000
#
# extra IO
# 0000 0000 0000 000*
#
# input1
# 0000 0000 0000 0**0
# 0110 1010 0101 0010
#
# input2
# 0000 0000 000* *000
# 0110 1010 0100 1100
#
# input3
# 0000 0000 0**0 0000
# 0110 1010 0011 0100
#
# input4
# 0000 00** 0000 0000
# 0110 1001 0101 0100
#
# input5
# 0000 **00 0000 0000
# 0110 0110 0101 0100
#
# input6
# 00** 0000 0000 0000
# 0101 1010 0101 0100

while True:
    print('Switching mute on')
    set_gpio(0, 0)
    time.sleep(time_delay)
    print('Switching mute off')
    set_gpio(64, 0)
    time.sleep(time_delay)

    print('Switching relay 1 on')
    set_gpio(64, 2)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 1 off')
    set_gpio(64, 4)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 2 on')
    set_gpio(64, 8)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 2 off')
    set_gpio(64, 16)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 3 on')
    set_gpio(64, 32)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 3 off')
    set_gpio(64, 64)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 4 on')
    set_gpio(65, 0)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 4 off')
    set_gpio(66, 0)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 5 on')
    set_gpio(68, 0)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 5 off')
    set_gpio(72, 0)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 6 on')
    set_gpio(80, 0)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 6 off')
    set_gpio(96, 0)
    reset_relays()
    time.sleep(time_delay)
