import pygame
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu

class World:
    def init(self):
        self.ctx = GameContext()
        self.scenes = {
            "LoadingScreen": LoadingScreen(self.ctx),
            "MainMenu": MainMenu(self.ctx),
        }
        self.current_scene = "MainMenu"

class GameContext:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.dt_s = 0
