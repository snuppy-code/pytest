from src.Classes.ForagingAssets import insertSprites
import pygame
import pygame_gui # type: ignore
import random
from src.Classes.ForagingAssets import *

class Foraging:
    def __init__(self,ctx):
        self.ctx = ctx
        self.assets = []

    def onEnter(self):
        insertSprites(self.ctx.foraging_sprites)

        choices = [PotatoBush, Rock]
        weights = [1, 1]

        background_width, background_height = self.ctx.images["foraging_background.png"].get_size()

        for i in range(50):
            asset_class = random.choices(choices, weights, k=1)[0]
            temp_sprite = asset_class()
            w, h = temp_sprite.image.get_size()

            attempts = 50
            for a in range(attempts):
                x = random.randint(0, background_width - w)
                y = random.randint(0, background_height - h)

                new_rect = pygame.Rect(x, y, w, h)

                if any(new_rect.colliderect(a.rect) for a in self.assets):
                    continue

                temp_sprite.pos = pygame.math.Vector2(x, y)
                temp_sprite.rect = new_rect
                self.assets.append(temp_sprite)
                break


    def onExit(self):
        pass

    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s
    
        self.ctx.screen.blit(self.ctx.images["foraging_background.png"])
    
        menu = pygame.Surface((self.ctx.w,self.ctx.h))
    
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*0,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*1,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*2,400,150),0,40)

        self.ctx.screen.blit(menu)    
        self.ctx.screen.blit(menu)
