from amplifier import Amplifier
from cd_player import CdPlayer
from dvd_player import DvdPlayer
from home_theater_facade import HomeTheaterFacade
from tuner import Tuner

amplifier = Amplifier()
cd = CdPlayer()
dvd = DvdPlayer()
tuner = Tuner()

facade = HomeTheaterFacade(tuner, amplifier, cd, dvd)

facade.watch_movie()
facade.listen_to_cd()
facade.listen_to_radio()
facade.end_radio()
