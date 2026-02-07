import pygame
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu

class World:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.dt_s = 0
        self.scenes = {
            "LoadingScreen": LoadingScreen(self),
            "MainMenu": MainMenu(self),
        }
        self.current_scene = "MainMenu"
        
    def transition_scene_to(self,newSceneName):
        self.current_scene = newSceneName