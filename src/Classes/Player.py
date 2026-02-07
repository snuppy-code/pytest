import pygame
from pygame.math import Vector2
from src.constants.vectors import *

pygame.init()

class Player:
    def __init__(self,ctx):
        self.pos = Vector2(ctx.w/2, ctx.h/2)
        self.inventory = {}
        self.health = 100
        self.objects_on_screen = []
        self.harvest_indicator = pygame.font.Font(None, 24).render("F to harvest", True, (255,255,255))
        self.ctx = ctx

    def _move(self, lookVector):
        self.pos += (lookVector * 200) * self.ctx.dt_s

    def teleport(self, toPos):
        self.pos = toPos

    def draw_indicator(self, obj): 
        rect = self.harvest_indicator.get_rect()
        rect.midbottom = obj.rect.midtop
        rect.y -= 10
        self.ctx.vscreen.blit(self.harvest_indicator, rect)
        
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
        min_dist = 20

        for obj in self.objects_on_screen:
            dist = self.pos.distance_to(obj.pos)

            if dist < min_dist:
                min_dist = dist
                closest_harvestable_obj = obj

        if closest_harvestable_obj != None:
            self.draw_indicator(closest_harvestable_obj)
            
        
