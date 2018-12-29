# -*- coding: utf-8 -*-

import digitalio
import time
from adafruit_bus_device import spi_device


class MdacAttenuator(object):
    '''
    Manages an MDAC attenuator via SPI
    '''
    def __init__(self, spi, cs, baudrate=1000000, debug=False, level=0, db_level=0):
        self.level = level
        self.db_level = db_level
        self.debug = debug
        self._device = spi_device.SPIDevice(spi, cs, baudrate=baudrate, polarity=0, phase=0)

        print('mdac-attenuator starting init')

    def _write_level(self, level):
        '''
        Sets the MDAC volume to a specific linear level
        '''
        if level < 0 or level >= 65536:
            return
        with self._device as device:
            high_byte, low_byte = divmod(level, 256)
            device.write(bytearray([3]))
            device.write(bytearray([high_byte]))
            device.write(bytearray([low_byte]))
            self.level = level
            print('mdac-attenuator level {0}'.format(level))

    def set_db_level(self, db_level):
        '''
        Sets the MDAC volume to a specific Db level
        '''
        pass