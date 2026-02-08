import pygame
import random


class Trader:
    def __init__(self, ctx):
        self.ctx = ctx

    def onEnter(self):
        blueberry_seed_image = self.ctx.images["blueberry_seedbag.png"]
        money_image = self.ctx.images["blueberry_seedbag.png"]
        potato_image = self.ctx.images["potato_growing_grown.png"]
        daikon_image = self.ctx.images["daikon_growing_grown.png"]
<<<<<<< Updated upstream
        # camp
=======
>>>>>>> Stashed changes

        offer_type = random.randint(1,2)
        amount = 0
        if offer_type == 1:
            amount = random.randint(1, 10)
        else:
            amount = random.randint(1,5)


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
