# -*- coding: utf-8 -*-

import time
from .encoder_panel import EncoderPanel


class VolumeControl(EncoderPanel):
    '''
    Volume control module
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b, change_object, debug=True):
        super(VolumeControl, self).__init__(pixel_pin, encoder_pin_a, encoder_pin_b)
        self.change_object = change_object
        self.encoder_last_position = 0
        self.encoder_last_change = 0
        self.encoder_position = 0
        self.encoder_last_change_time = time.time()
        self.fade_colour = (1, 0, 1, 0)
        self.debug = debug
        self.fade_ring()



    def _print(self, message):
        '''
        Small function for printing information is debug option is enabled
        '''
        if not self.debug:
            return
        else:
            print('volume-control: {0}'.format(message))

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
        self.ring.fill((0, 3, 3, 0))
        pixel_val = self._calculate_volume_ring(self.change_object.level)
        for pxl in range(pixel_val[0]):
            time.sleep(0.01)
            self.write_single_pixel(pxl, pixel_val[1])
        return

    def _calculate_volume_ring(self, level):
        '''
        Returns the RGBW values for the 16 NeoPixels given a volume level
        '''
        levels = 128
        num_pixels = 16
        pxl_max_value = 64
        primary_colour = (8, 0, 0, 0)
        secondary_colour = (0, 0, 8, 0)

        pxl_val = levels / num_pixels
        start_offset = int(level / pxl_val)
        pixel_partially_lit = (level / pxl_val) - start_offset
        pixel = int(pxl_max_value * pixel_partially_lit)
        return (start_offset + 1, [pixel, 3, 3, 0])

    def read_encoder(self):
        '''
        Reads the position of the encoder
        '''
        self.encoder_position = self.encoder.position

        if self.encoder_last_position == self.encoder_position:
            return

        if self.encoder_position > (self.encoder_last_change):
            self.change_object.up()
            self.encoder_last_change = self.encoder_position
            self.write_single_pixel(*self._calculate_volume_ring(self.change_object.level))
        elif self.encoder_position < (self.encoder_last_change):
            self.change_object.down()
            self.encoder_last_change = self.encoder_position
            self.write_single_pixel(*self._calculate_volume_ring(self.change_object.level))

        self.encoder_last_position = self.encoder_position
        self.encoder_last_change_time = time.time()
