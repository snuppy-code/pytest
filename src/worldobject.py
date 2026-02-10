import pygame
from src.Player import Player
from src.fadeblack import FadeBlackManager
from src.scenes.camp import Camp
from src.scenes.loadingscreen import LoadingScreen
from src.scenes.mainmenu import MainMenu
from src.scenes.farmplot import Farmplot
from src.scenes.foraging import Foraging
from src.scenes.trader import Trader
from src.storm import Storm
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

        self.font = Font(self)

        self.transitioning = False
        self.fademanager = FadeBlackManager(self)
        self.clock = pygame.time.Clock()
        self.dt_s = 0
        self.day_night_clock = 0 # seconds
        self.player = None
        self.fonts_to_blit = []
        
        # initialized in loadingscreen
        self.images = None

        self.audios = None

        self.storm = Storm(self)
        
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

        self.player = Player(self,pygame.Vector2(640,360))

    def transition_scene_to(self,newSceneName,reset_time=False):
        self.nextscene = newSceneName
        self.nextscene_resetclock = reset_time
        print(f"preparing transition from {self.current_scene} to {newSceneName}")
        self.fademanager.request_fadeoutin(0.4)
    
    def _actually_transition_scene(self):
        print(f"actually transitioning from {self.current_scene} to {self.nextscene}")
        self.scenes[self.current_scene].onExit()

        if self.current_scene == "Foraging" and self.nextscene == "Camp":
            self.player.teleport(pygame.math.Vector2(1009, 503))
        elif self.current_scene == "Camp" and self.nextscene == "Foraging":
            self.player.teleport(pygame.math.Vector2(66, 195))
        elif self.current_scene == "Farmplot":
            self.player.teleport(pygame.math.Vector2(382, 216))
        elif self.current_scene == "Trader":
            self.player.teleport(pygame.math.Vector2(299, 432))
        elif self.nextscene == "Camp":
            self.player.teleport(pygame.math.Vector2(869, 210))

        self.current_scene = self.nextscene
        if self.nextscene_resetclock:
            self.reset_clock()
            for k,scene in self.scenes.items():
                # print(k,scene)
                scene.alwaysTick(pygame.event.get())
        self.nextscene_resetclock = None
        self.nextscene = None
        self.scenes[self.current_scene].onEnter()

    def increment_day_time(self):
        if (self.current_scene != "LoadingScreen") and (self.current_scene != "MainMenu"):
            self.day_night_clock += self.dt_s

    def get_time_str(self) -> str:
        DAY_DURATION_SECONDS = 4 * 60 
        START_TIME = 6 # 6 am
        END_TIME = 22 # 10 pm
        
        raw_hours = ((DAY_DURATION_SECONDS / (END_TIME-START_TIME)) ** -1) * self.day_night_clock + START_TIME
        game_hours = int(raw_hours)
        game_minutes = int((raw_hours - game_hours) * 60)

        return f"{game_hours:02d}.{game_minutes:02d}"

    def get_sunlight(self):
        DAY_DURATION_SECONDS = 4 * 60
        START_TIME = 6
        END_TIME = 22
        
        t = ((DAY_DURATION_SECONDS / (END_TIME-START_TIME)) ** -1) * self.day_night_clock + START_TIME
        sunlight_intensity = sin((pi / 24) * t)

        return max(0, sunlight_intensity)

    def reset_clock(self):
        self.day_night_clock = 0
        self.dt_s = (self.dt_s + 120)

    def draw_night_overlay(self):
        NIGHT_COLOR = (20, 20, 50)
        lighting_overlay = pygame.Surface((self.w, self.h))
        brightness = self.get_sunlight()
        assert brightness >= 0 and brightness <= 1
        alpha = int((1 - brightness) * 200) # not darker than 200 out of 255 alpha for darkening
        #print(f"time: {self.get_time_str()}, sunlight: {self.get_sunlight()}, clamped: {brightness}, alpha: {alpha}")

        lighting_overlay.set_alpha(alpha)
        lighting_overlay.fill(NIGHT_COLOR)

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
        for k,scene in self.scenes.items():
            # print(k,scene)
            scene.alwaysTick(events)
        
        self.fademanager.world_tick_draw()
        if self.fademanager.faded_to_black() and not (self.nextscene is None):
            self._actually_transition_scene()

        self.storm.update()
        
        self.draw_night_overlay()
        # renders allat to the screen !

        for f in self.fonts_to_blit:
            self.vscreen.blit(f)

        pygame.transform.scale(self.vscreen, (self.non_v_w,self.non_v_h), self.screen)
        pygame.display.flip()
    
class Font:
    def __init__(self,ctx):
        self.ctx = ctx
    
    def render(self,text,size=26):
        font_daydream = pygame.font.Font("assets/fonts/Daydream DEMO.otf",size)
        a = font_daydream.render(text,False,"black")
        b = font_daydream.render(text,False,"white")
        c = pygame.Surface((a.get_width()+2,a.get_height()+2),pygame.SRCALPHA)
        c.blit(a,(2,2))
        c.blit(b,(0,0))
        return c


    def draw(self,text,x,y,size=26):
        font_daydream = pygame.font.Font("assets/fonts/Daydream DEMO.otf",size)
        self.ctx.vscreen.blit(font_daydream.render(text,False,"black"),(x,y))
        self.ctx.vscreen.blit(font_daydream.render(text,False,"white"),(x+2,y+2))

