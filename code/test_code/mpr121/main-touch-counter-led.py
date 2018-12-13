import gc
import adafruit_dotstar
import time
import adafruit_mpr121
import busio
import board

gc.collect()   # make some rooooom

dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

led_red = 0
led_green = 0
led_blue = 0

######################### HELPERS ##############################

def led_up(led_value, increment=1):
    if led_value < (255 - increment):
        led_value += increment
    return led_value


def led_down(led_value, increment=1):
    if led_value > increment:
        led_value -= increment
    return led_value

######################### MAIN LOOP ##############################

last_touched = 0
increment = 32

while True:
    for i in range(8):
        if mpr121.is_touched(i):
            if i > last_touched:
                led_red = led_up(led_red, increment)
                dot[0] = [led_red, 0, 0]
            if i < last_touched:
                led_red = led_down(led_red, increment)
                dot[0] = [led_red, 0, 0]

            last_touched = i
