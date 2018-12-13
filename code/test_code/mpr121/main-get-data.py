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

time.sleep(2)
for i in range(12):
    print(mpr121.baseline_data(i))
time.sleep(2)

while True:
    print(
        [
        mpr121.filtered_data(7),
        mpr121.filtered_data(8),
        mpr121.filtered_data(9),
        mpr121.filtered_data(10),
        mpr121.filtered_data(11)
        ]
        )
    time.sleep(0.1)
