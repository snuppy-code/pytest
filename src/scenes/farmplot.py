import pygame

from src.util import get_mouse_pos


class Farmplot:
    def __init__(self, ctx):
        self.ctx = ctx
        self.slots = {
            "topleft": "empty", "topmiddle": "empty", "topright": "empty",
            "horleft": "empty", "hormiddle": "empty", "horright": "empty",
            "lowleft": "empty", "lowmiddle": "empty", "lowright": "empty",
        }

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onFrame(self, events):
        self.ctx.vscreen.blit(self.ctx.images["farmplot.png"])
        # self.ctx.font.draw("7",30,50)

    def alwaysTick(self, events):
        pass
    
    def get_bag_mouse_over():
        pass

    def get_tile_mouse_in(self):
        mousepos = get_mouse_pos(self.ctx)
        mx, my = mousepos.x, mousepos.y
        
        x_bounds = [(10, 101), (117, 224), (246, 350)]
        y_bounds = [(21, 108), (120, 217), (232, 329)]
        
        cols = ["left", "middle", "right"]
        rows = ["top", "hor", "low"]

        col_idx = next((i for i, (low, high) in enumerate(x_bounds) if low <= mx <= high), None)
        row_idx = next((i for i, (low, high) in enumerate(y_bounds) if low <= my <= high), None)

        if col_idx is not None and row_idx is not None:
            return f"{rows[row_idx]}{cols[col_idx]}"
        
        return None

'''

'''