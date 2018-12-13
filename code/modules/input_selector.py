# -*- coding: utf-8 -*-

import digitalio
import time
from adafruit_bus_device import spi_device


class InputSelector(object):
    '''
    Manages an input selector via SPI
    '''

    def _init_mcp_register(self, reg_a, reg_b):
        '''
        Sets a both registers on the MCP23S17
        '''
        self._device.write(bytes(64))
        self._device.write(bytes(18))
        self._device.write(bytes([reg_a, reg_b]))

    def _init_mcp(self):
        '''
        Initialises the pin IO direction for both MCP23S17 banks
        '''
        self._device.write(bytes(64))
        self._device.write(bytes([0, 0]))
        self._device.write(bytes(64))
        self._device.write(bytes([1, 0]))
        print('input-selector init complete')

    def __init__(self, spi, cs, baudrate=8000000, input_current=1,
                mute_delay=1000, debug=False, inputs=6, loop=True):
        self.input_current = input_current
        self.inputs = inputs
        self.mute_delay = mute_delay
        self.mute_enabled = False
        self.debug = debug
        self._device = spidev.SPIDevice(spi, cs, baudrate=baudrate, polarity=0, phase=0)
        self._init_mcp()
        print('input-selector waiting for mute delay')
        time.sleep(self.mute_delay)
        self.toggle_mute()


    def toggle_mute(self):
        '''
        Toggles mute relay on/off
        '''
        if self.mute_enabled:
            self._device.write(bytes([128, 0]))
            self.mute_enabled = True
            print('input-selector mute enabled')
        else:
            self._device.write(bytes([0, 0]))
            self.mute_enabled = False
            print('input-selector mute disabled')

    def select_input(self, input):
        '''
        Selects a specific input
        '''
        if input > 6:
            if self.loop:
                pass
            else:
                pass
        elif input < 1:
            if self.loop:
                pass
            else:
                pass
        else:
            pass
            self.input_current = input

    def next_input(self, increment):
        '''
        Selects the next input
        '''
        self.select_input(input=self.input_current + increment)
