# -*- coding: utf-8 -*-

import time
from .encoder_panel import EncoderPanel


class VolumeControl(EncoderPanel):
    '''
    Volume control module
    '''
    def __init__(self, pixel_pin, encoder_pin_a, encoder_pin_b, attenuator, level=30, debug=True):
        super(VolumeControl, self).__init__(pixel_pin, encoder_pin_a, encoder_pin_b)
        self.attenuator = attenuator
        self.encoder_last_position = 0
        self.encoder_last_change_position = 0
        self.encoder_position = 0
        self.encoder_last_change_time = time.time()
        self.colour_background = [0, 3, 3, 0]
        self.colour_level_pixel = 0
        self.pixel_max_brightness = 64
        self.debug = debug
        self.fade_ring()
        time.sleep(0.5)
        self.fade_to_level(level)


    def _print(self, message):
        '''
        Small function for printing information is debug option is enabled
        '''
        if not self.debug:
            return
        else:
            print('volume-control: {0}'.format(message))

    def up(self):
        self.attenuator.up()
        self.write_single_pixel(*self._calculate_volume_ring(self.attenuator.level))

    def down(self):
        self.attenuator.down()
        self.write_single_pixel(*self._calculate_volume_ring(self.attenuator.level))

    def fade_to_level(self, level):
        '''
        Fades to specifiied level
        '''
        self._print('fading to: {0}'.format(level))
        while self.attenuator.level < level:
            time.sleep(0.01)
            self.up()

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
        self.fade_ring()
        for i in range(0, self.attenuator.level):
            self.write_single_pixel(*self._calculate_volume_ring(i))
            time.sleep(0.01)

        return

    def _calculate_volume_ring(self, level):
        '''
        Returns the RGBW values for the 16 NeoPixels given a volume level
        '''
        levels = len(self.attenuator.levels)
        pxl_val = levels / self.ring_num_neopixels
        start_offset = int(level / pxl_val)
        pixel_partially_lit = (level / pxl_val) - start_offset
        level_pixel = int(self.pixel_max_brightness * pixel_partially_lit)
        pixel_value = self.colour_background.copy()
        pixel_value[self.colour_level_pixel] = level_pixel

        return (start_offset + 1, pixel_value)

    def read_encoder(self):
        '''
        Reads the position of the encoder
        '''
        self.encoder_position = self.encoder.position

        if self.encoder_position == self.encoder_last_position:
            return

        if self.encoder_position > self.encoder_last_position:
            self.up()

        elif self.encoder_position < self.encoder_last_position:
            self.down()

        self.encoder_last_position = self.encoder_position
        self.encoder_last_change_time = time.time()
