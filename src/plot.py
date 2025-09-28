import matplotlib.pyplot as plt
import librosa

plt.rcParams.update({"font.size": 12})


def plot(
    spectrogram,
    local_maxima,
    sample_rate,
    hop_length,
    n_fft,
    plot_width=15,
    plot_height=10,
):

    spectrogram_db = librosa.amplitude_to_db(spectrogram)

    plt.figure(figsize=(plot_width, plot_height))
    librosa.display.specshow(
        spectrogram_db,
        y_axis="log",
        x_axis="time",
        sr=sample_rate,
        hop_length=hop_length,
        cmap="inferno",
    )

    # Column indices -> time in seconds
    time_vals = local_maxima[:, 1] * hop_length / sample_rate

    # Row indices -> frequency in Hz
    freq_vals = local_maxima[:, 0] * sample_rate / n_fft

    # Overlay maxima on top of the spectrogram
    plt.scatter(time_vals, freq_vals, color="cyan", s=10, alpha=0.7, marker="o")

    plt.show()
