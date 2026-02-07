import pygame
import pygame_gui

class TestScene:
    def __init__(self,ctx):
        self.ctx = ctx
        self.once = True
        
    def onFrame(self, events):
        # replace with background image 
        self.ctx.screen.fill((195, 176, 165))
        
        if self.once:
            self.once = False
            self.ctx.audios.PLING.play()

    def onEnter(self):
        pass

    def onExit(self):
        pass