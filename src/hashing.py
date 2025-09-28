def generate_hashes(local_maxima, fan_value=5, target_zone=50):
    HZ_INDEX = 0
    TIME_INDEX = 1
    FREQ_BIN_SIZE = 2

    hashes = []

    for i, (freq1, t1) in enumerate(local_maxima):

        for j in range(1, fan_value + 1):

            if i + j >= local_maxima.shape[0]:
                break

            t2 = local_maxima[i + j, TIME_INDEX]
            freq2 = local_maxima[i + j, HZ_INDEX]
            dt = t2 - t1

            freq1_bin = freq1 // FREQ_BIN_SIZE
            freq2_bin = freq2 // FREQ_BIN_SIZE

            if 0 < dt <= target_zone:
                h = (
                    ((freq1_bin & 0xFFF) << 20)
                    | ((freq2_bin & 0xFFF) << 8)
                    | (dt & 0xFF)
                )
                hashes.append((h, t1))

    return hashes
