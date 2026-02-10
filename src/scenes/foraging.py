import pygame
import random
from src.Classes.ForagingAssets import *
from src.audio import Audios
from src.interactibles import *
from src.storm import Storm

class Foraging:
    def __init__(self,ctx):
        self.ctx = ctx
        self.objects_on_screen = []
        self.collidables = []
        self.background_sound = Audios.WILDWIND

        insertInfo(self.ctx.images, self.ctx)

    def onEnter(self):
        print("hi")
        self.portal = ScenePortal(
            ctx=self.ctx,
            reachable_prompt=self.ctx.font.render("Press f to return to camp",15),
            zone=CircleZone((40,160), 200),
            target_scene="Camp"
        )

        # fix this mama
        # you don't want to have rocks and stuff ON THE ROAD!!!!!!
        insertInfo(self.ctx.images, self.ctx)
        self.background_sound.WILDWIND.play(-1)

        choices = [PotatoBush, DaikonBush]
        weights = [1, 1/2]

        background_width, background_height = self.ctx.images["foraging_map.png"].get_size()
        for i in range(20):
            asset_class = random.choices(choices, weights, k=1)[0]
            temp_sprite = asset_class()
            w, h = temp_sprite.image.get_size()

            attempts = 80
            for a in range(attempts):
                x = random.randint(0, background_width - w)
                y = random.randint(0, background_height - h)
                if (x < 200) and (y < 200):
                    continue
                new_rect = pygame.Rect(x, y, w, h)

                if any(new_rect.colliderect(a) for a in self.collidables):
                    continue

                temp_sprite.pos = pygame.math.Vector2(x, y)
                temp_sprite.rect = new_rect
                temp_sprite.node = ForageNode(
                    ctx=self.ctx,
                    reachable_prompt=self.ctx.font.render("Press f to forage",15),
                    zone=CircleZone(temp_sprite.rect.center, 50),
                )
                self.objects_on_screen.append(temp_sprite)
                break
        
        self.bounds = RectZone(self.ctx.images["foraging_map.png"].get_rect())
        self.ctx.player.obj_in_scene = self.objects_on_screen
        self

    def onExit(self):
        self.background_sound.WILDWIND.stop()
        pass

    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s

        self.ctx.vscreen.blit(self.ctx.images["foraging_map.png"], self.ctx.player.pos*-0.8)

        to_keep = [obj for obj in self.objects_on_screen if not getattr(obj, 'to_del', False)]
        self.objects_on_screen = to_keep
        

        for obj in self.objects_on_screen:
            if obj.node.tick():
                self.ctx.player.available_plants.append(obj)
                obj.node.draw()
            
            obj.draw()

        if self.portal.tick():
            self.ctx.player.available_plants.insert(0, self.portal)
            self.portal.draw()
    
        #pygame.draw.rect(self.ctx.vscreen, "red", self.collision_rect)
        self.ctx.player.update(events)
        self.ctx.player.draw()
        self.ctx.storm.draw()

    def alwaysTick(self, events):
        pass
        