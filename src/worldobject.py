import pygame
from src.fadeblack import FadeBlackManager
from src.scenes.camp import Camp
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu
from src.scenes.farmplot import Farmplot
from src.scenes.foraging import Foraging
from src.scenes.trader import Trader
from math import pi, sin

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

        self.transitioning = False
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
            "Foraging": Foraging(self),
            "Farmplot": Farmplot(self),
            "Trader": Trader(self),
        }
        self.current_scene = "LoadingScreen"
        self.scenes[self.current_scene].onEnter()

    def transition_scene_to(self,newSceneName):
        self.nextscene = newSceneName
        print(f"preparing transition from {self.current_scene} to {newSceneName}")
        self.fademanager.request_fadeoutin(0.4)
    
    def _actually_transition_scene(self):
        print(f"actually transitioning from {self.current_scene} to {self.nextscene}")
        self.scenes[self.current_scene].onExit()
        self.current_scene = self.nextscene
        self.nextscene = None
        self.scenes[self.current_scene].onEnter()

    def increment_day_time(self):
        if (self.current_scene != "LoadingScreen") and (self.current_scene != "MainMenu"):
            self.day_night_clock += self.dt_s

    def get_time_str(self) -> str:
        DAY_DURATION_SECONDS = 4 * 60 
        START_TIME = 6 # 6 am
        END_TIME = 22 # 10 pm

        seconds_passed = self.day_night_clock
        
        raw_hours = (4/75) * seconds_passed + START_TIME
        game_hours = int(raw_hours)
        game_minutes = int((raw_hours - game_hours) * 60)

        return f"{game_hours:02d}:{game_minutes:02d}"

    def get_sunlight(self):
        DAY_DURATION_SECONDS = 5 * 60
        START_TIME = 6
        END_TIME = 22
        
        t = ((DAY_DURATION_SECONDS / (END_TIME-START_TIME)) ** -1) * self.day_night_clock + START_TIME
        sunlight_intensity = sin((pi / 24) * t)

        return max(0, sunlight_intensity)

    def draw_night_overlay(self):
        NIGHT_COLOR = (20, 20, 50)
        lighting_overlay = pygame.Surface((self.w, self.h))
        brightness = self.get_sunlight()
        assert brightness >= 0 and brightness <= 1
        alpha = int((1 - brightness) * 200) # not darker than 200 out of 255 alpha for darkening
        print(f"time: {self.get_time_str()}, sunlight: {self.get_sunlight()}, clamped: {brightness}, alpha: {alpha}")

        # 2. Prepare the overlay
        lighting_overlay.set_alpha(alpha)
        lighting_overlay.fill(NIGHT_COLOR)

        # 3. Blit it over the entire screen
        self.vscreen.blit(lighting_overlay, (0, 0))
    
    def run(self):
        print("World started")
        while self.running:
            self.onFrame()

    def onFrame(self):
        # print("World frame!")
        self.dt_s = self.clock.tick(30) / 1000
        
        self.increment_day_time()

        events = pygame.event.get()
        for event in events:
            # allow closing the window,,
            if event.type == pygame.QUIT:
                self.running = False

        self.scenes[self.current_scene].onFrame(events)
        self.fademanager.world_tick_draw()
        if self.fademanager.faded_to_black() and not (self.nextscene is None):
            self._actually_transition_scene()
        
        self.draw_night_overlay()
        # renders allat to the screen !
        pygame.transform.scale(self.vscreen, (self.non_v_w,self.non_v_h), self.screen)
        pygame.display.flip()
