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


######################### HELPERS ##############################

######################### MAIN LOOP ##############################

while True:
    # Loop through all 12 inputs (0-11).
    for i in range(12):
        # Call is_touched and pass it then number of the input.  If it's touched
        # it will return True, otherwise it will return False.
        if mpr121.is_touched(i):
            print('Input {} touched!'.format(i))
    time.sleep(0.1)
