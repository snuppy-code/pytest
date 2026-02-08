import pygame

from src.Classes.Player import Player

class Camp:
    def __init__(self,ctx):
        self.ctx = ctx
        
        self.ctx.player = Player(ctx,pygame.Vector2(640,360))
        
        self.interactibles = Interactibles()

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s
        
        self.ctx.vscreen.blit(self.ctx.images["camp_background.png"],self.ctx.player.pos*-0.5)
        
        self.ctx.player.update(events)
        self.ctx.player.draw_to(self.ctx.vscreen)
        

'''
Interactibles system.
- Transition to another scene (shop,the wilds,farm plot)
- Popup (house- to sleep)
- Harvest minigame
'''
        
class LevelInteractibles:
    def __init__(self,interactibles):
        self.interactibles = interactibles
    
    def tick_all(self):
        for interactible in self.interactibles:
            interactible.tick()


class Harvestable:
    def __init__(self,):
        self.sprite = 
    
    def tick(self):
        pass