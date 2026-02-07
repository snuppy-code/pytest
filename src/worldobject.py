import pygame
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu
from src.scenes.test_scene import TestScene
from src.audio import Audios
import pygame_gui # type: ignore

class World:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        
        self.gui_manager = pygame_gui.UIManager((self.w, self.h), theme_path="quick_start.json")
        
        self.clock = pygame.time.Clock()
        self.dt_s = 0
        
        self.audios = Audios
        
        self.scenes = {
            "LoadingScreen": LoadingScreen(self),
            "MainMenu": MainMenu(self),
            "TestScene": TestScene(self)
        }
        self.current_scene = "MainMenu"
    
    def run(self):
        running = True
        while running:
            self.onFrame()

    def onFrame(self,events):
        self.dt_s = self.clock.tick(30) / 1000
        self.scenes[self.current_scene].onFrame(events)

        # .get gives a list of all events since last call
        events = pygame.event.get()
        for event in events:
            # allow closing the window,,
            if event.type == pygame.QUIT:
                running = False
            self.gui_manager.process_events(event)
            
        self.gui_manager.update(self.dt_s)
        self.gui_manager.draw_ui(self.screen)

        # renders allat to the screen !
        pygame.display.flip()
    
    def transition_scene_to(self,newSceneName):
        self.scenes[self.current_scene].onExit()
        self.current_scene = newSceneName
        self.scenes[self.current_scene].onEnter()