import pygame

from src.button import Button


class MainMenu:
    def __init__(self,ctx):
        self.ctx = ctx

        self.continueButton = Button(
            (186,83),
            self.ctx.images["mainmenu_newgame_normal.png"],
            self.ctx.images["mainmenu_newgame_hover.png"],
            self.ctx.images["mainmenu_newgame_select.png"],
            self.ctx.images["mainmenu_newgame_disabled.png"],
        )
    
    def onEnter(self):
        pass

    def onExit(self):
        pass
    
    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s

        self.ctx.vscreen.blit(self.ctx.images["mainmenu_background.png"])
        
        been_pressed = self.continueButton.tick_just_pressed(events)

        self.ctx.vscreen.blit(self.ctx.images["mainmenu_newgame_normal.png"],dest=(186,83))
        self.ctx.vscreen.blit(self.ctx.images["mainmenu_continue_normal.png"],dest=(186,175))

        # menu = pygame.Surface((self.ctx.w,self.ctx.h))
        
        # pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*0,400,150),0,40)
        # pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*1,400,150),0,40)
        # pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*2,400,150),0,40)
        
        # self.ctx.vscreen.blit(menu)
        
        