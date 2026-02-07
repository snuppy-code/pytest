import pygame
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu

class World:
    def __init__(self):
        self.ctx = GameContext(self)
        self.scenes = {
            "LoadingScreen": LoadingScreen(self.ctx),
            "MainMenu": MainMenu(self.ctx),
        }
        self.current_scene = "MainMenu"

class GameContext:
    def __init__(self, world):
        self.world = world
        self.screen = pygame.display.set_mode((1280,720))
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.dt_s = 0
        
    def transition_scene_to(self,newSceneName):
        self.world.current_scene = newSceneName
        self.world.current_scene = "MainMenu"