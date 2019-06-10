import digitalio
import board
import busio
import time
from modules import MdacAttenuator, InputSelector, VolumeControl, InputControl

volume_fade_in_done = False
debug_mode = True

ir_input = digitalio.DigitalInOut(board.A0)
cs_input_selector = digitalio.DigitalInOut(board.A4)
cs_mdac = digitalio.DigitalInOut(board.A5)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
attenuator = MdacAttenuator(spi, cs_mdac, steps=128)
selector = InputSelector(spi, cs_input_selector)


volume_control = VolumeControl(
    pixel_pin=board.D10,
    encoder_pin_a=board.D7,
    encoder_pin_b=board.D9,
    increment_before_change=1,
    change_object=attenuator,
)

input_control = InputControl(
    pixel_pin=board.D13,
    encoder_pin_a=board.D11,
    encoder_pin_b=board.D12,
    increment_before_change=26,
    change_object=selector,
)

while True:
    volume_control.read_encoder()
    input_control.read_encoder()
