import pygame
pygame.init()
from src.worldobject import World
world = World()

# from src.font import Fonts

running = True
while running:
    
    # allow closing the window,,
    # .get gives a list of all events since last call
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # call onFrame callback for each scene
    world.onFrame(events)

    # renders allat to the screen !
    pygame.display.flip()


pygame.quit()