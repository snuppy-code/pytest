import pygame
import random

from src.button import Button


def createbutton(on):
    on.sellButton = Button(
            on.ctx,
            (440,63),
            on.ctx.images["sell_checkmark_normal.png"],
            on.ctx.images["sell_checkmark_hovered.png"],
            on.ctx.images["sell_checkmark_selected.png"],
            on.ctx.images["sell_checkmark_disabled.png"],
            )

class Trader:
    def __init__(self, ctx):
        self.ctx = ctx
        self.give = None
        self.get = None
        self.sellButton = None

    def onEnter(self):
        if self.give is None:
            self.pick_quest()
        
        if self.sellButton is None:
            createbutton(self)

    def pick_quest(self):
        # only request blueberry if player has a few
        player_potential_blueberries = self.ctx.player.inventory.blueberry_grown+self.ctx.player.inventory.blueberry_seed
        if player_potential_blueberries > 4:
            which_you_give = random.randint(1,3)
        else:
            which_you_give = random.randint(1,2)


        if which_you_give == 1: #player gives potato, gets blueberry or money
            how_many_you_give = random.randint(4,17) # max give 17
            self.give = ("potato",how_many_you_give)
            
            what_you_get = random.randint(1,2)
            if what_you_get == 1:
                self.get = ("blueberry", 2)#CHANGETHIS, 2-4, no more, no less, and scaling with how many you give)
            elif what_you_get == 2:
                self.get = ("money", how_many_you_give*random.randint(2,3))
            
        elif which_you_give == 2: #player gives daikon, gets blueberry or money
            how_many_you_give = random.randint(3,10)
            self.give = ("daikon",how_many_you_give)

            what_you_get = random.randint(1,2)
            if what_you_get == 1:
                self.get = ("blueberry", 3)#CHANGETHIS, 3-9, no more, no less, and scaling with how many you give)
            elif what_you_get == 2:
                self.get = ("money", how_many_you_give*random.randint(4,6))
            
        elif which_you_give == 3:
            how_many_you_give = random.randint(3,10)
            self.give = ("blueberry",how_many_you_give)
            self.get = ("money", how_many_you_give*random.randint(8,14))
        
    def onExit(self):
        pass

    def onFrame(self, events):
        self.ctx.vscreen.blit(self.ctx.images["trader_stall.png"])
        self.ctx.font.draw("Press e to exit",10,10,22)

        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
                print("Detected PLAYER pressed E")
                self.ctx.transition_scene_to("Camp")

        if self.give is None:
            self.pick_quest()


        if self.give[0] == "potato":
            self.ctx.vscreen.blit(self.ctx.images["potato_trader.png"], dest=(399,184))
            self.ctx.font.draw(str(self.give[1]),399,184,size=22)

            if self.ctx.player.inventory.potato_grown < self.give[1]:
                self.sellButton.disable_button()
            else:
                self.sellButton.enable_button()

        elif self.give[0] == "daikon":
            self.ctx.vscreen.blit(self.ctx.images["daik_trader.png"], dest=(399,184))
            self.ctx.font.draw(str(self.give[1]),399,184,size=22)

            if self.ctx.player.inventory.daikon_grown < self.give[1]:
                self.sellButton.disable_button()
            else:
                self.sellButton.enable_button()

        elif self.give[0] == "blueberry":
            self.ctx.vscreen.blit(self.ctx.images["blue_trader.png"], dest=(399,184))
            self.ctx.font.draw(str(self.give[1]),399,184,size=22)

            if self.ctx.player.inventory.blueberry_grown < self.give[1]:
                self.sellButton.disable_button()
            else:
                self.sellButton.enable_button()



        if self.get[0] == "blueberry":
            self.ctx.vscreen.blit(self.ctx.images["blueberry_seedbag.png"], dest=(515,187))
            self.ctx.font.draw(str(self.give[1]),515,187,size=22)
        elif self.get[0] == "money":
            self.ctx.vscreen.blit(self.ctx.images["moneybag.png"], dest=(515,187))
            self.ctx.font.draw(str(self.give[1]),515,187,size=22)

        if self.sellButton is None:
            createbutton(self)
        
        sell = self.sellButton.tick_just_pressed()
        self.sellButton.draw_to(self.ctx.vscreen)

        if sell:
            if self.get[0] == "blueberry":
                self.ctx.player.inventory.blueberry_seed += self.get[1]
            elif self.get[0] == "money":
                self.ctx.player.inventory.rouble += self.get[1]
            self.get = None
            self.give = None
            if self.give is None:
                self.pick_quest()

    def alwaysTick(self, events):
        pass