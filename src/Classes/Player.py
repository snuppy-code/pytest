import pygame
from src.worldobject import World
from pygame.math import Vector2
import src.constants.vectors

class Player:
    def __init__(self):
        self.pos = Vector2(World.w/2, World.h/2)

    def _move(self, lookVector):
        self.pos += (lookVector * 200) * World.dt_s

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self._move()
