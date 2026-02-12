from enum import Enum
import pygame

###########

BASE_PATH = "assets/audio/"


class Audios(Enum):
    WALKING = "walking_loopable.wav"
    WILDWIND = "wildwind.wav"
    DAMAGE_1 = "damage_1.wav"
    DAMAGE_2 = "damage_2.wav"
    DAMAGE_3 = "damage_3.wav"
    DAMAGE_4 = "damage_4.wav"
    DAMAGE_5 = "damage_5.wav"
    DAMAGE_6 = "damage_6.wav"
    DAMAGE_7 = "damage_7.wav"
    FORESTING_COMPLETE_GOOD = "foresting_complete_good.wav"

    def __init__(self, filename):
        full_path = BASE_PATH + filename
        try:
            self.s = pygame.mixer.Sound(full_path)
        except pygame.error:
            self.s = None

    def play(self, loops=0, volume=0.5):
        if self.s:
            self.s.set_volume(volume)
            self.s.play(loops=loops)

    def stop(self):
        if self.s:
            self.s.stop()
