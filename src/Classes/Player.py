import pygame
from pygame.math import Vector2
from src.constants.vectors import *

class Player:
    MIN_DIST = 20

    def __init__(self,ctx):
        self.pos = Vector2(ctx.w/2, ctx.h/2)
        self.inventory = {}
        self.health = 100
        self.objects_on_screen = []

    def _move(self, lookVector):
        self.pos += (lookVector * 200) * self.ctx.dt_s

    def teleport(self, toPos):
        self.pos = toPos

    def draw_indicator(self, obj):
        pass
        

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

        closest_harvestable_obj = None

        for obj in self.objects_on_screen:
            dist = self.pos.distance_to(obj.pos)

            if dist < min_dist:
                min_dist = dist
                closest_harvestable_obj = obj

        if closest_harvestable_obj != None:
            self.draw_indicator(closest_harvestable_obj)
            
        
