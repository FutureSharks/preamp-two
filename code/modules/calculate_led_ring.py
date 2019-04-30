# -*- coding: utf-8 -*-


def calculate_volume_ring(levels=200, num_pixels=16, pxl_max_value=32):
    '''
    Returns the RGBW values for the ring of 16 NeoPixels on the volume control
    '''
    result = []
    pxl_val = levels / num_pixels

    for level in range(levels):
        ring_values = [0] * num_pixels
        pixels_fully_lit = int(level / pxl_val)
        pixel_partially_lit = (level / pxl_val) - pixels_fully_lit
        ring_values[:pixels_fully_lit] = [pxl_max_value] * pixels_fully_lit
        ring_values[pixels_fully_lit] = int(pxl_max_value * pixel_partially_lit)
        ring_values[pixels_fully_lit + 1:] = [0] * (num_pixels - pixels_fully_lit - 1)

        result.append([i for i in ring_values])

    return result

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
