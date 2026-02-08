import pygame

from src.util import get_mouse_pos


class Farmplot:
    def __init__(self, ctx):
        self.ctx = ctx
        self.slots = {
            "topleft": None, "topmiddle": None, "topright": None,
            "horleft": None, "hormiddle": None, "horright": None,
            "lowleft": None, "lowmiddle": None, "lowright": None,
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
        
        if self.holding_bag is None:
            if pygame.mouse.get_just_pressed()[0]:
                self.holding_bag = self.get_bag_mouse_over()
        else:
            if pygame.mouse.get_just_released()[0]:
                target_tile = self.get_tile_mouse_in()
                if not (target_tile is None):
                    self.try_plant_in(target_tile)
                self.holding_bag = None
        
        original_coords = [
            (410,50),
            (481,50),
            (550,50),
        ]
        maybe_oneheld_coords = original_coords.copy()
        
        if not (self.holding_bag is None):
            maybe_oneheld_coords[self.holding_bag] = get_mouse_pos(self.ctx)
            maybe_oneheld_coords[self.holding_bag] = (
                maybe_oneheld_coords[self.holding_bag][0]-20,
                maybe_oneheld_coords[self.holding_bag][1]-20
            )

        self.ctx.vscreen.blit(self.ctx.images["potato_seedbag.png"],maybe_oneheld_coords[0])
        self.ctx.vscreen.blit(self.ctx.images["daikon_seedbag.png"],maybe_oneheld_coords[1])
        self.ctx.vscreen.blit(self.ctx.images["blueberry_seedbag.png"],maybe_oneheld_coords[2])


    def alwaysTick(self, events):
        for maybe_growth in self.slots:
            if not (maybe_growth is None):
                maybe_growth.tick(self.ctx.dt_s)
                if self.ctx.dt_s > 0.1:
                    print("growth detected abnormally high dt: "+str(self.ctx.dt_s))
    
    def draw_growths(self):
        13,42 x 136,38 x 260,35
        11,128 x 123,129 x 262,130
        14,239 x 128,235 x 259,238
        self.ctx.vscreen.blit()

    def try_plant_in(self,target_tile):
        if self.holding_bag == 0:
            self.try_plant_potato(target_tile)
        elif self.holding_bag == 1:
            self.try_plant_daikon(target_tile)
        elif self.holding_bag == 2:
            self.try_plant_blueberry(target_tile)
        else:
            assert False
    
    def try_plant_potato(self,target_tile):
        there = self.slots[target_tile]
        if there is None:
            self.slots[target_tile] = Growth(
                self.ctx.images["potato_growing_sprout.png"],
                self.ctx.images["potato_growing_medium.png"],
                self.ctx.images["potato_growing_grown.png"])

    def try_plant_daikon(self,target_tile):
        there = self.slots[target_tile]
        if there is None:
            self.slots[target_tile] = Growth(
                self.ctx.images["daikon_growing_sprout.png"],
                self.ctx.images["daikon_growing_medium.png"],
                self.ctx.images["daikon_growing_grown.png"])
            
    def try_plant_blueberry(self,target_tile):
        there = self.slots[target_tile]
        if there is None:
            self.slots[target_tile] = Growth(
                self.ctx.images["blueberry_growing_sprout.png"],
                self.ctx.images["blueberry_growing_medium.png"],
                self.ctx.images["blueberry_growing_grown.png"])
    
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
        mx, my = mousepos[0], mousepos[1]
        
        x_bounds = [(10, 101), (117, 224), (246, 350)]
        y_bounds = [(21, 108), (120, 217), (232, 329)]
        
        cols = ["left", "middle", "right"]
        rows = ["top", "hor", "low"]

        col_idx = next((i for i, (low, high) in enumerate(x_bounds) if low <= mx <= high), None)
        row_idx = next((i for i, (low, high) in enumerate(y_bounds) if low <= my <= high), None)

        if col_idx is not None and row_idx is not None:
            return f"{rows[row_idx]}{cols[col_idx]}"
        
        return None

class Growth:
    def __init__(self, image_sprout, image_medium, image_grown):
        self.image_sprout = image_sprout
        self.image_medium = image_medium
        self.image_grown = image_grown
        
        self.growth_stages = [
            {"range": (0, 160), "image": self.image_sprout},
            {"range": (161, 320), "image": self.image_medium},
            {"range": (321, 480), "image": self.image_grown}
        ]

        self.existed_s = 0
        self.current_image = self.image_sprout

    def tick(self, dt_s):
        self.existed_s += dt_s
        
        for stage in self.growth_stages:
            start, end = stage["range"]
            if start <= self.existed_s <= end:
                self.current_image = stage["image"]
                break
        else:
            if self.existed_s > 480:
                self.current_image = self.image_grown

        return self.current_image