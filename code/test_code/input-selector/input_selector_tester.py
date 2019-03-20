import time
import board
import busio
import digitalio
from adafruit_bus_device.spi_device import SPIDevice

cs = digitalio.DigitalInOut(board.A5)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
device = SPIDevice(spi, cs, baudrate=1000000, polarity=0, phase=0)


def set_reg(register, value):
    with device as d:
        d.write(bytearray([64]))
        d.write(bytearray([register]))
        d.write(bytearray([value]))


def set_gio(gio_a, gio_b):
    with device as d:
        d.write(bytearray([64]))
        d.write(bytearray([18]))
        d.write(bytearray([gio_a]))
        d.write(bytearray([gio_b]))


def reset_relays():
    time.sleep(0.040)
    set_gio(64, 0)

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
# mute
# 0*00 0000  0000 0000
#
# extra IO
# 0000 0000  0000 000*
#
# input1
# 0000 0000  0000 0**0
#
# input2
# 0000 0000  000* *000
#
# input3
# 0000 0000  0**0 0000
#
# input4
# 0000 00**  0000 0000
#
# input5
# 0000 **00  0000 0000
#
# input6
# 00** 0000  0000 0000

while True:
    print('Switching mute on')
    set_gio(0, 0)
    time.sleep(time_delay)
    print('Switching mute off')
    set_gio(64, 0)
    time.sleep(time_delay)

    print('Switching relay 1')
    set_gio(0, 2)
    reset_relays()
    time.sleep(time_delay)
    set_gio(0, 4)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 2')
    set_gio(64, 8)
    reset_relays()
    time.sleep(time_delay)
    set_gio(64, 16)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 3')
    set_gio(64, 32)
    reset_relays()
    time.sleep(time_delay)
    set_gio(64, 64)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 4')
    set_gio(65, 0)
    reset_relays()
    time.sleep(time_delay)
    set_gio(66, 0)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 5')
    set_gio(68, 0)
    reset_relays()
    time.sleep(time_delay)
    set_gio(72, 0)
    reset_relays()
    time.sleep(time_delay)

    print('Switching relay 6')
    set_gio(80, 0)
    reset_relays()
    time.sleep(time_delay)
    set_gio(96, 0)
    reset_relays()
    time.sleep(time_delay)
