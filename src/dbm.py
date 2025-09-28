import librosa
from preprocess import normalize
from spectrogram import create_spectrogram
from extract_maxima import extract_local_maxima
from plot import plot
from hashing import generate_hashes


class DBM:

    def __init__(self):
        self.db = {}

    def getDB(self):
        return self.db

    def add_song(
        self,
        path,
        song_id,
        desired_sample_rate=22050,
        hop_length=256,
        box_height_hz=30,
        box_width_hops=50,
        n_fft=4096,
        duration=None,
        offset=0.0,
        fan_value=5,
        target_zone=50,
    ):
        signal, sample_rate = librosa.load(
            path,
            sr=desired_sample_rate,
            mono=True,
            duration=duration,
            offset=offset,
        )
        signal = normalize(signal, sample_rate)

        spectrogram = create_spectrogram(
            signal, sample_rate, hop_length=hop_length, n_fft=n_fft
        )

        local_maxima = extract_local_maxima(
            spectrogram, box_height_hz=box_height_hz, box_width_hops=box_width_hops
        )

        hashes = generate_hashes(local_maxima, fan_value, target_zone)
        for h, t1 in hashes:
            if h not in self.db:
                self.db[h] = []
            self.db[h].append((song_id, t1))

    def search_song(
        self,
        path,
        desired_sample_rate=22050,
        hop_length=256,
        box_height_hz=30,
        box_width_hops=50,
        n_fft=4096,
        fan_value=5,
        target_zone=50,
    ):
        # Process the new search clip just like the db songs
        signal, sample_rate = librosa.load(path, sr=desired_sample_rate, mono=True)
        signal = normalize(signal, sample_rate)

        spectrogram = create_spectrogram(
            signal, sample_rate, hop_length=hop_length, n_fft=n_fft
        )
        local_maxima = extract_local_maxima(spectrogram, box_height_hz, box_width_hops)
        hashes = generate_hashes(local_maxima, fan_value, target_zone)

        matches = {}  # song_id -> number of matching hashes
        for h, t1 in hashes:
            if h in self.db:
                for song_id, _ in self.db[h]:
                    matches[song_id] = matches.get(song_id, 0) + 1

        sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)

        return sorted_matches
