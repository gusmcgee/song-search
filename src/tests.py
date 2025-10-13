from preprocess import normalize
import librosa
from song_search import SongSearch
import soundfile as sf
import os

song_search = SongSearch()


def test_normalize():
    os.makedirs("test-output", exist_ok=True)

    def test_on_file(name):
        signal, sample_rate = librosa.load(
            f"live-song-snippets/{name}", sr=song_search.desired_sample_rate, mono=True
        )
        signal = normalize(signal, sample_rate, target_rms=song_search.target_rms)
        sf.write(f"test-output/Processed {name}", signal, sample_rate, subtype="PCM_16")

    test_on_file("Angst 1.wav")
    test_on_file("Krunkberry Blossom 1.wav")
    test_on_file("Good Times & Tan Lines 2.wav")
    test_on_file("Processed Angst 11.wav")


if __name__ == "__main__":
    test_normalize()
