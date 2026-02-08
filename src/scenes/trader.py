import pygame


class Trader:
    def __init__(self, ctx):
        self.ctx = ctx

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onFrame(self, events):
        
        demo_surface = pygame.Surface((218,236),pygame.SRCALPHA)
        demo_surface.fill((0,0,255,100))