import pygame

from src.Classes.Player import Player
from src.interactibles import *

class Camp:
    def __init__(self,ctx):
        self.ctx = ctx
        
        self.ctx.player = Player(ctx,pygame.Vector2(640,360))
        
        self.interactibles = LevelInteractibles()
        self.interactibles.add(ScenePortal(
            ctx=ctx,
            reachable_prompt=ctx.images["press_f_to_go_to_farm_plot.png"],
            zone=RectZone(pygame.Rect(0,0,400,300)),
            target_scene="FarmPlot",
        ))
        self.interactibles.add(ScenePortal(
            ctx=ctx,
            reachable_prompt=ctx.images["press_f_to_go_to_the_wilds.png"],
            zone=RectZone(pygame.Rect(800,500,400,300)),
            target_scene="TheWilds",
        ))
        demo_surface = pygame.Surface((300,300))
        demo_surface.fill("red")
        self.interactibles.add(ScenePortal(
            ctx=ctx,
            reachable_prompt=ctx.images["press_f_to_talk_with_trader.png"],
            zone=RectZone(pygame.Rect(200,400,300,300)),
            image=demo_surface,
            target_scene="Trader",
        ))

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s
        
        self.ctx.vscreen.blit(self.ctx.images["camp_background.png"],self.ctx.player.pos*-0.5)

        self.tick_and_draw(self.ctx,events)
        
        self.ctx.player.update(events)
        self.ctx.player.draw()