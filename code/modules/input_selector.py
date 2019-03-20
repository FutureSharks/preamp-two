# -*- coding: utf-8 -*-

import digitalio
import time
from adafruit_bus_device import spi_device


class InputSelector(object):
    '''
    Manages an input selector via SPI
    '''
    def __init__(self, spi, cs, baudrate=1000000, input_current=1,
                mute_delay=1, debug=False, inputs=6, loop=True):
        self.input_current = input_current
        self.inputs = inputs
        self.input_loop = loop
        self.mute_delay = mute_delay
        self.mute_enabled = True
        self.debug = debug
        self._device = spi_device.SPIDevice(spi, cs, baudrate=baudrate, polarity=0, phase=0)

        print('input-selector starting init')
        self._set_register(0, 0)
        self._set_register(1, 0)
        print('input-selector waiting for mute delay')
        time.sleep(self.mute_delay)
        self.toggle_mute()

    def _set_register(self, register, value):
        '''
        Sets a both registers on the MCP23S17
        '''
        with self._device as device:
            device.write(bytearray([64]))
            device.write(bytearray([register]))
            device.write(bytearray([value]))

    def _set_gpio(self, gio_a, gio_b):
        '''
        Sets a both registers on the MCP23S17
        '''
        with self._device as device:
            device.write(bytearray([64]))
            device.write(bytearray([18]))
            device.write(bytearray([gio_a]))
            device.write(bytearray([gio_b]))

    def toggle_mute(self):
        '''
        Toggles mute relay on/off
        '''
        if self.mute_enabled:
            self._set_gpio(64, 0)
            self.mute_enabled = False
            print('input-selector mute disabled')
        else:
            self._set_gpio(0, 0)
            self.mute_enabled = True
            print('input-selector mute enabled')

    def select_input(self, input):
        '''
        Selects a specific input
        '''
        if input > self.inputs:
            if self.input_loop:
                input = 1
            else:
                return
        elif input < 1:
            if self.input_loop:
                input = self.inputs
            else:
                return

        if input == 1:
            self._set_gio(0, 2)
            time.sleep(0.01)
            self._set_gio(0, 4)
        elif input == 2:
            self._set_gio(0, 8)
            time.sleep(0.01)
            self._set_gio(0, 16)
        elif input == 3:
            self._set_gio(0, 32)
            time.sleep(0.01)
            self._set_gio(0, 64)
        elif input == 4:
            self._set_gio(1, 0)
            time.sleep(0.01)
            self._set_gio(2, 0)
        elif input == 5:
            self._set_gio(4, 0)
            time.sleep(0.01)
            self._set_gio(8, 0)
        elif input == 6:
            self._set_gio(16, 0)
            time.sleep(0.01)
            self._set_gio(32, 0)

        print('input-selector input {0} selected'.format(input))
        self.input_current = input

    def next_input(self, increment=1):
        '''
        Selects the next input
        '''
        self.select_input(input=self.input_current + increment)
