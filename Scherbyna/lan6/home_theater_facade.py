class HomeTheaterFacade:
    def __init__(self, tuner, amplifier, cd_player, dvd_player):
        self.tuner = tuner
        self.amplifier = amplifier
        self.cd_player = cd_player
        self.dvd_player = dvd_player

    def watch_movie(self):
        self.tuner.on()
        self.dvd_player.on()
        self.dvd_player.play()

    def end_movie(self):
        self.dvd_player.stop()
        self.dvd_player.off()
        self.tuner.off()

    def listen_to_cd(self):
        self.cd_player.on()
        self.amplifier.on()
        self.cd_player.play()

    def end_to_cd(self):
        self.cd_player.off()
        self.amplifier.off()

    def listen_to_radio(self):
        self.tuner.on()
        self.tuner.set_frequency()

    def end_radio(self):
        self.tuner.off()