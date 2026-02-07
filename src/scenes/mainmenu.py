import pygame
from src.button import Button

class MainMenu:
    def __init__(self,ctx):
        self.ctx = ctx
    
    def onEnter(self):
        self.newgameButton = Button(
            self.ctx,
            (186,83),
            self.ctx.images["mainmenu_newgame_normal.png"],
            self.ctx.images["mainmenu_newgame_hover.png"],
            self.ctx.images["mainmenu_newgame_selected.png"],
        )
        self.continueButton = Button(
            self.ctx,
            (186,175),
            self.ctx.images["mainmenu_continue_normal.png"],
            self.ctx.images["mainmenu_continue_hover.png"],
            self.ctx.images["mainmenu_continue_selected.png"],
            self.ctx.images["mainmenu_continue_disabled.png"],
        )

    def onExit(self):
        pass
    
    def onFrame(self,events):
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s
        self.ctx.vscreen.blit(self.ctx.images["mainmenu_background.png"])
        
        continue_pressed = self.continueButton.tick_just_pressed(events)
        newgame_pressed = self.newgameButton.tick_just_pressed(events)
        self.continueButton.draw_to(self.ctx.vscreen)
        self.newgameButton.draw_to(self.ctx.vscreen)

        # menu = pygame.Surface((self.ctx.w,self.ctx.h))
        
        # pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*0,400,150),0,40)
        # pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*1,400,150),0,40)
        # pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*2,400,150),0,40)
        
        # self.ctx.vscreen.blit(menu)
        
        