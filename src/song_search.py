from dbm import DBM


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
        plot_width=13,
        plot_height=8,
        fan_value=5,
        target_zone=50,
    ):
        self.dbm = DBM()
        self.desired_sample_rate = desired_sample_rate
        self.hop_length = hop_length
        self.box_height_hz = box_height_hz
        self.box_width_hops = box_width_hops
        self.n_fft = n_fft
        self.duration = duration
        self.offset = offset
        self.plot_width = plot_width
        self.plot_height = plot_height
        self.fan_value = fan_value
        self.target_zone = target_zone

    def add_song(self, path, name):
        self.dbm.add_song(
            path,
            name,
            desired_sample_rate=self.desired_sample_rate,
            hop_length=self.hop_length,
            box_height_hz=self.box_height_hz,
            box_width_hops=self.box_width_hops,
            n_fft=self.n_fft,
            duration=self.duration,
            offset=self.offset,
            fan_value=self.fan_value,
            target_zone=self.target_zone,
        )

    def search_song(self, path):
        return self.dbm.search_song(
            path,
            desired_sample_rate=self.desired_sample_rate,
            hop_length=self.hop_length,
            box_height_hz=self.box_height_hz,
            box_width_hops=self.box_width_hops,
            n_fft=self.n_fft,
            fan_value=self.fan_value,
            target_zone=self.target_zone,
        )
