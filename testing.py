import pygame # type: ignore

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

dt = 0

player_pos = pygame.Vector2(screen.get_width)

running = True
while running:
    
    # allow closing the window,,
    # .get gives a list of all events since last call
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # render my game <-- here

    # renders allat to the screen !
    pygame.display.flip()
    clock.tick(144)

pygame.quit()