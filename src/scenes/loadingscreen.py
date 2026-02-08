import pygame
import pygame
from src.audio import Audios

class LoadingScreen:
    def __init__(self,ctx):
        self.ctx = ctx
        print("Loadingscreen init")
        
        # self.loading_progress = 0
        # self.loading_font = pygame.font.SysFont(pygame.font.get_default_font(),50)
        
        # # initial variables to get width/height that doesn't change as text changes
        # # fixes text jittering during loading
        # t = f"Loading progress: {self.loading_progress:.2f}%"
        # s = self.loading_font.render(t,True,(255,255,255))
        # self.initial_w = s.widthygame_shaders
        # self.initial_h = s.height
    
    def onEnter(self):
        print("entered loadingscreen")
        # Loading is expected to be very short,
        # just draw black screen so we don't flash "loading!" for 1 microsecond
        self.ctx.vscreen.fill("black")
        
        # load audio
        self.ctx.audios = Audios

        # load all images - designed for 640x360 canvas
        # {string: surface}
        self.ctx.images = {
            "mainmenu_background.png": pygame.image.load("assets/images/mainmenu_background.png"),
            
            "mainmenu_newgame_normal.png": pygame.image.load("assets/images/mainmenu_newgame_normal.png"),
            "mainmenu_newgame_hover.png": pygame.image.load("assets/images/mainmenu_newgame_hover.png"),
            "mainmenu_newgame_selected.png": pygame.image.load("assets/images/mainmenu_newgame_selected.png"),
            "mainmenu_newgame_disabled.png": pygame.image.load("assets/images/mainmenu_newgame_disabled.png"),

            "mainmenu_continue_normal.png": pygame.image.load("assets/images/mainmenu_continue_normal.png"),
            "mainmenu_continue_hover.png": pygame.image.load("assets/images/mainmenu_continue_hover.png"),
            "mainmenu_continue_selected.png": pygame.image.load("assets/images/mainmenu_continue_selected.png"),
            "mainmenu_continue_disabled.png": pygame.image.load("assets/images/mainmenu_continue_disabled.png"),
            
            "camp_background.png": pygame.image.load("assets/images/camp_background.png"),
            
            "press_f_to_go_to_farm_plot.png": pygame.image.load("assets/images/press_f_to_go_to_farm_plot.png"),
            "press_f_to_go_to_the_wilds.png": pygame.image.load("assets/images/press_f_to_go_to_the_wilds.png"),
            "press_f_to_talk_with_trader.png": pygame.image.load("assets/images/press_f_to_talk_with_trader.png"),
            
            "farmplot.png": pygame.image.load("assets/images/farmplot.png"),
            "foraging_map.png": pygame.image.load("assets/images/foraging_map.png"),
            
            "bush_sprite_foraging.png": pygame.image.load("assets/images/bush_sprite_foraging.png").convert_alpha(),
            
            "potato_growing_sprout.png": pygame.image.load("assets/images/potato_growing_sprout.png"),
            "potato_growing_medium.png": pygame.image.load("assets/images/potato_growing_medium.png"),
            "potato_growing_grown.png": pygame.image.load("assets/images/potato_growing_grown.png"),
            "potato_seedbag.png": pygame.image.load("assets/images/potato_seedbag.png"),
            "potato_bush.png": pygame.image.load("assets/images/potato_bush.png"),
            
            "daikon_growing_sprout.png": pygame.image.load("assets/images/daikon_growing_sprout.png"),
            "daikon_growing_medium.png": pygame.image.load("assets/images/daikon_growing_medium.png"),
            "daikon_growing_grown.png": pygame.image.load("assets/images/daikon_growing_grown.png"),
            "daikon_seedbag.png": pygame.image.load("assets/images/daikon_seedbag.png"),
            "daikon_bush.png": pygame.image.load("assets/images/daikon_bush.png"),
            
            "blueberry_growing_sprout.png": pygame.image.load("assets/images/blueberry_growing_sprout.png"),
            "blueberry_growing_medium.png": pygame.image.load("assets/images/blueberry_growing_medium.png"),
            "blueberry_growing_grown.png": pygame.image.load("assets/images/blueberry_growing_grown.png"),
            "blueberry_seedbag.png": pygame.image.load("assets/images/blueberry_seedbag.png"),
            "blueberry_bush.png": pygame.image.load("assets/images/blueberry_bush.png"),

            "trader_stall.png": pygame.image.load("assets/images/trader_stall.png"),
            
            "walk_down_1.png": pygame.image.load("assets/sprites/walk_down_1.png").convert_alpha(),
            "walk_down_2.png": pygame.image.load("assets/sprites/walk_down_2.png").convert_alpha(),
            "walk_down_3.png": pygame.image.load("assets/sprites/walk_down_3.png").convert_alpha(),
            "walk_down_4.png": pygame.image.load("assets/sprites/walk_down_4.png").convert_alpha(),

            "walk_left_1.png": pygame.image.load("assets/sprites/walk_left_1.png").convert_alpha(),
            "walk_left_2.png": pygame.image.load("assets/sprites/walk_left_2.png").convert_alpha(),
            "walk_left_3.png": pygame.image.load("assets/sprites/walk_left_3.png").convert_alpha(),
            "walk_left_4.png": pygame.image.load("assets/sprites/walk_left_4.png").convert_alpha(),

            "walk_right_1.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_left_1.png").convert_alpha(), True, False),
            "walk_right_2.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_left_2.png").convert_alpha(), True, False),
            "walk_right_3.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_left_3.png").convert_alpha(), True, False),
            "walk_right_4.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_left_4.png").convert_alpha(), True, False),

            "walk_up_1.png": pygame.image.load("assets/sprites/walk_up_1.png").convert_alpha(),
            "walk_up_2.png": pygame.image.load("assets/sprites/walk_up_2.png").convert_alpha(),
            "walk_up_3.png": pygame.image.load("assets/sprites/walk_up_3.png").convert_alpha(),
            "walk_up_4.png": pygame.image.load("assets/sprites/walk_up_4.png").convert_alpha(),

            "walk_down_right_1.png": pygame.image.load("assets/sprites/walk_down_right_1.png").convert_alpha(),
            "walk_down_right_2.png": pygame.image.load("assets/sprites/walk_down_right_2.png").convert_alpha(),
            "walk_down_right_3.png": pygame.image.load("assets/sprites/walk_down_right_3.png").convert_alpha(),
            "walk_down_right_4.png": pygame.image.load("assets/sprites/walk_down_right_4.png").convert_alpha(),

            "walk_down_left_1.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_down_right_1.png").convert_alpha(), True, False),
            "walk_down_left_2.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_down_right_2.png").convert_alpha(), True, False),
            "walk_down_left_3.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_down_right_3.png").convert_alpha(), True, False),
            "walk_down_left_4.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_down_right_4.png").convert_alpha(), True, False),

            "walk_up_right_1.png": pygame.image.load("assets/sprites/walk_up_right_1.png").convert_alpha(),
            "walk_up_right_2.png": pygame.image.load("assets/sprites/walk_up_right_2.png").convert_alpha(),
            "walk_up_right_3.png": pygame.image.load("assets/sprites/walk_up_right_3.png").convert_alpha(),
            "walk_up_right_4.png": pygame.image.load("assets/sprites/walk_up_right_4.png").convert_alpha(),

            "walk_up_left_1.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_up_right_1.png").convert_alpha(), True, False),
            "walk_up_left_2.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_up_right_2.png").convert_alpha(), True, False),
            "walk_up_left_3.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_up_right_3.png").convert_alpha(), True, False),
            "walk_up_left_4.png": pygame.transform.flip(pygame.image.load("assets/sprites/walk_up_right_4.png").convert_alpha(), True, False),

            "idle.png": pygame.image.load("assets/sprites/idle.png").convert_alpha()
        }
        print("loaded EVERYTHING !")

        self.ctx.transition_scene_to("MainMenu")

    def onExit(self):
        pass

    def onFrame(self,events):
        pass
        # w = self.ctx.w
        # h = self.ctx.h
        # dt_s = self.ctx.dt_s
        
        # if self.loading_progress >= 100:
        #     self.ctx.transition_scene_to("MainMenu")
        # else:
        #     self.loading_progress += 60 * self.ctx.dt_s
        
        # self.ctx.vscreen.fill("black")
        
        # print("LoadingScene onFrame called!")
        
        # t = f"Loading progress: {self.loading_progress:.2f}%"
        # s = self.loading_font.render(t,True,(255,255,255))
        # p = (self.ctx.w/2-self.initial_w/2,self.ctx.h/2-self.initial_h/2)
        # self.ctx.vscreen.blit(s,p)
    
    def alwaysTick(self, events):
        pass