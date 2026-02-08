import pygame


class FadeBlackManager():
    def __init__(self,ctx):
        self.ctx = ctx
        self.running = False
        self.blackscreen = pygame.Surface((ctx.w,ctx.h),pygame.SRCALPHA)
        self.fadedtoblack = False
    
    def world_tick_draw(self):
        if self.running:
            self.elapsed_time += self.ctx.dt_s
            if self.elapsed_time >= self.fadetotal_time:
                self.running = False
                self.elapsed_time = None
                self.fadeout_time = None
                self.fadetotal_time = None
                self.fadedtoblack = False
                self.blackscreen.fill((0,0,0,0))
            elif self.elapsed_time >= self.fadeout_time:
                self.fadedtoblack = True
                self.blackscreen.fill((0,0,0,(1-((self.elapsed_time-self.fadeout_time)/self.fadeout_time))*255))
            else:
                self.blackscreen.fill((0,0,0,self.elapsed_time/self.fadeout_time*255))

            self.ctx.vscreen.blit(self.blackscreen)
    
    def request_fadeoutin(self,fadeout_time):
        self.running = True
        self.elapsed_time = 0
        self.fadeout_time = fadeout_time
        self.fadetotal_time = fadeout_time*2
    
    def faded_to_black(self):
        return self.fadedtoblack