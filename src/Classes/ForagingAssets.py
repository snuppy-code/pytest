import pygame
from src.interactibles import ForageNode
pygame.init()

sprites_dict = {}
ctx = None

def insertInfo(sprites, incoming_ctx):
    global sprites_dict
    sprites_dict = sprites

    global ctx
    ctx = incoming_ctx


class PotatoBush(pygame.sprite.Sprite):
    def __init__(self, pos=pygame.math.Vector2(0,0)):
        super().__init__()
        self.image = sprites_dict["potato_bush.png"]
        self.rect = self.image.get_rect(topleft=pos)
        self.collision_rect = pygame.Rect(0,0, 10, 10)
        self.collision_rect.center = self.rect.center
        self.node = 

        print(self.collision_rect)
        print(self.rect)
        self.rarity = "common"
        self.harvestable = True

    def draw(self):
        self.collision_rect.topleft = self.pos+ctx.player.pos*-0.8
        ctx.vscreen.blit(self.image, dest=self.pos+ctx.player.pos*-0.8)

    def forage(self):
        pass

class DaikonBush(pygame.sprite.Sprite):
    def __init__(self, pos=pygame.math.Vector2(0,0)):
        super().__init__()
        self.image = sprites_dict["daikon_bush.png"]
        self.rect = self.image.get_rect(topleft=pos)
        self.collision_rect = pygame.Rect(0,0, 10, 10)
        self.collision_rect.center = self.rect.center

        print(self.collision_rect)
        print(self.rect)
        self.rarity = "common"
        self.harvestable = True

    def draw(self):
        self.collision_rect.topleft = self.pos+ctx.player.pos*-0.8
        ctx.vscreen.blit(self.image, dest=self.pos+ctx.player.pos*-0.8)

    def forage(self):
        pass

"""
class Rock:
    def __init__(self, pos=pygame.math.Vector2(0,0)):
        super().__init__()
        self.image = sprites_dict["bush_sprite_foraging.png"]
        self.rect = self.image.get_rect(topleft=pos)
        self.collision_rect = pygame.Rect(0,0, 10, 10)
        self.collision_rect.center = self.rect.center
        self.harvestable = False

    def draw(self):
        ctx.vscreen.blit(self.image, dest=self.pos+ctx.player.pos*-0.8)
        """