# -*- coding: utf-8 -*-

import digitalio
import time
from adafruit_bus_device import spi_device


class MdacAttenuator(object):
    '''
    Manages an MDAC attenuator via SPI
    '''
    def __init__(self, spi, cs, baudrate=1000000, debug=True, steps=200, attenuation_slope=80):
        self.level = 0
        self.levels = []
        self.attenuation_slope = attenuation_slope
        self.steps = steps
        self.dac_value = None
        self.debug = debug
        self._device = spi_device.SPIDevice(spi, cs, baudrate=baudrate, polarity=0, phase=0)
        self._write_dac_value(0)
        self._calculate_levels()
        self._print('initialed with {0} levels'.format(len(self.levels)))

    def _print(self, message):
        '''
        Small function for printing information is debug option is enabled
        '''
        if not self.debug:
            return
        else:
            print('mdac-attenuator: {0}'.format(message))

    def _write_dac_value(self, value):
        '''
        Sets the MDAC value
        '''
        if value < 0 or value >= 65536:
            self._print('dac value must be between 0 and 65535. Given value {0}'.format(value))
            return
        with self._device as device:
            high_byte, low_byte = divmod(value, 256)
            device.write(bytearray([3]))
            device.write(bytearray([high_byte]))
            device.write(bytearray([low_byte]))
            self.dac_value = value
            self._print('DAC value set: {0}'.format(value))

    def _calculate_levels(self):
        '''
        Calculates a list of linear values for a logarithmic scale
        '''
        for i in range(self.steps):
            self.levels.append(round((10**-(i/self.attenuation_slope)) * 65536))

        self.levels[0] = 0
        self.levels[-1] = 65535
        self.level_max = len(self.levels) - 1
        self.levels = list(set(self.levels))
        self.levels.sort()

    def set_level(self, level):
        '''
        Sets an attenuation level
        '''
        if level > self.level_max or level < 0:
            self._print('level must be between 0 and {0}. Given level {1}'.format(self.level_max, level))
            return
        self._write_dac_value(self.levels[level])
        self.level = level
        self._print('level set {0}'.format(self.level))

    def up(self):
        self.set_level(self.level + 1)

    def down(self):
        self.set_level(self.level - 1)
