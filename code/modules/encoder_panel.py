# -*- coding: utf-8 -*-

import neopixel
from rotaryio import IncrementalEncoder
import time


class EncoderPanel(object):
    '''
    Represents a EN1J encoder surrounded by a ring of 16 RGBW NeoPixels
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b):
        self.ring_num_neopixels = 16
        self.ring_offset = -3
        self.offset_ring_addesses = list(range(0, self.ring_num_neopixels))[self.ring_offset:] + list(range(0, self.ring_num_neopixels))[:self.ring_offset]
        self.ring = neopixel.NeoPixel(
            pin=pixel_pin,
            n=self.ring_num_neopixels,
            pixel_order=(1, 0, 2, 3)
        )
        self.encoder = IncrementalEncoder(encoder_pin_a, encoder_pin_b)
        self.intro_animation()

    def write_single_pixel(self, pixel_number, pixel_value):
        '''
        Writes to a single NeoPixel on the ring
        '''
        if pixel_number > self.ring_num_neopixels:
            raise Exception('length of led_values cannot be higher than ring_num_neopixels: {0}'.format(self.ring_num_neopixels))

        self.ring[self.offset_ring_addesses[pixel_number - 1]] = pixel_value
        self.ring.show()

    def fill_pixel_ring(self, pixel_value):
        '''
        Fills the ring with a single value
        '''
        self.ring.fill(pixel_value)
        self.ring.show()

    def _calculate_ring_offset(self, pixel):
        '''
        Calculates offset between the top and first NeoPixels
        '''
        result = pixel + self.ring_offset

        if result < 0:
            result = self.ring_num_neopixels - abs(result)
        if result > self.ring_num_neopixels - 1:
            result = 0 + (result - self.ring_num_neopixels)

        return result

    def intro_animation(self):
        '''
        Displays a short ring animation
        '''
        for pxl in range(self.ring_num_neopixels):
            n = self._calculate_ring_offset(pxl)
            n_1 = self._calculate_ring_offset(min(pxl + 1, self.ring_num_neopixels - 1))
            self.ring[n] = (0, 0, 255, 0)
            self.ring[n_1] = (255, 0, 0, 0)
            time.sleep(0.02)

        self.ring.fill((0, 0, 0, 0))

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
