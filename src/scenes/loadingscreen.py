import pygame

class LoadingScreen:
    def __init__(self,ctx):
        self.ctx = ctx
        
        self.loading_progress = 0
        self.loading_font = pygame.font.SysFont(pygame.font.get_default_font(),50)
        
        # initial variables to get width/height that doesn't change as text changes
        # fixes text jittering during loading
        t = f"Loading progress: {self.loading_progress:.2f}%"
        s = self.loading_font.render(t,True,(255,255,255))
        self.initial_w = s.width
        self.initial_h = s.height
    
    def onEnter(self):
        # Loading is expected to be very short,
        # just draw black screen so we don't flash "loading!" for 1 microsecond
        self.ctx.screen.fill("black")
        self.ctx.audios.load()
        
    def onFrame(self):
        pass
        # w = self.ctx.w
        # h = self.ctx.h
        # dt_s = self.ctx.dt_s
        
        # if self.loading_progress >= 100:
        #     self.ctx.transition_scene_to("MainMenu")
        # else:
        #     self.loading_progress += 60 * self.ctx.dt_s
        
        # self.ctx.screen.fill("black")
        
        # print("LoadingScene onFrame called!")
        
        # t = f"Loading progress: {self.loading_progress:.2f}%"
        # s = self.loading_font.render(t,True,(255,255,255))
        # p = (self.ctx.w/2-self.initial_w/2,self.ctx.h/2-self.initial_h/2)
        # self.ctx.screen.blit(s,p)