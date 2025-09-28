import numpy as np
import librosa

def create_spectrogram(signal, sample_rate, n_fft=4096, hop_length=256):
    stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)
    return np.abs(stft)