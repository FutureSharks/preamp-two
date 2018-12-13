from machine import SPI, Pin, ADC
import time
import machine
import neopixel

import utime

# This configures a NeoPixel strip on GPIO4 with 1 pixels
np = neopixel.NeoPixel(machine.Pin(4), 25, bpp=4)

# NodeMCU hardware SPI pins
# SCK is GPIO14 / D5
# MOSI is GPIO13 / D7
# CS is set to GPIO02 / D4
spi = SPI(1, baudrate=5000000, polarity=0, phase=0)
cs = Pin(2, Pin.OUT)
cs.on()

# light reader pin ADC00 / A0
light = ADC(0)


def setMCP23S08(select_register, register_value):
    '''
    http://ww1.microchip.com/downloads/en/DeviceDoc/21919e.pdf

    register 0 = IODIR
    register 9 = GPIO
    '''
    cs.off()
    # Send device opcode
    spi.write(bytearray([64]))
    # Select the register to write to
    spi.write(bytearray([select_register]))
    # Write the register value
    spi.write(bytearray([register_value]))
    cs.on()


def set_all_neopixels(rgbw):
    for pixel in range(0, np.n):
        np[pixel] = rgbw
        np.write()

pixel_numbers = [
    [24, 23, 22, 21, 20],
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

def set_neopixels(rows):
    for row in range(0, 5):
        for column in range(0, 5):
            level = 255 - (rows[row][column] * 8)
            if level >= 256:
                level = 255
            elif level < 0:
                level = 0
            pixel = pixel_numbers[row][column]
            np[pixel] = (0, 0, level, 10)
    np.write()


def calculate_MCP23S08_value(row, column):
    '''
    Calculates the value to send to the MCP23S08 GPIO in order to select a column and row photodiode to read
    '''
    if row == 1:
        value_4051 = '001'
    elif row == 2:
        value_4051 = '010'
    elif row == 3:
        value_4051 = '100'
    elif row == 4:
        value_4051 = '000'
    elif row == 5:
        value_4051 = '110'
    if column == 1:
        value_MCP = '01111'
    elif column == 2:
        value_MCP = '10111'
    elif column == 3:
        value_MCP = '11011'
    elif column == 4:
        value_MCP = '11101'
    elif column == 5:
        value_MCP = '11110'
    return int('{0}{1}'.format(value_MCP, ''.join(reversed(value_4051))), 2)


# Set all pins to outputs
setMCP23S08(0, 0)

set_all_neopixels((4, 0, 0, 0))

def run():
    while True:
        rows = []
        for row in range(1, 6):
            columns = []
            for column in range(1, 6):
                # This takes 5-7ms
                setMCP23S08(9, calculate_MCP23S08_value(row=row, column=column))
                light_level = light.read()
                columns.append(light_level)
            rows.append(columns)
        # This takes 45-50ms
        set_neopixels(rows)
