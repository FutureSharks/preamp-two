# -*- coding: utf-8 -*-


class MdacAttenuator(object):
    '''
    Manages an MDAC attenuator via SPI
    '''
    def __init__(self, y):
        self.x = y
