import pygame

from src.Player import Player
from src.interactibles import *

class Camp:
    def __init__(self,ctx):
        self.ctx = ctx
        self.interactibles = LevelInteractibles()

    def onEnter(self):

        demo_surface1 = pygame.Surface((360,217),pygame.SRCALPHA)
        demo_surface1.fill((255,0,0,100))
        self.interactibles.add(ScenePortal(
            ctx=self.ctx,
            reachable_prompt=self.ctx.font.render("Press f to view farm plot",15),
            zone=RectZone(pygame.Rect(20,29,360,217)),
            image=demo_surface1,
            pos=pygame.Vector2(20,29),
            target_scene="Farmplot",
        ))
        demo_surface2 = pygame.Surface((125,65),pygame.SRCALPHA)
        demo_surface2.fill((0,255,0,100))
        self.interactibles.add(House(
            ctx=self.ctx,
            reachable_prompt=self.ctx.font.render("Press f to go to sleep",15),
            zone=RectZone(pygame.Rect(820,142,125,65)),
            image=demo_surface2,
            pos=pygame.Vector2(820,142),
        ))
        demo_surface3 = pygame.Surface((218,236),pygame.SRCALPHA)
        demo_surface3.fill((0,0,255,100))
        self.interactibles.add(ScenePortal(
            ctx=self.ctx,
            reachable_prompt=self.ctx.font.render("Press f to go into the wilds",15),
            zone=RectZone(pygame.Rect(1062,484,218,236)),
            image=demo_surface3,
            pos=pygame.Vector2(1062,484),
            target_scene="Foraging",
        ))
        demo_surface4 = pygame.Surface((200,200),pygame.SRCALPHA)
        demo_surface4.fill((0,180,180,100))
        self.interactibles.add(ScenePortal(
            ctx=self.ctx,
            reachable_prompt=self.ctx.font.render("Press f to talk with the trader",15),
            zone=RectZone(pygame.Rect(238,472,200,200)),
            image=demo_surface4,
            pos=pygame.Vector2(238,472),
            target_scene="Trader",
        ))
        self.bounds = RectZone(self.ctx.images["camp_background.png"].get_rect())
        self.ctx.player = Player(self.ctx,pygame.Vector2(640,360))

    def onExit(self):
        pass

    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s
        
        self.ctx.vscreen.blit(self.ctx.images["camp_background.png"],self.ctx.player.pos*-0.5)
        
        self.ctx.player.update(events)
        self.ctx.player.draw()

        self.interactibles.tick_and_draw(self.ctx,events)
    
    def alwaysTick(self, events):
        pass