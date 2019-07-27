# -*- coding: utf-8 -*-

import time
from .encoder_panel import EncoderPanel


class InputControl(EncoderPanel):
    '''
    Input control module
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b, change_object, debug=True, fade_colour=(1, 0, 1, 0)):
        super(InputControl, self).__init__(pixel_pin, encoder_pin_a, encoder_pin_b)
        self.change_object = change_object
        self.increment_before_change = 26
        self.encoder_last_position = 0
        self.encoder_last_change = 0
        self.encoder_position = 0
        self.fade_colour = fade_colour
        self.last_change_time = time.time()
        self.debug = debug

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
        self.ring.fill(self.fade_colour)
        return

    def unfade_ring(self):
        '''
        Fades ring to a low brightness
        '''
        self._print('unfading')
        self.fill_pixel_ring(self.calculate_input_ring(self.change_object.input_current))
        return

    def calculate_input_ring(self, input):
        '''
        Returns the RGBW values for the ring of 16 NeoPixels on the input selector
        '''
        if input == 1:
            return (16, 0, 0, 2)
        if input == 2:
            return (16, 9, 0, 0)
        if input == 3:
            return (0, 16, 16, 0)
        if input == 4:
            return (0, 0, 16, 0)
        if input == 5:
            return (9, 0, 16, 0)
        if input == 6:
            return (0, 16, 0, 10)

    def read_encoder(self):
        '''
        Reads the position of the encoder
        '''
        self.encoder_position = self.encoder.position

        if self.encoder_last_position == self.encoder_position:
            return

        if self.encoder_position > (self.encoder_last_change + self.increment_before_change):
            self.change_object.up()
            self.encoder_last_change = self.encoder_position
            self.fill_pixel_ring(self.calculate_input_ring(self.change_object.input_current))
        elif self.encoder_position < (self.encoder_last_change - self.increment_before_change):
            self.change_object.down()
            self.encoder_last_change = self.encoder_position
            self.fill_pixel_ring(self.calculate_input_ring(self.change_object.input_current))

        self.encoder_last_position = self.encoder_position
        self.last_change_time = time.time()
