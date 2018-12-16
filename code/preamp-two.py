import digitalio
import board
import input_selector
import mdac_attenuator
import busio
import time


cs_input_selector = digitalio.DigitalInOut(board.A5)
cs_mdac = digitalio.DigitalInOut(board.A4)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)

selector = input_selector.InputSelector(spi, cs_input_selector)
attenuator = mdac_attenuator.MdacAttenuator(spi, cs_mdac)

while True:
    selector.select_input(1)
    attenuator._write_level(65536)
    time.sleep(99999)
