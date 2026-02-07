import pygame

class Button:
    def __init__(self,pos_tuple,image_surface_normal,image_surface_hover,image_surface_select,image_surface_disabled,collider_rect=None):
        assert (image_surface_normal.get_width(),image_surface_normal.get_height()) == (image_surface_hover.get_width(),image_surface_hover.get_height())
        assert (image_surface_hover.get_width(),image_surface_hover.get_height()) == (image_surface_select.get_width(),image_surface_select.get_height())
        assert (image_surface_select.get_width(),image_surface_select.get_height()) == (image_surface_disabled.get_width(),image_surface_disabled.get_height())
        
        if collider_rect is None:
            self.collider_rect = collider_rect
        else:
            self.collider_rect = pygame.Rect(pos_tuple,(pos_tuple[0]+image_surface_normal.get_width(),pos_tuple[1]+image_surface_normal.get_height()))

        self.pos = pos_tuple

        self.image_states = {
            "normal": image_surface_normal,
            "hover": image_surface_hover,
            "select": image_surface_select,
            "disabled": image_surface_disabled,
        }
        self.state = "normal"

    def tick_just_pressed(self,events):
        if self.state == "disabled":
            return False
    
        self.state = "normal"
        if self.collider_rect.collidepoint(pygame.mouse.get_pos()):
            self.state = "hover"
            for event in events:
                if event == pygame.MOUSEBUTTONDOWN:
                    self.state = "select"
                if event == pygame.MOUSEBUTTONUP:
                    self.state = "normal"
                    return True
        return False

    def draw_to(self,surface):
        surface.blit(self.image_states[self.state],dest=self.pos)

    def disable_button(self):
        self.state = "disabled"
    
    def enable_button(self):
        self.state = "normal"