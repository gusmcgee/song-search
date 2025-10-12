from scipy.signal import butter, filtfilt
import numpy as np


def highpass_filter(signal, sample_rate, cutoff=80, order=1):
    # Normalize cutoff to Nyquist frequency
    nyq = sample_rate / 2
    b, a = butter(order, cutoff / nyq, btype="high")
    return filtfilt(b, a, signal)


def normalize(signal, sample_rate, target_rms=0.2):
    # Oscillates about y = 0
    signal = signal - np.mean(signal)

    # High pass filer
    signal = highpass_filter(signal, sample_rate)

    # Apply root mean square normalizaiton
    rms = np.sqrt(np.mean(signal**2))
    # Scale signal
    signal = signal * (target_rms / rms)

    # Clip big values
    signal = np.clip(signal, -1.0, 1.0)

    return signal
