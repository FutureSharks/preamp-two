# -*- coding: utf-8 -*-

import digitalio
import time
from adafruit_bus_device import spi_device


class MdacAttenuator(object):
    '''
    Manages an MDAC attenuator via SPI
    '''
    def __init__(self, spi, cs, baudrate=1000000, debug=False, steps=128, attenuation_slope=40):
        self.level = 0
        self.levels = []
        self.attenuation_slope = attenuation_slope
        self.steps = steps
        self.dac_value = None
        self.debug = debug
        self._device = spi_device.SPIDevice(spi, cs, baudrate=baudrate, polarity=0, phase=0)
        print('mdac-attenuator initialising with level {0}'.format(self.level))
        self._write_dac_value(0)
        self._calculate_levels()

    def _write_dac_value(self, value):
        '''
        Sets the MDAC value
        '''
        if value < 0 or value > 65536:
            print('mdac-attenuator dac value must be between 0 and 65536')
            return
        with self._device as device:
            high_byte, low_byte = divmod(value, 256)
            device.write(bytearray([3]))
            device.write(bytearray([high_byte]))
            device.write(bytearray([low_byte]))
            self.dac_value = value
            print('mdac-attenuator value {0}'.format(value))

    def _calculate_levels(self):
        '''
        Calculates a list of linear values for a logarithmic scale
        '''
        for i in range(self.steps):
            self.levels.append(round((10**-(i/self.attenuation_slope)) * 65536))

        # Make levels[0] == 0
        # Make levels[-1] == 65536

        self.levels.reverse()
        self.levels = list(set(self.levels))

    def set_level(self, level):
        '''
        Sets an attenuation level
        '''
        if level > len(self.levels) or level < 0:
            print('mdac-attenuator level must be between 0 and {0}'.format(len(self.levels) + 1))
            return
        self._write_dac_value(self.levels[level])
        self.level = level

    def up(self):
        self.set_level(self.level + 1)

    def down(self):
        self.set_level(self.level - 1)
