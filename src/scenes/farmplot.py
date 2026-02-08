import pygame

from src.button import Button
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
        
        if self.holding_bag is None:
            if pygame.mouse.get_just_pressed()[0]:
                self.holding_bag = self.get_bag_mouse_over()
                trying_to_harvest_tile = self.get_tile_mouse_in()
                if trying_to_harvest_tile is not None:
                    at_tile = self.slots[trying_to_harvest_tile]
                    if at_tile is not None:
                        if at_tile.is_grown():
                            if at_tile.type == "potato":
                                self.ctx.player.inventory.potato_grown += 1
                            elif at_tile.type == "daikon":
                                self.ctx.player.inventory.daikon_grown += 1
                            elif at_tile.type == "blueberry":
                                self.ctx.player.inventory.blueberry_grown += 1
                            self.slots[trying_to_harvest_tile] = None
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

        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
                print("Detected PLAYER pressed E")
                self.ctx.transition_scene_to("Camp")

        self.draw_growths()

        self.ctx.font.draw(str(self.ctx.player.inventory.potato_grown),429,240)
        self.ctx.font.draw(str(self.ctx.player.inventory.daikon_grown),518,240)
        self.ctx.font.draw(str(self.ctx.player.inventory.blueberry_grown),586,240)

        self.ctx.vscreen.blit(self.ctx.images["potato_seedbag.png"],maybe_oneheld_coords[0])
        self.ctx.vscreen.blit(self.ctx.images["daikon_seedbag.png"],maybe_oneheld_coords[1])
        self.ctx.vscreen.blit(self.ctx.images["blueberry_seedbag.png"],maybe_oneheld_coords[2])

        (x0,y0) = maybe_oneheld_coords[0]
        (x1,y1) = maybe_oneheld_coords[1]
        (x2,y2) = maybe_oneheld_coords[2]
        self.ctx.font.draw(str(self.ctx.player.inventory.potato_seed),x0+40,y0+20)
        self.ctx.font.draw(str(self.ctx.player.inventory.daikon_seed),x1+40,y1+20)
        self.ctx.font.draw(str(self.ctx.player.inventory.blueberry_seed),x2+40,y2+20)

        

        self.ctx.font.draw("Press e to exit",10,319,22)

    def alwaysTick(self, events):
        for _,maybe_growth in self.slots.items():
            if not (maybe_growth is None):
                maybe_growth.tick(self.ctx.dt_s)
                if self.ctx.dt_s > 0.1:
                    print("growth detected abnormally high dt: "+str(self.ctx.dt_s))
    
    def draw_growths(self):
        slot_coords = {
            # top
            "topleft": pygame.Vector2(12, 37),
            "topmiddle": pygame.Vector2(132, 38),
            "topright": pygame.Vector2(260, 35),
            
            # hor
            "horleft": pygame.Vector2(11, 128),
            "hormiddle": pygame.Vector2(134, 129),
            "horright": pygame.Vector2(262, 130),
            
            # low
            "lowleft": pygame.Vector2(14, 239),
            "lowmiddle": pygame.Vector2(139, 239),
            "lowright": pygame.Vector2(262, 238)
        }

        for slot_name, position in slot_coords.items():
            growth = self.slots[slot_name]
            if growth is not None:
                self.ctx.vscreen.blit(growth.current_image, position-growth.offset)

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
        if self.ctx.player.inventory.potato_seed > 0:
            there = self.slots[target_tile]
            if there is None:
                self.slots[target_tile] = Growth(
                    self.ctx.images["potato_growing_sprout.png"],
                    self.ctx.images["potato_growing_medium.png"],
                    self.ctx.images["potato_growing_grown.png"],
                    pygame.Vector2(0,14),
                    "potato")
                self.ctx.player.inventory.potato_seed -= 1

    def try_plant_daikon(self,target_tile):
        if self.ctx.player.inventory.daikon_seed > 0:
            there = self.slots[target_tile]
            if there is None:
                self.slots[target_tile] = Growth(
                    self.ctx.images["daikon_growing_sprout.png"],
                    self.ctx.images["daikon_growing_medium.png"],
                    self.ctx.images["daikon_growing_grown.png"],
                    pygame.Vector2(0,55),
                    "daikon")
                self.ctx.player.inventory.daikon_seed -= 1
            
    def try_plant_blueberry(self,target_tile):
        if self.ctx.player.inventory.blueberry_seed > 0:
            there = self.slots[target_tile]
            if there is None:
                self.slots[target_tile] = Growth(
                    self.ctx.images["blueberry_growing_sprout.png"],
                    self.ctx.images["blueberry_growing_medium.png"],
                    self.ctx.images["blueberry_growing_grown.png"],
                    pygame.Vector2(0,49),
                    "blueberry")
                self.ctx.player.inventory.blueberry_seed -= 1
    
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
    def __init__(self, image_sprout, image_medium, image_grown, offset,type):
        self.image_sprout = image_sprout
        self.image_medium = image_medium
        self.image_grown = image_grown
        
        self.type = type
        
        self.offset = offset

        self.growth_stages = [
            {"range": (0, 160), "image": self.image_sprout},
            {"range": (161, 320), "image": self.image_medium},
            {"range": (321, 480), "image": self.image_grown},
            # {"range": (0, 1), "image": self.image_sprout},
            # {"range": (1.1, 2), "image": self.image_medium},
            # {"range": (2.1, 3), "image": self.image_grown}
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
    
    def is_grown(self):
        return self.current_image is self.image_grown