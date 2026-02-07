import pygame
from src.worldobject import World
from pygame.math import Vector2
from src.constants.vectors import *

class Player:
    def __init__(self):
        self.pos = Vector2(World.w/2, World.h/2)
        self.inventory = {}
        self.health = 100

    def _move(self, lookVector):
        self.pos += (lookVector * 200) * World.dt_s

    def teleport(self, toPos):
        self.pos = toPos

    def quick_time_event(self, desired_plant):
        

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self._move(UP)

        if keys[pygame.K_a]:
            self._move(LEFT)

        if keys[pygame.K_s]:
            self._move(DOWN)

        if keys[pygame.K_d]:
            self._move(RIGHT)
