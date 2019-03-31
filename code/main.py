import digitalio
import board
import busio
import time
from modules import MdacAttenuator, InputSelector, EncoderPanel, calculate_volume_ring, calculate_input_ring


volume_fade_in_done = False
debug_mode = True

cs_input_selector = digitalio.DigitalInOut(board.A4)
cs_mdac = digitalio.DigitalInOut(board.A5)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
attenuator = MdacAttenuator(spi, cs_mdac)
selector = InputSelector(spi, cs_input_selector)


volume_control = EncoderPanel(
    pixel_pin=board.D9,
    encoder_pin_a=board.D5,
    encoder_pin_b=board.D7,
    increment_before_change=1,
    change_object=attenuator,
)

input_control = EncoderPanel(
    pixel_pin=board.D12,
    encoder_pin_a=board.D10,
    encoder_pin_b=board.D11,
    increment_before_change=8,
    change_object=selector,
)


while True:
    # if not volume_fade_in_done:
    #     while True:
    #         if attenuator.level > 5000:
    #             volume_fade_in_done = True
    #             break
    #         attenuator.up()
    #         volume_control.write_ring(calculate_volume_ring(attenuator.level))

    volume_control.read_encoder()
    volume_control.update_led_ring(calculate_volume_ring(attenuator.level))

    input_control.read_encoder()
    input_control.update_led_ring(calculate_input_ring(selector.input_current))
