import pygame
pygame.init()
from src.worldobject import World
from src.font import Fonts
World.init()


running = True
while running:
    
    # allow closing the window,,
    # .get gives a list of all events since last call
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # call onFrame callback for each scene
    World.scenes[World.current_scene].onFrame()

    # renders allat to the screen !
    pygame.display.flip()
    World.dt_s = World.clock.tick(144) / 1000
    # print(dt_s)


pygame.quit()