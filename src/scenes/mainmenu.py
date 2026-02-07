import pygame
from src.worldobject import World

class MainMenu:
    def __init__(self):
        pass
        
    def onFrame(self):
        # replace with background image 
        World.screen.fill((195, 176, 165))
        
        menu = pygame.Surface((World.w,World.h))
        
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(World.w/2-400/2,60+(150+20)*0,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(World.w/2-400/2,60+(150+20)*1,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(World.w/2-400/2,60+(150+20)*2,400,150),0,40)
        
        World.screen.blit(menu)