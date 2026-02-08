import pygame

class FadeBlackManager():
    HOLD_TIME = 0.05 

    def __init__(self, ctx):
        self.ctx = ctx
        self.running = False
        self.blackscreen = pygame.Surface((ctx.w, ctx.h), pygame.SRCALPHA)
        self.fadedtoblack = False
        self.elapsed_time = 0
        self.fadeout_time = 0
        self.fadetotal_time = 0

    def world_tick_draw(self):
        if not self.running:
            return

        self.elapsed_time += self.ctx.dt_s
        
        #turn black
        if self.elapsed_time < self.fadeout_time:
            progress = self.elapsed_time / self.fadeout_time
            alpha = int(progress * 255)
            self.fadedtoblack = False
        
        #hold
        elif self.elapsed_time < (self.fadeout_time + self.HOLD_TIME):
            alpha = 255
            self.fadedtoblack = True
            
        elif self.elapsed_time < self.fadetotal_time:
            time_into_fadein = self.elapsed_time - (self.fadeout_time + self.HOLD_TIME)
            progress = time_into_fadein / self.fadeout_time
            alpha = int((1 - progress) * 255)
            self.fadedtoblack = False
            
        # cleanup
        else:
            self.running = False
            alpha = 0
            self.fadedtoblack = False
            self.blackscreen.fill((0, 0, 0, 0))

        if self.running:
            self.blackscreen.fill((0, 0, 0, alpha))
            self.ctx.vscreen.blit(self.blackscreen)

    def request_fadeoutin(self, fadeout_time):
        self.running = True
        self.elapsed_time = 0
        self.fadeout_time = fadeout_time
        # total time = (fade out) + (hold) + (fade in)
        self.fadetotal_time = (fadeout_time * 2) + self.HOLD_TIME
    
    def faded_to_black(self):
        return self.fadedtoblack