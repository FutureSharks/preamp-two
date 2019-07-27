import digitalio
import board
import busio
import time
from modules import MdacAttenuator, InputSelector, VolumeControl, InputControl

rings_faded = False
rings_fade_timeout = 3
debug_mode = True

ir_input = digitalio.DigitalInOut(board.A0)
cs_input_selector = digitalio.DigitalInOut(board.A4)
cs_mdac = digitalio.DigitalInOut(board.A5)
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
attenuator = MdacAttenuator(spi, cs_mdac, steps=128)
selector = InputSelector(spi, cs_input_selector)


volume_control = VolumeControl(
    pixel_pin=board.D13,
    encoder_pin_a=board.D11,
    encoder_pin_b=board.D12,
    change_object=attenuator,
)

input_control = InputControl(
    pixel_pin=board.D10,
    encoder_pin_a=board.D7,
    encoder_pin_b=board.D9,
    change_object=selector,
)



while True:
    volume_control.read_encoder()
    input_control.read_encoder()

    now = time.time()

    if (now - volume_control.last_change_time) > rings_fade_timeout and (now - input_control.last_change_time) > rings_fade_timeout:
        if not rings_faded:
            volume_control.fade_ring()
            input_control.fade_ring()
            rings_faded = True
    else:
        if rings_faded:
            volume_control.unfade_ring()
            input_control.unfade_ring()
        rings_faded = False
