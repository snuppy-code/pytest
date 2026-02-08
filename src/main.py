import pygame
successes, failures = pygame.init()
# print(f"Successes: {successes}, Failures: {failures}")

from src.worldobject import World
world = World()
world.run()

pygame.quit()