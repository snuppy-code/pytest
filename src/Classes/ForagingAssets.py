import pygame
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
        self.rarity = "common"
        self.harvestable = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def forage(self):
        

class Rock:
    def __init__(self, pos=pygame.math.Vector2(0,0)):
        super().__init__()
        self.image = sprites_dict["rock.png"]
        self.rect = self.image.get_rect(topleft=pos)
        self.harvestable = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)