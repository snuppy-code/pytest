import pygame
from src.worldobject import World

class LoadingScreen:
    def __init__(self):
        self.loading_progress = 0
        self.loading_font = pygame.font.SysFont(pygame.font.get_default_font(),50)
        
        # initial variables to get width/height that doesn't change as text changes
        # fixes text jittering during loading
        t = f"Loading progress: {self.loading_progress:.2f}%"
        s = self.loading_font.render(t,True,(255,255,255))
        self.initial_w = s.width
        self.initial_h = s.height
        
        
    def onFrame(self):
        if self.loading_progress >= 100:
            World.transition_scene_to("MainMenu")
        else:
            self.loading_progress += 60 * World.dt_s
        
        World.screen.fill("black")
        
        print("LoadingScene onFrame called!")
        
        t = f"Loading progress: {self.loading_progress:.2f}%"
        s = self.loading_font.render(t,True,(255,255,255))
        p = (World.w/2-self.initial_w/2,World.h/2-self.initial_h/2)
        World.screen.blit(s,p)