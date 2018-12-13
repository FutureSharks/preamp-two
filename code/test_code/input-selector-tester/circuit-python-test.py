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


print('init')
set_reg(0, 0)

while True:
    time.sleep(1)
    # unmute
    print('unmute')
    set_reg(18, 0)
    time.sleep(1)
    # mute
    print('mute')
    set_reg(18, 147)
