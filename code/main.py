import digitalio
import board
import busio
import time
from modules import MdacAttenuator, InputSelector, EncoderPanel, calculate_volume_ring, calculate_input_ring


volume_fade_in_done = False
debug_mode = True

ir_input = digitalio.DigitalInOut(board.A0)
cs_input_selector = digitalio.DigitalInOut(board.A4)
cs_mdac = digitalio.DigitalInOut(board.A5)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
attenuator = MdacAttenuator(spi, cs_mdac, steps=128)
selector = InputSelector(spi, cs_input_selector)


volume_control = EncoderPanel(
    pixel_pin=board.D10,
    encoder_pin_a=board.D7,
    encoder_pin_b=board.D9,
    increment_before_change=1,
    change_object=attenuator,
)

input_control = EncoderPanel(
    pixel_pin=board.D13,
    encoder_pin_a=board.D11,
    encoder_pin_b=board.D12,
    increment_before_change=8,
    change_object=selector,
)

l = 0

while True:
    # if not volume_fade_in_done:
    #     while True:
    #         if attenuator.level > 5000:
    #             volume_fade_in_done = True
    #             break
    #         attenuator.up()
    #         volume_control.write_ring(calculate_volume_ring(attenuator.level))

    volume_control.read_encoder()

    if l != attenuator.level:
        volume_control.update_led_ring(calculate_volume_ring(attenuator.level))

    l = attenuator.level
    #
    # input_control.read_encoder()
    # input_control.update_led_ring(calculate_input_ring(selector.input_current))
