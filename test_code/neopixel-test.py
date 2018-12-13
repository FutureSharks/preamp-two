import machine
import neopixel
import time

# This configures a NeoPixel strip on GPIO4 with 1 pixels
np = neopixel.NeoPixel(machine.Pin(4), 25, bpp=4)


for pixel in range(0, np.n):
    for value in range(0, 64):
        np[pixel] = (value, 0, 0, 0)
        np.write()
    for value in range(0, 64):
        np[pixel] = (0, value, 0, 0)
        np.write()
    np[pixel] = (0, 0, 0, 0)
