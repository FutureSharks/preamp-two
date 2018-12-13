# Write your code here :-)
import time
 
# Import MPR121 module.
import adafruit_mpr121
 
import busio
 
# Create I2C bus.
import board
i2c = busio.I2C(board.SCL, board.SDA)
 
# Create MPR121 class.
mpr121 = adafruit_mpr121.MPR121(i2c)
 
# Loop forever testing each input and printing when they're touched.
while True:
    # Loop through all 12 inputs (0-11).
    for i in range(12):
        # it will return True, otherwise it will return False.
        if mpr121.is_touched(i):
            print('Input {} touched!'.format(i))
    time.sleep(0.25)
    