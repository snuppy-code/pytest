import pygame

from src.worldobject import World

successes, failures = pygame.init()
# print(f"Successes: {successes}, Failures: {failures}")

world = World()
world.run()

pygame.quit()
