import pygame
import pygame
from pathlib import Path
###########

if not pygame.font.get_init():
    pygame.font.init()

class Fonts:
    NOTO_SERIF_KHMER = pygame.font.SysFont("notoserifkhmer")
