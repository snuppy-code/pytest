from enum import Enum
from pygame.mixer import Sound
from pathlib import Path

script_path = Path(__file__).resolve()
script_dir = script_path.parent


class Audios(Enum):
    CHOPPING = Sound(path)