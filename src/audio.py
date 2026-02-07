import pygame
from enum import Enum
from pathlib import Path
from pygame.mixer import Sound

###########

BASE_PATH = Path.cwd() / "assets" / "audio"

if not pygame.mixer.get_init():
    pygame.mixer.init()

class Audios(Enum):
    PLING = "PLING.wav"

    def __init__(self, filename):
        self.filename = filename
        self._cache = None

    @property
    def sound(self):
        if self._cache is None:
            path = str(BASE_PATH / self.filename)
            self._cache = Sound(path)

        self._cache.play()

    def play(self):
        self.sound