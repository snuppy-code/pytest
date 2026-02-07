import pygame
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu

class World:
    screen = None
    w = 0
    h = 0
    clock = None
    dt_s = 0
    scenes = None
    current_scene = None
    
    @staticmethod
    def init():
        World.screen = pygame.display.set_mode((1280,720))
        World.w = World.screen.get_width()
        World.h = World.screen.get_height()
        World.clock = pygame.time.Clock()
        World.scenes = {
            "LoadingScreen": LoadingScreen(),
            "MainMenu": MainMenu(),
        }
        World.current_scene = "MainMenu"
    
    @staticmethod
    def transition_scene_to(newSceneName):
        World.current_scene = newSceneName
