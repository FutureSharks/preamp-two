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
    set_gio(128, 0)

print('init')
set_reg(0, 0)
set_reg(1, 0)

time_delay = 1

while True:
    print('Switching relay 1')
    set_gio(213, 72)
    time.sleep(0.01)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 2')
    set_gio(213, 48)
    time.sleep(0.01)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 3')
    set_gio(212, 208)
    time.sleep(0.01)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 4')
    set_gio(211, 80)
    time.sleep(0.01)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 5')
    set_gio(205, 80)
    time.sleep(0.01)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay 6')
    set_gio(181, 80)
    time.sleep(0.01)
    reset_relays()
    time.sleep(time_delay)
    print('Switching relay mute on')
    set_gio(0, 0)
    time.sleep(time_delay)
    print('Switching relay mute off')
    reset_relays()
    time.sleep(time_delay)
