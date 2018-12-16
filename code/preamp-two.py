import digitalio
import board
import input_selector
import busio

cs = digitalio.DigitalInOut(board.A5)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)

selector = input_selector.InputSelector(spi, cs)

selector.next_input()
selector.toggle_mute()
