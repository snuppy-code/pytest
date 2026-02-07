import pygame
import pygame
from enum import Enum
from pathlib import Path
###########

if not pygame.font.get_init():
    pygame.font.init()

class Fonts(Enum):
    NOTO_SERIF_KHMER = pygame.font.SysFont("notoserifkhmer")
