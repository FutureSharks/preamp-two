import digitalio
import board
import busio
import time
from mdac_attenuator import MdacAttenuator
from input_selector import InputSelector
from encoder_panel import EncoderPanel

cs_input_selector = digitalio.DigitalInOut(board.A4)
cs_mdac = digitalio.DigitalInOut(board.A5)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)

selector = InputSelector(spi, cs_input_selector)
attenuator = MdacAttenuator(spi, cs_mdac)


encoder1 = EncoderPanel(
    pixel_pin=board.D9,
    encoder_pin_a=board.D5,
    encoder_pin_b=board.D7
)

encoder2 = EncoderPanel(
    pixel_pin=board.D12,
    encoder_pin_a=board.D10,
    encoder_pin_b=board.D11
)

while True:
    encoder2.read_encoder()
