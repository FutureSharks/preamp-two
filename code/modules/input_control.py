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
        self.colour_background = [0, 0, 0, 0]
        self.colour_input_pixel = 0
        self.last_change_time = time.time()
        self.debug = debug
        self.counter = 0
        self.update_ring_colour()

    def _print(self, message):
        '''
        Small function for printing information is debug option is enabled
        '''
        if not self.debug:
            return
        else:
            print('input-control: {0}'.format(message))

    def update_ring_colour(self):
        '''
        Updates the ring colour based on the current encoder position counter
        '''
        if self.counter < 0:
            self.counter = 127
        if self.counter > 127:
            self.counter = 0

        pos = self.counter

        if pos < 0 or pos > 127:
            r = g = b = 0
        elif pos < 43:
            r = int(pos * 3)
            g = int(127 - pos*3)
            b = 0
        elif pos < 85:
            pos -= 43
            r = int(127 - pos*3)
            g = 0
            b = int(pos*3)
        else:
            pos -= 85
            r = 0
            g = int(pos*3)
            b = int(127 - pos*3)

        input = int(self.counter/25) + 1
        if self.selector.input_current != input:
            self.selector.select_input(input)
            self.flash_ring()
            print(self.counter)

        self.fill_pixel_ring((int(r/8), int(g/8), int(b/8), 0))

    def flash_ring(self):
        '''
        Fades ring to a low brightness
        '''
        self.ring.fill([8, 0, 0, 0])
        self.ring.fill([0, 8, 0, 0])
        self.ring.fill([0, 0, 8, 0])
        return

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

    def read_encoder(self):
        '''
        Reads the position of the encoder
        '''
        self.encoder_position = self.encoder.position

        if self.encoder_position == self.encoder_last_position:
            return

        if self.encoder_position > self.encoder_last_position:
            self.counter += 1
            self.update_ring_colour()

        elif self.encoder_position < self.encoder_last_position:
            self.counter -= 1
            self.update_ring_colour()

        self.encoder_last_position = self.encoder_position
        self.encoder_last_change_time = time.time()
