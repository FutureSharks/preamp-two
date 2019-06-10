# -*- coding: utf-8 -*-

import neopixel
from rotaryio import IncrementalEncoder
import time


class VolumeControl(object):
    '''
    Volume control module: EN1J encoder surrounded by a ring of 16 RGBW NeoPixels
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b, change_object, increment_before_change=1):
        self.change_object = change_object
        self.increment_before_change = increment_before_change
        self.ring_num_neopixels = 16
        self.ring_offset = -3
        self.ring_resolution = 16
        self.ring = neopixel.NeoPixel(
            pin=pixel_pin,
            n=self.ring_num_neopixels,
            pixel_order=(1, 0, 2, 3)
        )
        self.encoder_resolution = 128
        self.encoder_last_position = 0
        self.encoder_last_change = 0
        self.encoder_position = 0
        self.encoder = IncrementalEncoder(encoder_pin_a, encoder_pin_b)
        self.intro_animation()

    def write_single_pixel(self, pixel_number, pixel_value):
        '''
        Writes to a single NeoPixel on the ring
        '''
        if pixel_number > self.ring_num_neopixels:
            print('length of led_values cannot be higher than ring_num_neopixels: {0}'.format(self.ring_num_neopixels))
            return

        self.ring[pixel_number - 1] = pixel_value
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

    def set_ring_point(self, point):
        '''
        Sets a dot on the ring at point
        '''
        x = point / self.encoder_resolution
        y = round(x * self.ring_resolution)
        return y

    def calculate_volume_ring(self, level):
        '''
        Returns the RGBW values for the ring of 16 NeoPixels on the volume control
        '''
        levels = 128
        num_pixels = 16
        pxl_max_value = 64
        pxl_val = levels / num_pixels
        ring_values = [0] * num_pixels
        start_offset = int(level / pxl_val)
        pixel_partially_lit = (level / pxl_val) - start_offset
        pixel = int(pxl_max_value * pixel_partially_lit)
        return (start_offset + 1, [pixel, 3, 3, 0])

    def read_encoder(self):
        '''
        Reads the position of the encoder
        '''
        self.encoder_position = self.encoder.position

        if self.encoder_position > (self.encoder_last_change + self.increment_before_change):
            self.change_object.up()
            self.encoder_last_change = self.encoder_position
            self.write_single_pixel(*self.calculate_volume_ring(self.change_object.level))
        elif self.encoder_position < (self.encoder_last_change - self.increment_before_change):
            self.change_object.down()
            self.encoder_last_change = self.encoder_position
            self.write_single_pixel(*self.calculate_volume_ring(self.change_object.level))

        self.encoder_last_position = self.encoder_position
