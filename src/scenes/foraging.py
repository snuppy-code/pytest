import pygame
import random
from src.Classes.ForagingAssets import *
from src.audio import Audios
from src.interactibles import *

class Foraging:
    def __init__(self,ctx):
        self.ctx = ctx
        self.objects_on_screen = []
        self.background_sound = Audios.WILDWIND

        insertInfo(self.ctx.images, self.ctx)


    def onEnter(self):
        print("hi")
        self.collision_rect = pygame.Rect(40,50,200,170)

        # fix this mama
        # you don't want to have rocks and stuff ON THE ROAD!!!!!!
        insertInfo(self.ctx.images, self.ctx)
        self.background_sound.WILDWIND.play(-1, 0.5)

        choices = [PotatoBush, Rock]
        weights = [1, 1]


        background_width, background_height = self.ctx.images["foraging_map.png"].get_size()

        for i in range(50):
            asset_class = random.choices(choices, weights, k=1)[0]
            temp_sprite = asset_class()
            w, h = temp_sprite.image.get_size()

            attempts = 50
            for a in range(attempts):
                x = random.randint(0, background_width - w)
                y = random.randint(0, background_height - h)

                new_rect = pygame.Rect(x, y, w, h)

                if any(new_rect.colliderect(a.rect) for a in self.objects_on_screen):
                    continue

                if new_rect.colliderect(self.collision_rect):
                    continue

                temp_sprite.pos = pygame.math.Vector2(x, y)
                temp_sprite.rect = new_rect
                temp_sprite.collision_rect = pygame.Rect(0,0, 10, 10)
                temp_sprite.collision_rect.center = temp_sprite.rect.center
                self.objects_on_screen.append(temp_sprite)
                break
        
        self.bounds = RectZone(self.ctx.images["foraging_map.png"].get_rect())
        self.ctx.player.teleport(pygame.math.Vector2(40, 162))

        self.ctx.player.obj_in_scene = self.objects_on_screen

    def onExit(self):
        self.background_sound.WILDWIND.stop()
        pass

    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s

        self.ctx.vscreen.blit(self.ctx.images["foraging_map.png"], self.ctx.player.pos*-0.5)

        for obj in self.objects_on_screen:
            obj.draw()
    
        self.ctx.player.update(events)
        self.ctx.player.draw()


    def alwaysTick(self, events):
        pass
        