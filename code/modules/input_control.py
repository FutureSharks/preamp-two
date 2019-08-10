# -*- coding: utf-8 -*-

import time
from .encoder_panel import EncoderPanel


class InputControl(EncoderPanel):
    '''
    Input control module
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b, selector, input=1, debug=False):
        super(InputControl, self).__init__(pixel_pin, encoder_pin_a, encoder_pin_b)
        self.selector = selector
        self.encoder_last_position = 0
        self.encoder_position = 0
        self.last_change_time = time.time()
        self.debug = debug
        self.counter_crossover_points = [int((i*21.17) + 1) for i in range(0, 6)]
        self.selector.select_input(input)
        self.counter = self.counter_crossover_points[input - 1]
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
        Updates the ring colour based on the current encoder position counter and changes inputs
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

        input = int(self.counter/21.17) + 1

        if self.counter in self.counter_crossover_points and self.selector.input_current != input:
            self.selector.select_input(input)
            self.flash_ring()

        self.last_change_time = time.time()
        self.fill_pixel_ring((int(r/8), int(g/8), int(b/8), 0))

    def flash_ring(self):
        '''
        Flashes the ring briefly to indicate a change
        '''
        self.ring.fill([8, 0, 0, 0])
        self.ring.fill([0, 8, 0, 0])
        self.ring.fill([0, 0, 8, 0])
        return

    def read_encoder(self):
        '''
        Reads the position of the encoder and takes action
        '''
        self.encoder_position = self.encoder.position

        if self.counter not in self.counter_crossover_points and time.time() - self.last_change_time > 2:
            desired_point = self.counter_crossover_points[self.selector.input_current - 1]
            self._print('fading to: {0}'.format(desired_point))
            while self.counter not in self.counter_crossover_points:
                if self.counter > 106:
                    self.counter += 1
                elif self.counter > desired_point:
                    self.counter -= 1
                else:
                    self.counter += 1
                self.update_ring_colour()
            self._print('fading done')

        if self.encoder_position == self.encoder_last_position:
            return

        if self.encoder_position > self.encoder_last_position:
            self.counter += 1
            self.update_ring_colour()

        elif self.encoder_position < self.encoder_last_position:
            self.counter -= 1
            self.update_ring_colour()

        self.encoder_last_position = self.encoder_position
