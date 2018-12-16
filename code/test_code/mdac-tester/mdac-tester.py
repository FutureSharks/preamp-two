# -*- coding: utf-8 -*-

import time
import board
import busio
import digitalio
from adafruit_bus_device.spi_device import SPIDevice

cs = digitalio.DigitalInOut(board.A4)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
mdac_device = SPIDevice(spi, cs, baudrate=1000000, polarity=0, phase=0)


def write_level(level):
    if level < 0 or level > 65536:
        return
    with mdac_device as device:
        high_byte, low_byte = divmod(level, 256)
        device.write(bytearray([3]))
        device.write(bytearray([high_byte]))
        device.write(bytearray([low_byte]))
        print('mdac-attenuator level {0}'.format(level))

time_delay = 1

while True:
    write_level(10000)
    time.sleep(time_delay)
    write_level(20000)
    time.sleep(time_delay)
    write_level(30000)
    time.sleep(time_delay)
    write_level(40000)
    time.sleep(time_delay)
    write_level(50000)
    time.sleep(time_delay)
    write_level(60000)
    time.sleep(time_delay)
