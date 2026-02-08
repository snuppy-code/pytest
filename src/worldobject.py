import pygame
from src.fadeblack import FadeBlackManager
from src.scenes.camp import Camp
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu
from src.scenes.farmplot import Farmplot
from src.scenes.foraging import Foraging
from math import pi, sin
from src.Player import Player

class World:
    def __init__(self):
        self.running = True

        primary_display_size = pygame.display.get_desktop_sizes()[0]
        vscreen_scaling_factor_x = (primary_display_size[0]//640)
        vscreen_scaling_factor_y = (primary_display_size[1]//360)
        self.vscreen_scaling_factor = min(vscreen_scaling_factor_x,vscreen_scaling_factor_y)

        self.screen = pygame.display.set_mode((640*self.vscreen_scaling_factor, 360*self.vscreen_scaling_factor))
        self.vscreen = pygame.Surface((640,360))
        self.non_v_w = self.screen.get_width()
        self.non_v_h = self.screen.get_height()
        self.w = self.vscreen.get_width()
        self.h = self.vscreen.get_height()


        self.fademanager = FadeBlackManager(self)
        self.clock = pygame.time.Clock()
        self.dt_s = 0
        self.day_night_clock = 0 # seconds
        
        # initialized in loadingscreen
        self.images = None

        self.audios = None
        
        self.scenes = {
            "LoadingScreen": LoadingScreen(self),
            "MainMenu": MainMenu(self),
            "Camp": Camp(self),
            # "Foraging":   (self),
            "Farmplot": Farmplot(self),
        }
        self.current_scene = "LoadingScreen"
        self.scenes[self.current_scene].onEnter()

    def transition_scene_to(self,newSceneName):
        print(f"transitioning from {self.current_scene} to {newSceneName}")
        self.fademanager.request_fadeoutin(1)
        self.scenes[self.current_scene].onExit()
        self.current_scene = newSceneName
        self.scenes[self.current_scene].onEnter()
        #todo: maybe add fade in/out of black between scenes here?

    def get_time_str(self) -> str:
        DAY_DURATION_SECONDS = 5 * 60 
        START_TIME = 6 # 6 am
        END_TIME = 22 # 10 pm

        seconds_passed = self.day_night_clock
        
        raw_hours = (4/75) * seconds_passed + START_TIME
        game_hours = int(raw_hours)
        game_minutes = int((raw_hours - game_hours) * 60)

        return f"{game_hours:02d}:{game_minutes:02d}"

    def get_sunlight(self):
        START_TIME = 6
        
        t = (4/75) * self.day_night_clock + START_TIME
        sunlight_intensity = sin((pi / 24) * t)

        return max(0, sunlight_intensity)

    
    def run(self):
        print("World started")
        while self.running:
            self.onFrame()

    def onFrame(self):
        # print("World frame!")
        self.dt_s = self.clock.tick(30) / 1000
        self.day_night_clock += self.dt_s

        # .get gives a list of all events since last call
        events = pygame.event.get()
        for event in events:
            # allow closing the window,,
            if event.type == pygame.QUIT:
                self.running = False

        self.scenes[self.current_scene].onFrame(events)
        self.fademanager.world_tick_draw()

        # renders allat to the screen !
        pygame.transform.scale(self.vscreen, (self.non_v_w,self.non_v_h), self.screen)
        pygame.display.flip()