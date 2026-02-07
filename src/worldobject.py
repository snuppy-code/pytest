import pygame
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu
from src.scenes.test_scene import TestScene
from src.audio import Audios
from math import pi, sin

class World:
    def __init__(self):
        self.running = True

        self.screen = pygame.display.set_mode((1280,720))
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        
        self.clock = pygame.time.Clock()
        self.dt_s = 0
        self.day_night_clock = 0 # seconds
        
        self.images = None

        self.scenes = {
            "LoadingScreen": LoadingScreen(self),
            "MainMenu": MainMenu(self),
            "TestScene": TestScene(self),
        }
        self.current_scene = "LoadingScreen"
        self.scenes[self.current_scene].onEnter()

    def transition_scene_to(self,newSceneName):
        print(f"transitioning from {self.current_scene} to {newSceneName}")
        self.scenes[self.current_scene].onExit()
        self.current_scene = newSceneName
        self.scenes[self.current_scene].onEnter()
        #todo: maybe add fade in/out of black between scenes here?

    def get_time_str(self) -> str:
        real_seconds_passed = self.day_night_clock
        
        game_hours_passed = (4/75) * real_seconds_passed + 8
        game_minutes_passed = int((game_hours_passed - int(game_hours_passed)) * 60)
        game_hours_passed = int(game_hours_passed)

        return str(game_hours_passed) + ":" + str(game_minutes_passed)

    def get_sunlight(self):
        t = (4/75) * self.day_night_clock + 8
        return max(0, 0.5 * sin((pi/12) * t - (pi/2)) + 0.5)

    
    def run(self):
        print("World started")
        while self.running:
            self.onFrame()

    def onFrame(self):
        print("World frame!")
        self.dt_s = self.clock.tick(30) / 1000
        self.day_night_clock += self.dt_s

        # .get gives a list of all events since last call
        events = pygame.event.get()
        for event in events:
            # allow closing the window,,
            if event.type == pygame.QUIT:
                self.running = False

        self.scenes[self.current_scene].onFrame(events)

        # renders allat to the screen !
        pygame.display.flip()