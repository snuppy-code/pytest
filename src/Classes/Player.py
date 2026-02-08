import pygame
from pygame.math import Vector2
from src.constants.vectors import *
from enum import Enum

pygame.init()

class WalkDownAnimations(Enum):
    WALK_DOWN_1 = "walk_down_1.png"
    WALK_DOWN_2 = "walk_down_2.png"
    WALK_DOWN_3 = "walk_down_3.png"
    WALK_DOWN_4 = "walk_down_4.png"

class IdleAnimation(Enum):
    IDLE = "idle.png"


class Player:
    def __init__(self,ctx):
        self.pos = Vector2(ctx.w/2, ctx.h/2)
        self.inventory = {}
        self.health = 100
        self.objects_on_screen = []
        self.harvest_indicator = pygame.font.Font(None, 24).render("F to harvest", True, (255,255,255))
        self.ctx = ctx
        self.qte = False
        self.obj_to_harvest = None
        self.tick = 0
        self.t0 = 0
        self.last_animation_class = IdleAnimation
        self.animation_class = IdleAnimation

    def _move(self, lookVector):
        self.pos += (lookVector * 200) * self.ctx.dt_s

    def _animate(self):
        pass

    def teleport(self, toPos):
        self.pos = toPos

    def draw_indicator(self, obj): 
        rect = self.harvest_indicator.get_rect()
        rect.midbottom = obj.rect.midtop
        rect.y -= 10
        self.ctx.vscreen.blit(self.harvest_indicator, rect)

    def quick_time_event(self):
        pass

        
    def update(self, events):
        keys = pygame.key.get_pressed()
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_f or event.key != pygame.K_SPACE and self.qte:
                    self.qte = False

                if event.key == pygame.K_f and self.obj_to_harvest != None and self.qte == False:
                    self.qte = True
                    self.quick_time_event()
                    

        if keys[pygame.K_w]:
            self._move(UP)

        if keys[pygame.K_a]:
            self._move(LEFT)

        if keys[pygame.K_s]:
            self._move(DOWN)

        if keys[pygame.K_d]:
            self._move(RIGHT)
            self._animate()


        closest_harvestable_obj = None
        min_dist = 20

        for obj in self.objects_on_screen:
            dist = self.pos.distance_to(obj.pos)

            if dist < min_dist:
                min_dist = dist
                closest_harvestable_obj = obj

        if closest_harvestable_obj != None and (not self.qte):
            self.draw_indicator(closest_harvestable_obj)

        self.obj_to_harvest = closest_harvestable_obj
        self.tick += self.ctx.dt_s
            
        
