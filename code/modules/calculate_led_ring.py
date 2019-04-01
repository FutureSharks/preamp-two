# -*- coding: utf-8 -*-


def calculate_volume_ring(level):
    '''
    Returns the RGBW values for the ring of 16 NeoPixels on the volume control
    '''
    return [(round(level/512), 0, 0, 0) for i in range(16)]

def calculate_input_ring(input):
    '''
    Returns the RGBW values for the ring of 16 NeoPixels on the input selector
    '''
    if input == 1:
        return [(16, 0, 0, 0)]
    if input == 2:
        return [(0, 16, 0, 0)]
    if input == 3:
        return [(0, 0, 16, 0)]
    if input == 4:
        return [(0, 0, 0, 16)]
    if input == 5:
        return [(8, 8, 0, 0)]
    if input == 6:
        return [(0, 0, 8, 8)]
