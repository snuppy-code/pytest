import pygame
import pygame
from src.audio import Audios

class LoadingScreen:
    def __init__(self,ctx):
        self.ctx = ctx
        print("Loadingscreen init")
        
        # self.loading_progress = 0
        # self.loading_font = pygame.font.SysFont(pygame.font.get_default_font(),50)
        
        # # initial variables to get width/height that doesn't change as text changes
        # # fixes text jittering during loading
        # t = f"Loading progress: {self.loading_progress:.2f}%"
        # s = self.loading_font.render(t,True,(255,255,255))
        # self.initial_w = s.widthygame_shaders
        # self.initial_h = s.height
    
    def onEnter(self):
        print("entered loadingscreen")
        # Loading is expected to be very short,
        # just draw black screen so we don't flash "loading!" for 1 microsecond
        self.ctx.vscreen.fill("black")
        
        # load audio
        self.ctx.audios = Audios

        # load all images - designed for 640x360 canvas
        # {string: surface}
        self.ctx.images = {
            "mainmenu_background.png": pygame.image.load("assets/images/mainmenu_background.png"),
            
            "mainmenu_newgame_normal.png": pygame.image.load("assets/images/mainmenu_newgame_normal.png"),
            "mainmenu_newgame_hover.png": pygame.image.load("assets/images/mainmenu_newgame_hover.png"),
            "mainmenu_newgame_selected.png": pygame.image.load("assets/images/mainmenu_newgame_selected.png"),

            "mainmenu_continue_normal.png": pygame.image.load("assets/images/mainmenu_continue_normal.png"),
            "mainmenu_continue_hover.png": pygame.image.load("assets/images/mainmenu_continue_hover.png"),
            "mainmenu_continue_selected.png": pygame.image.load("assets/images/mainmenu_continue_selected.png"),
            "mainmenu_continue_disabled.png": pygame.image.load("assets/images/mainmenu_continue_disabled.png")

            # "foraging_background.png": pygame.image.load("assets/images/foraging_background.png")
            # "potato_bush.png": pygame.image.load("assets/sprites/potato_bush.png").convert_alpha()
            "idle.png": pygame.image.load("assets/sprites/idle.png").convert_alpha(),
            "walk_down_1.png": pygame.image.load("assets/sprites/walk_down_1.png").convert_alpha(),
            "walk_down_2.png": pygame.image.load("assets/sprites/walk_down_2.png").convert_alpha(),
            "walk_down_3.png": pygame.image.load("assets/sprites/walk_down_3.png").convert_alpha(),
            "walk_down_4.png": pygame.image.load("assets/sprites/walk_down_4.png").convert_alpha()
        }

        self.ctx.transition_scene_to("MainMenu")

    def onExit(self):
        pass

    def onFrame(self,events):
        pass
        # w = self.ctx.w
        # h = self.ctx.h
        # dt_s = self.ctx.dt_s
        
        # if self.loading_progress >= 100:
        #     self.ctx.transition_scene_to("MainMenu")
        # else:
        #     self.loading_progress += 60 * self.ctx.dt_s
        
        # self.ctx.vscreen.fill("black")
        
        # print("LoadingScene onFrame called!")
        
        # t = f"Loading progress: {self.loading_progress:.2f}%"
        # s = self.loading_font.render(t,True,(255,255,255))
        # p = (self.ctx.w/2-self.initial_w/2,self.ctx.h/2-self.initial_h/2)
        # self.ctx.vscreen.blit(s,p)