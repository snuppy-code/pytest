import pygame
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu
from src.scenes.test_scene import TestScene
from src.audio import Audios

class World:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280,720))
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        
        self.clock = pygame.time.Clock()
        self.dt_s = 0
        self.day_night_clock = 0 # seconds
        
        self.audios = Audios

        # {string: surface}
        # initialized as {string: None} and filled in after, so I dont have to write the same path twice on one line
        self.images = {
            "mainmenu_background.png": None,
            
            "mainmenu_newgame_normal.png": None,
            "mainmenu_newgame_hover.png": None,
            "mainmenu_newgame_selected.png": None,

            "mainmenu_continue_normal.png": None,
            "mainmenu_continue_hover.png": None,
            "mainmenu_continue_selected.png": None,
        }
        for path in self.images:
            self.images[path] = pygame.image.load(path)
        
        self.scenes = {
            "LoadingScreen": LoadingScreen(self),
            "MainMenu": MainMenu(self),
            "TestScene": TestScene(self)
        }
        self.current_scene = "MainMenu"

    def get_time(self) -> str:
        real_seconds_passed = self.day_night_clock
        
        game_hours_passed = (4/75) * real_seconds_passed + 8
        game_minutes_passed = int((game_hours_passed - int(game_hours_passed)) * 60)
        game_hours_passed = int(game_hours_passed)

        return str(game_hours_passed) + ":" + str(game_minutes_passed)

    
    def run(self):
        running = True
        while running:
            self.onFrame()

    def onFrame(self):
        self.dt_s = self.clock.tick(30) / 1000
        self.day_night_clock += self.dt_s

        # .get gives a list of all events since last call
        events = pygame.event.get()
        for event in events:
            # allow closing the window,,
            if event.type == pygame.QUIT:
                running = False

        self.scenes[self.current_scene].onFrame(events)

        # renders allat to the screen !
        pygame.display.flip()
    
    def transition_scene_to(self,newSceneName):
        self.scenes[self.current_scene].onExit()
        self.current_scene = newSceneName
        self.scenes[self.current_scene].onEnter()