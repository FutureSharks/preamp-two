# -*- coding: utf-8 -*-

import neopixel
from rotaryio import IncrementalEncoder
import time


class VolumeControl(object):
    '''
    Volume control module: EN1J encoder surrounded by a ring of 16 RGBW NeoPixels
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b, change_object, debug=True, fade_colour=(1, 0, 1, 0)):
        self.change_object = change_object
        self.increment_before_change = 1
        self.ring_num_neopixels = 16
        self.ring_offset = 5
        self.offset_ring_addesses = list(range(0, self.ring_num_neopixels))[self.ring_offset:] + list(range(0, self.ring_num_neopixels))[:self.ring_offset]
        self.ring = neopixel.NeoPixel(
            pin=pixel_pin,
            n=self.ring_num_neopixels,
            pixel_order=(1, 0, 2, 3)
        )
        self.encoder_resolution = 128
        self.encoder_last_position = 0
        self.encoder_last_change = 0
        self.encoder_position = 0
        self.fade_colour = fade_colour
        self.encoder = IncrementalEncoder(encoder_pin_a, encoder_pin_b)
        self.last_change_time = time.time()
        self.debug = debug
        self.intro_animation()

    def _print(self, message):
        '''
        Small function for printing information is debug option is enabled
        '''
        if not self.debug:
            return
        else:
            print('volume-control: {0}'.format(message))

    def write_single_pixel(self, pixel_number, pixel_value):
        '''
        Writes to a single NeoPixel on the ring
        '''
        if pixel_number > self.ring_num_neopixels:
            _print('length of led_values cannot be higher than ring_num_neopixels: {0}'.format(self.ring_num_neopixels))
            return

        self.ring[self.offset_ring_addesses[pixel_number]] = pixel_value
        self.ring.show()

    def fill_pixel_ring(self, pixel_values):
        '''
        Fills the ring with a single value
        '''
        self.ring.fill(pixel_values)
        self.ring.show()

    def intro_animation(self):
        '''
        Displays a short ring animation
        '''
        for pxl in range(self.ring_num_neopixels):
            n = self.offset_ring_addesses[pxl]
            n_1 = self.offset_ring_addesses[min(pxl + 1, self.ring_num_neopixels - 1)]
            self.ring[n] = (0, 0, 255, 0)
            self.ring[n_1] = (255, 0, 0, 0)
            time.sleep(0.02)

        self.ring.fill((0, 3, 3, 0))

    def test_ring(self):
        '''
        Cycles through colors for the whole ring
        '''
        self.ring.fill((255, 0, 0, 0))
        time.sleep(1)
        self.ring.fill((0, 255, 0, 0))
        time.sleep(1)
        self.ring.fill((0, 0, 255, 0))
        time.sleep(1)
        self.ring.fill((0, 0, 0, 255))
        time.sleep(1)
        self.ring.fill((0, 0, 0, 0))
        return

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

        if self.encoder_position > (self.encoder_last_change + self.increment_before_change):
            self.change_object.up()
            self.encoder_last_change = self.encoder_position
            self.write_single_pixel(*self._calculate_volume_ring(self.change_object.level))
        elif self.encoder_position < (self.encoder_last_change - self.increment_before_change):
            self.change_object.down()
            self.encoder_last_change = self.encoder_position
            self.write_single_pixel(*self._calculate_volume_ring(self.change_object.level))

        self.encoder_last_position = self.encoder_position
        self.last_change_time = time.time()
