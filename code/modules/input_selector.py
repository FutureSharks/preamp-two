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

    def _disable_all_relays(self, with_delay=True):
        '''
        Turns off all relays with optional delay
        '''
        if with_delay:
            time.sleep(0.01)
        self._set_gpio(64, 0)

    def _set_all_relays_to_off(self):
        '''
        Switches all relays to off position where no input is selected
        '''
        if self.mute_enabled:
            self._set_gpio(42, 84)
        else:
            self._set_gpio(106, 84)

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
            self._set_gpio(106, 82)
            self._disable_all_relays()
        elif input == 2:
            self._set_gpio(106, 76)
            self._disable_all_relays()
        elif input == 3:
            self._set_gpio(106, 52)
            self._disable_all_relays()
        elif input == 4:
            self._set_gpio(105, 84)
            self._disable_all_relays()
        elif input == 5:
            self._set_gpio(102, 84)
            self._disable_all_relays()
        elif input == 6:
            self._set_gpio(90, 84)
            self._disable_all_relays()

        print('input-selector input {0} selected'.format(input))
        self.input_current = input

    def next_input(self, increment=1):
        '''
        Selects the next input
        '''
        self.select_input(input=self.input_current + increment)

    def up(self):
        self.next_input(1)

    def down(self):
        self.next_input(-1)
