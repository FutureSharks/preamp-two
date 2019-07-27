# -*- coding: utf-8 -*-

import time
from .encoder_panel import EncoderPanel


class InputControl(EncoderPanel):
    '''
    Input control module
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b, selector, debug=True):
        super(InputControl, self).__init__(pixel_pin, encoder_pin_a, encoder_pin_b)
        self.selector = selector
        self.increment_before_change = 26
        self.encoder_last_position = 0
        self.encoder_last_change = 0
        self.encoder_position = 0
        self.colour_background = [0, 3, 3, 0]
        self.colour_input_pixel = 0
        self.last_change_time = time.time()
        self.debug = debug
        self.set_ring_by_input()

    def _print(self, message):
        '''
        Small function for printing information is debug option is enabled
        '''
        if not self.debug:
            return
        else:
            print('input-control: {0}'.format(message))

    def fade_ring(self):
        '''
        Fades ring to a low brightness
        '''
        self._print('fading')
        self.ring.fill(self.colour_background)
        return

    def unfade_ring(self):
        '''
        Fades ring to a low brightness
        '''
        self._print('unfading')
        self.fill_pixel_ring(self.calculate_input_ring(self.selector.input_current))
        return

    def set_ring_by_input(self):
        '''
        Returns the RGBW values for the ring of 16 NeoPixels on the input selector
        '''
        self.fill_pixel_ring(self.colour_background)
        pixel_value = self.colour_background.copy()
        pixel_value[self.colour_input_pixel] = 32

        if self.selector.input_current == 1:
            pxl_range = range(0, 3)
        if self.selector.input_current == 2:
            pxl_range = range(2, 5)
        if self.selector.input_current == 3:
            pxl_range = range(4, 7)
        if self.selector.input_current == 4:
            pxl_range = range(6, 9)
        if self.selector.input_current == 5:
            pxl_range = range(8, 11)
        if self.selector.input_current == 6:
            pxl_range = range(10, 13)

        for pxl in pxl_range:
            self.write_single_pixel(pxl, pixel_value)
            print(pxl, pixel_value)

    def read_encoder(self):
        '''
        Reads the position of the encoder
        '''
        self.encoder_position = self.encoder.position

        if self.encoder_position == self.encoder_last_position:
            return

        if self.encoder_position > (self.encoder_last_change + self.increment_before_change):
            self.selector.up()
            self.set_ring_by_input()
            self.encoder_last_change = self.encoder_position
        elif self.encoder_position < (self.encoder_last_change - self.increment_before_change):
            self.selector.down()
            self.set_ring_by_input()
            self.encoder_last_change = self.encoder_position

        self.encoder_last_position = self.encoder_position
        self.last_change_time = time.time()
