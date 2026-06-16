import pygame


def get_mouse_pos(ctx):
    mousepos = pygame.mouse.get_pos()
    return (
        mousepos[0] / ctx.vscreen_scaling_factor,
        mousepos[1] / ctx.vscreen_scaling_factor,
    )
