import pygame  # type: ignore
import pygame.gfxdraw

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

dt = 0

a = pygame.Surface((500, 500))

running = True
while running:

    # allow closing the window,,
    # .get gives a list of all events since last call
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    a.fill("red")
    pygame.gfxdraw.bezier(a, ((0, 0), (400, 100), (0, 500)), 2, pygame.Color(0,255,0))
    screen.blit(a)

    # render my game <-- here

    # renders allat to the screen !
    pygame.display.flip()
    clock.tick(144)

pygame.quit()
