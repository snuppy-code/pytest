import pygame
from enum import Enum
from pathlib import Path
from pygame.mixer import Sound

###########

BASE_PATH = "assets/audio/"

if not pygame.mixer.get_init():
    pygame.mixer.init()

class Audios(Enum):
    WALKING = "walking_loopable.wav"
    WILDWIND = "wildwind.wav"

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




