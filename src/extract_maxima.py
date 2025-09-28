import numpy as np
import math


def extract_local_maxima(spectrogram, box_height_hz=30, box_width_hops=50):

    num_rows, num_cols = spectrogram.shape

    num_box_rows = math.ceil(num_rows / box_height_hz)
    num_box_cols = math.ceil(num_cols / box_width_hops)

    # Reverse (num_box_cols, num_box_rows, 2) instead of (num_box_rows, num_box_cols, 2)
    # is reqired for time efficient sorting of local_maxima wrt to time.
    local_maxima = np.zeros((num_box_cols, num_box_rows, 2), dtype=int)

    for i_local_maxima, left_of_box in enumerate(range(0, num_cols, box_width_hops)):
        right_of_box = min(left_of_box + box_width_hops, num_cols)

        for j_local_maxima, top_of_box in enumerate(range(0, num_rows, box_height_hz)):
            bottom_of_box = min(top_of_box + box_height_hz, num_rows)

            block = spectrogram[top_of_box:bottom_of_box, left_of_box:right_of_box]

            idx_of_max_flattend_form = np.argmax(block)
            max_val_box_row, max_val_box_col = np.unravel_index(
                idx_of_max_flattend_form, block.shape
            )

            max_val_row = max_val_box_row + top_of_box
            max_val_col = max_val_box_col + left_of_box

            HZ_INDEX_INDEX = 0
            TIME_INDEX_INDEX = 1
            local_maxima[i_local_maxima, j_local_maxima, HZ_INDEX_INDEX] = max_val_row
            local_maxima[i_local_maxima, j_local_maxima, TIME_INDEX_INDEX] = max_val_col

        # Sort the new row of values by time
        local_maxima[i_local_maxima] = local_maxima[i_local_maxima][
            local_maxima[i_local_maxima][:, 1].argsort()
        ]

    return local_maxima.reshape(-1, 2)
