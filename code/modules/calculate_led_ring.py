# -*- coding: utf-8 -*-


def calculate_volume_ring(level):
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

    return (start_offset + 1, [pixel, 0, 0, 0])

def calculate_input_ring(input):
    '''
    Returns the RGBW values for the ring of 16 NeoPixels on the input selector
    '''
    if input == 1:
        return (16, 0, 0, 0)
    if input == 2:
        return (0, 16, 0, 0)
    if input == 3:
        return (0, 0, 16, 0)
    if input == 4:
        return (0, 0, 0, 16)
    if input == 5:
        return (8, 8, 0, 0)
    if input == 6:
        return (0, 0, 8, 8)
