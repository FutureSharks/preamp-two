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


def set_neopixels(light_levels):
    def _get_pixel_number(row, column):
        if row == 1:
            pixel = 20 + 5 - column
        elif row == 2:
            pixel = 15 + column
        elif row == 3:
            pixel = 10 + 5 - column
        elif row == 4:
            pixel = 5 + column
        elif row == 5:
            pixel = column
        else:
            print('error')
        return pixel - 1
    for row in light_levels.keys():
        # Takes 2-4ms per row column
        for column in light_levels[row]:
            pixel = _get_pixel_number(int(row), int(column))
            level = 255 - (light_levels[row][column] * 8)
            if level >= 256:
                level = 255
            elif level < 0:
                level = 0
            np[pixel] = (0, 0, level, 14)
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

while True:
    light_levels = {}
    for row in range(1, 6):
        light_levels[str(row)] = {}
        for column in range(1, 6):
            # This takes 5-7ms
            setMCP23S08(9, calculate_MCP23S08_value(row=row, column=column))
            light_level = light.read()
            light_levels[str(row)][str(column)] = light_level
    # This takes 45-50ms
    set_neopixels(light_levels)
