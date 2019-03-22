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
encoder1 = EncoderPanel(pixel_pin=board.D9, encoder_pin_a=board.D5, encoder_pin_b=board.D7)
encoder2 = EncoderPanel(pixel_pin=board.D12, encoder_pin_a=board.D10, encoder_pin_b=board.D11)

last_position_encoder1 = None
last_position_encoder2 = None

while True:
    # position_encoder1 = encoder1.encoder.position
    # if last_position_encoder1 is None or position_encoder1 != last_position_encoder1:
    #     print('Encoder 1 position: {0}'.format(position_encoder1))
    # last_position_encoder1 = position_encoder1

    position_encoder2 = encoder2.encoder.position
    if last_position_encoder2 is None or position_encoder2 != last_position_encoder2:
        print('Encoder 2 position: {0}'.format(position_encoder2))

    if last_position_encoder2 is not None:
        if position_encoder2 > last_position_encoder2:
            #selector.next_input()
            attenuator.increase_level()
        elif position_encoder2 < last_position_encoder2:
            #selector.next_input(increment=-1)
            attenuator.decrease_level()

    last_position_encoder2 = position_encoder2
