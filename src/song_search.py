import librosa
import numpy as np
from preprocess import normalize
from extract_maxima import extract_local_maxima
from hashing import generate_hashes


class SongSearch:
    def __init__(
        self,
        desired_sample_rate=22050,
        hop_length=256,
        box_height_hz=30,
        box_width_hops=50,
        n_fft=4096,
        duration=None,
        offset=0.0,
        fan_value=5,
        target_zone=50,
        target_rms=0.2,
    ):
        self.db = {}
        self.desired_sample_rate = desired_sample_rate
        self.hop_length = hop_length
        self.box_height_hz = box_height_hz
        self.box_width_hops = box_width_hops
        self.n_fft = n_fft
        self.duration = duration
        self.offset = offset
        self.fan_value = fan_value
        self.target_zone = target_zone
        self.target_rms = target_rms

    def getDB(self):
        return self.db

    def add_song(self, path, song_id):
        signal, sample_rate = librosa.load(
            path,
            sr=self.desired_sample_rate,
            mono=True,
            duration=self.duration,
            offset=self.offset,
        )
        signal = normalize(signal, sample_rate, target_rms=self.target_rms)

        spectrogram = create_spectrogram(signal, self.n_fft, self.hop_length)

        local_maxima = extract_local_maxima(
            spectrogram,
            box_height_hz=self.box_height_hz,
            box_width_hops=self.box_width_hops,
        )

        hashes = generate_hashes(local_maxima, self.fan_value, self.target_zone)
        for h, t1 in hashes:
            if h not in self.db:
                self.db[h] = []
            self.db[h].append((song_id, t1))

    def search_song(self, path):
        # Process the new search clip just like the db songs
        signal, sample_rate = librosa.load(path, sr=self.desired_sample_rate, mono=True)
        signal = normalize(signal, sample_rate, target_rms=self.target_rms)

        spectrogram = create_spectrogram(signal, self.n_fft, self.hop_length)
        local_maxima = extract_local_maxima(
            spectrogram, self.box_height_hz, self.box_width_hops
        )
        hashes = generate_hashes(local_maxima, self.fan_value, self.target_zone)

        matches = {}  # song_id -> number of matching hashes
        for h, t1 in hashes:
            if h in self.db:
                for song_id, _ in self.db[h]:
                    matches[song_id] = matches.get(song_id, 0) + 1

        sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)

        return sorted_matches


def create_spectrogram(signal, n_fft, hop_length):
    stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)
    return np.abs(stft)
