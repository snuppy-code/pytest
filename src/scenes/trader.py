import pygame
import random


class Trader:
    def __init__(self, ctx):
        self.ctx = ctx
        self.to_draw = {}

    def onEnter(self):
        blueberry_seed_image = self.ctx.images["blueberry_seedbag.png"]
        money_image = self.ctx.images["blueberry_seedbag.png"]
        potato_image = self.ctx.images["potato_growing_grown.png"]
        daikon_image = self.ctx.images["daikon_growing_grown.png"]

        offer_type = random.randint(1,2)
        amount = 0
        if offer_type == 1:
            amount = random.randint(1, 10)
        else:
            amount = random.randint(1,5)

        if offer_type == 1:
            self.to_draw["blueberry_seedbag.png"] = amount
        else:
            self.to_draw["blueberry_seedbag.png"] = amount

    def onExit(self):
        pass

    def onFrame(self, events):
        self.ctx.vscreen.blit(self.ctx.images["trader_stall.png"])
        self.ctx.font.draw("Press e to exit",10,10,22)

        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
                print("Detected PLAYER pressed E")
                self.ctx.transition_scene_to("Camp")

        for img in self.to_draw:
            self.ctx.vscreen.blit(self.ctx.images[img], dest=(500,200))
        
    
    def alwaysTick(self, events):
        pass
