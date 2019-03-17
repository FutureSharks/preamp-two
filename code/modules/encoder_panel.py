# -*- coding: utf-8 -*-

import neopixel
import rotaryio
import time


class EncoderPanel(object):
    '''
    Represents a EN1J encoder surrounded by a ring of 16 RGBW NeoPixels
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b):
        self.ring_num_neopixels = 16
        self.ring_offset = -3
        self.ring_resolution = 16
        self.ring = neopixel.NeoPixel(
            pin=pixel_pin,
            n=self.ring_num_neopixels,
            brightness=0.2,
            pixel_order=(1, 0, 2, 3)
        )
        self.encoder_resolution = 128
        self.encoder_last_position = 0
        self.encoder_position = 0
        self.encoder = rotaryio.IncrementalEncoder(encoder_pin_a, encoder_pin_b)
        self.intro_animation()

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

    def set_ring_point(self, point):
        '''
        Sets a dot on the ring at point
        '''
        x = point / self.encoder_resolution
        y = round(x * self.ring_resolution)
        return y

    def read_encoder(self):
        '''
        Reads and reports the position of the encoder
        '''
        while True:
            self.encoder_position = self.encoder.position

            if self.encoder_position >= self.encoder_resolution:
                self.encoder.position = self.encoder_resolution - 1
                self.encoder_position = self.encoder_resolution - 1
            elif self.encoder_position <= 0:
                self.encoder.position = 0
                self.encoder_position = 0

            self.ring.fill((self.encoder_position, 0, 0, 0))
            p = self.set_ring_point(self.encoder_position)
            self.ring[self._calculate_ring_offset(p)] = (0, 0, 255, 0)
            self.encoder_last_position = self.encoder_position
