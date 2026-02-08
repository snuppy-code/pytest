import pygame


class Trader:
    def __init__(self, ctx):
        self.ctx = ctx

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onFrame(self, events):
        self.ctx.vscreen.blit(self.ctx.images["trader_stall.png"])
        self.ctx.font.draw("Press e to exit",10,10,22)

        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
                print("Detected PLAYER pressed E")
                self.ctx.transition_scene_to("Camp")
        
    
    def alwaysTick(self, events):
        pass
