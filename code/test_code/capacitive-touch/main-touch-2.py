import gc
import adafruit_dotstar
import time
import adafruit_mpr121
import busio
import board
import touchio


gc.collect()   # make some rooooom

dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5)


######################### HELPERS ##############################

def bin_data(value, number_of_bins=3, max_bin_size=255, max_value_size=1000, single_bin=False):
    scaled_value = value * ((number_of_bins * max_bin_size) / max_value_size)
    bins = []
    count = 0
    while count < number_of_bins:
        if scaled_value > max_bin_size:
            if single_bin:
                bins.append(0)
            else:
                bins.append(255)
            scaled_value = scaled_value - 255
        else:
            bins.append(int(scaled_value))
            scaled_value = 0

        count += 1

    return bins

def calculate_position(state):
    def _clean_state(l):
        def _round_by(val, round_by=6.0):
            return int(round(val/round_by)*round_by)

        clean_state = []
        for i in l:
            if i < 10:
                clean_state.append(0)
            else:
                clean_state.append(_round_by(i))

        return clean_state

    # Round all items and fix negative values
    state = _clean_state(state)

    # If all values the same
    if len(set(state)) == 1:
        return 0

    length = len(state)
    ratio = 1000 / (length - 1)
    max_item = max(state)
    max_item_index = state.index(max_item)

    if max_item_index + 1 == length:
        # If last item is the max
        analyse = [state[-2], max_item, 0]
    elif max_item_index == 0:
        # If first item is the max
        analyse = [0, max_item, state[1]]
    else:
        analyse = [state[max_item_index - 1], max_item, state[max_item_index + 1]]

    centre = analyse[1]
    left = analyse[0]
    right = analyse[2]
    max_side = max([left, right])

    if left > right:
        multiplier = -1
    else:
        multiplier = 1

    distance_from_centre = max_side / centre * 0.5 * multiplier
    value = (ratio * max_item_index) + (distance_from_centre * ratio)

    return value


######################### MAIN LOOP ##############################

touch_pins = [
    touchio.TouchIn(board.A1),
    touchio.TouchIn(board.A2),
    touchio.TouchIn(board.A3),
    touchio.TouchIn(board.A4),
    touchio.TouchIn(board.A5),
]

touch_data = []

for i in touch_pins:
    baseline = i.raw_value
    scaler = 1000 / baseline
    touch_data.append((i, baseline, scaler))

while True:
    state = []
    for i in touch_data:
        level = (i[0].raw_value * i[2]) - 1000
        state.append(level)

    finger_position = calculate_position(state)
    # print(state)
    # print(finger_position)
    # print(bin_data(finger_position))
    # time.sleep(0.1)

    dot[0] = bin_data(finger_position)
