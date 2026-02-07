import pygame
import pygame_gui # type: ignore

class Camp:
    def __init__(self,ctx):
        self.ctx = ctx

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s
    
    
        # replace with background image 
        self.ctx.screen.fill((195, 176, 165))
    
        menu = pygame.Surface((self.ctx.w,self.ctx.h))
    
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*0,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*1,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*2,400,150),0,40)

        self.ctx.screen.blit(menu)    
        self.ctx.screen.blit(menu)