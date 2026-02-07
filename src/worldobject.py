import pygame
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu
from src.audio import Audios

class World:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        
        self.clock = pygame.time.Clock()
        self.dt_s = 0
        
        self.audios = Audios()
        
        self.scenes = {
            "LoadingScreen": LoadingScreen(self),
            "MainMenu": MainMenu(self),
            "TestScene": TestScene(self)
        }
        self.current_scene = "TestScene"
    
    def onFrame(self):
        self.dt_s = self.clock.tick(144) / 1000
        self.scenes[self.current_scene].onFrame()
    
    def transition_scene_to(self,newSceneName):
        self.current_scene = newSceneName