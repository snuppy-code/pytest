import pygame
import pygame.math.Vector2 as Vector2
from src.worldobject import World

class Example_RedDotWASD:
    def __init__(self):
        self.player_pos = Vector2(World.w/2,World.h/2)
        
    def onFrame(self):
        World.screen.fill("black")
        pygame.draw.circle(World.screen, "red", self.player_pos, 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos += pygame.Vector2(0,-200) * World.dt_s
        if keys[pygame.K_s]:
            self.player_pos += pygame.Vector2(0,200) * World.dt_s
        if keys[pygame.K_a]:
            self.player_pos += pygame.Vector2(-200,0) * World.dt_s
        if keys[pygame.K_d]:
            self.player_pos += pygame.Vector2(200,0) * World.dt_s

