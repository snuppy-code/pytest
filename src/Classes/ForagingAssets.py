import pygame
pygame.init()

sprites_dict = {}

def insertSprites(sprites):
    sprites_dict = sprites

class PotatoBush(pygame.sprite.Sprite):
    def __init__(self, pos=pygame.math.Vector2(0,0)):
        super().__init__()
        self.image = sprites_dict["potato_bush.png"]
        self.rect = self.image.get_rect(topleft=pos)
        self.rarity = "common"

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def forage(self):
        

class Rock:
    def __init__(self, pos=pygame.math.Vector2(0,0)):
        super().__init__()
        self.image = sprites_dict["rock.png"]
        self.rect = self.image.get_rect(topleft=pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)