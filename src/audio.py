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
    PLING_2 = "PLING2.wav"

    def __init__(self, filename):
        full_path = str(BASE_PATH / filename)
        try:
            self.s = pygame.mixer.Sound(full_path)
        except pygame.error:
            self.s = None

    def play(self, loops=0, volume=0.5):
        if self.s:
            self.s.set_volume(volume)
            self.s.play(loops=loops)


<<<<<<< Updated upstream
<<<<<<< Updated upstream
    def play(self):
        self.sound.play()
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
