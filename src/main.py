import librosa
from preprocess import normalize
from spectrogram import create_spectrogram
from extract_maxima import extract_local_maxima
from plot import plot
from dbm import DBM

desired_sample_rate = 22050
hop_length = 256
box_height_hz = 30
box_width_hops = 50
n_fft = 4096
duration = None
offset = 0.0
plot_width = 13
plot_height = 8
fan_value = 5
target_zone = 50

dbm = DBM()


def add_song(path, name):
    dbm.add_song(
        path,
        name,
        desired_sample_rate=desired_sample_rate,
        hop_length=hop_length,
        box_height_hz=box_height_hz,
        box_width_hops=box_width_hops,
        n_fft=n_fft,
        duration=duration,
        offset=offset,
        fan_value=fan_value,
        target_zone=target_zone,
    )


def search_song(path):
    return dbm.search_song(
        path,
        desired_sample_rate=desired_sample_rate,
        hop_length=hop_length,
        box_height_hz=box_height_hz,
        box_width_hops=box_width_hops,
        n_fft=n_fft,
        fan_value=fan_value,
        target_zone=target_zone,
    )


def main():
    add_song("song-files/sound-like-radio.wav", "sound like radio bruh")
    add_song("song-files/Angst-INZO.wav", "angst")
    add_song(
        "song-files/Good Times & Tan Lines - Zach Top.wav", "Good Times & Tan Lines"
    )

    result = search_song("song-files/live_radio.wav")

    print(result)

    # Plot graph
    # signal, sample_rate = librosa.load(
    #     "song-files/sound-like-radio.wav",
    #     sr=desired_sample_rate,
    #     mono=True,
    #     duration=duration,
    #     offset=offset,
    # )
    # signal = normalize(signal, sample_rate)

    # spectrogram = create_spectrogram(
    #     signal, sample_rate, hop_length=hop_length, n_fft=n_fft
    # )
    # local_maxima = extract_local_maxima(
    #     spectrogram, box_height_hz=box_height_hz, box_width_hops=box_width_hops
    # )

    # plot(
    #     spectrogram,
    #     local_maxima,
    #     sample_rate,
    #     hop_length,
    #     n_fft,
    #     plot_width=plot_width,
    #     plot_height=plot_height,
    # )

    # Save processed audio
    # # 2. Save as 16-bit PCM WAV
    # import soundfile as sf
    # sf.write("output8.wav", samples, new_rate, subtype="PCM_16")


if __name__ == "__main__":
    main()
