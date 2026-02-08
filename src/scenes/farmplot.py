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
        self.holding_bag = None

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onFrame(self, events):
        self.ctx.vscreen.blit(self.ctx.images["farmplot.png"])

        self.ctx.font.draw(str(self.ctx.player.inventory.potato_grown),415,240)
        self.ctx.font.draw(str(self.ctx.player.inventory.daikon_grown),492,240)
        self.ctx.font.draw(str(self.ctx.player.inventory.blueberry_grown),571,240)

        if not (self.holding_bag is None):
            self.ctx.vscreen.blit(self.ctx.images["potato_seedbag.png"])
            self.ctx.vscreen.blit(self.ctx.images["daikon_seedbag.png"])
            self.ctx.vscreen.blit(self.ctx.images["blueberry_seedbag.png"])

        mouse_over_bag = self.get_bag_mouse_over()
        if not (mouse_over_bag is None):
            if pygame.mouse.get_pressed()[0]:
                print("grab bag "+str(mouse_over_bag))

    def alwaysTick(self, events):
        pass
    
    def get_bag_mouse_over(self):
        mousepos = get_mouse_pos(self.ctx)
        mx, my = mousepos[0], mousepos[1]

        if not (40 <= my <= 113):
            return None

        x_bounds = [(409, 473), (482, 548), (552, 616)]
        
        for index, (low, high) in enumerate(x_bounds):
            if low <= mx <= high:
                return index  # 0, 1, eller 2 for the bag
        
        return None

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

# class Tile:
#     def __init__(self):
#         contained = 
#         self.image_sprout = image_sprout
#         self.image_medium = image_medium
#         self.image_grown = image_grown


# class PotatoGrowing:
    
#     @staticmethod
#     def draw_at():
        
    
# class DaikonGrowing:
    
# class BlueberryGrowing:


# '''

# '''