import gc
import adafruit_dotstar
import time
import at42qt2120
import busio
import board
from digitalio import DigitalInOut, Direction

gc.collect()

dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)
i2c = busio.I2C(board.SCL, board.SDA)

at42_change_pin = DigitalInOut(board.D7)
at42_change_pin.direction = Direction.INPUT

at42 = at42qt2120.AT42QT2120(i2c, at42_change_pin)

time.sleep(0.1)

firmware_version = at42.get_firmware_version()

print('AT42QT2120 with firmware version {0}'.format(firmware_version))


# Enable slider mode on channels 0-2
at42.enable_slider()

while True:
    slider = at42.get_slider_wheel_position()
    # Poll all keys for status
    if at42.get_key_status()[3]:
        dot[0] = [0, 255, slider]
    else:
        dot[0] = [0, 0, slider]
