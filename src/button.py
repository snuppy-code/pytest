import pygame

from src.util import get_mouse_pos

class Button:
    def __init__(self,ctx,pos_tuple,image_surface_normal,image_surface_hover,image_surface_selected,image_surface_disabled=None,collider_rect=None):
        
        self.image_states = {
            "normal": image_surface_normal,
            "hover": image_surface_hover,
            "selected": image_surface_selected,
        }
        assert (image_surface_normal.get_width(),image_surface_normal.get_height()) == (image_surface_hover.get_width(),image_surface_hover.get_height())
        assert (image_surface_hover.get_width(),image_surface_hover.get_height()) == (image_surface_selected.get_width(),image_surface_selected.get_height())
        if not (image_surface_disabled is None):
            self.image_states["disabled"] = image_surface_disabled
            assert (image_surface_selected.get_width(),image_surface_selected.get_height()) == (image_surface_disabled.get_width(),image_surface_disabled.get_height())

        if collider_rect is None:
            self.collider_rect = pygame.Rect(pos_tuple,image_surface_normal.get_size())
        else:
            self.collider_rect = collider_rect


        self.pos = pos_tuple
        self.state = "normal"
        self.ctx = ctx

    def tick_just_pressed(self):
        if self.state == "disabled":
            return False
        
        mousepos = get_mouse_pos(self.ctx)
        # print(mousepos)
        self.state = "normal"
        if self.collider_rect.collidepoint(mousepos):
            self.state = "hover"
            # print("Hovering!")
            if pygame.mouse.get_pressed()[0]:
                self.state = "selected"
            if pygame.mouse.get_just_released()[0]:
                self.state = "normal"
                return True
            
        return False

    def draw_to(self,surface):
        surface.blit(self.image_states[self.state],dest=self.pos)

    def disable_button(self):
        self.state = "disabled"
    
    def enable_button(self):
        self.state = "normal"