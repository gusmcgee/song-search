import librosa
from song_search import SongSearch
from preprocess import normalize
from spectrogram import create_spectrogram
from extract_maxima import extract_local_maxima
from plot import plot
import sys
import soundfile as sf


song_search = SongSearch()


def plotSpectrogram():
    signal, sample_rate = librosa.load(
        "song-files/sound-like-radio.wav",
        sr=song_search.desired_sample_rate,
        mono=True,
        duration=song_search.duration,
        offset=song_search.offset,
    )
    signal = normalize(signal, sample_rate)

    spectrogram = create_spectrogram(
        signal, sample_rate, hop_length=song_search.hop_length, n_fft=song_search.n_fft
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


def save_processed_audio(path, subtype="PCM_16"):
    sf.write(path, song_search.samples, song_search.new_rate, subtype=subtype)


def main():

    args = []
    if len(sys.argv) > 1:
        args = sys.argv[1:]

    for path in args:
        file_name = path.split("/")[-1]
        song_name = file_name.split(".")[0]
        file_type = file_name.split(".")[1]

        if file_type == "wav":
            print("Adding:", file_name)
            song_search.add_song(path, song_name)

    result = song_search.search_song("live-song-snippets/live_radio.wav")
    print(result[:5])


if __name__ == "__main__":
    main()
