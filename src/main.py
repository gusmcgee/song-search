import librosa
from song_search import SongSearch
from preprocess import normalize
from extract_maxima import extract_local_maxima
from plot import plot
from pathlib import Path
import numpy as np


song_search = SongSearch()


def plotSpectrogram(path):
    signal, sample_rate = librosa.load(
        path,
        sr=song_search.desired_sample_rate,
        mono=True,
        duration=song_search.duration,
        offset=song_search.offset,
    )
    signal = normalize(signal, sample_rate)

    spectrogram = np.abs(
        librosa.stft(signal, n_fft=song_search.n_fft, hop_length=song_search.hop_length)
    )

    local_maxima = extract_local_maxima(
        spectrogram,
        box_height_hz=song_search.box_height_hz,
        box_width_hops=song_search.box_width_hops,
    )

    plot(
        spectrogram,
        local_maxima,
        sample_rate,
        song_search.hop_length,
        song_search.n_fft,
        plot_width=song_search.plot_width,
        plot_height=song_search.plot_height,
    )


def main():
    # Load songs from song-files
    song_files_path = Path("song-files")
    song_files = [f for f in song_files_path.iterdir() if f.is_file()]

    for file_path in song_files:
        song_name = file_path.stem
        file_type = file_path.suffix

        if file_type == ".wav":
            print("Adding:", str(file_path))
            song_search.add_song(file_path, song_name)

    # Match songs from live-song-snippets to songs in song-files
    snippet_path = Path("live-song-snippets")
    snippet_files = [f for f in snippet_path.iterdir() if f.is_file()]
    for file_path in snippet_files:
        song_name = file_path.stem
        file_type = file_path.suffix

        if file_type == ".wav":
            snippet_name = file_path.stem
            result = song_search.search_song(file_path)
            print(snippet_name, "matches to...", result[:min(5, len(result))], "\n")


if __name__ == "__main__":
    main()
