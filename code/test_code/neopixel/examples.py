import board
import neopixel

pixel_pin = board.D10

ring = neopixel.NeoPixel(
    pin=pixel_pin,
    n=16,
    brightness=0.1,
    pixel_order=(1, 0, 2, 3)
)

RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0, 0)
GREEN = (0, 255, 0, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
PURPLE = (180, 0, 255, 0)
WHITE = (0, 0, 0, 255)

ring.fill(RED)
ring.fill(WHITE)
