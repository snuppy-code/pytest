import pygame

class Button:
    def __init__(self,ctx,pos_tuple,image_surface_normal,image_surface_hover,image_surface_selected,name,image_surface_disabled=None,collider_rect=None):
        
        self.image_states = {
            "normal": image_surface_normal,
            "hover": image_surface_hover,
            "selected": image_surface_selected,
        }
        assert (image_surface_normal.get_width(),image_surface_normal.get_height()) == (image_surface_hover.get_width(),image_surface_hover.get_height())
        assert (image_surface_hover.get_width(),image_surface_hover.get_height()) == (image_surface_selected.get_width(),image_surface_selected.get_height())
        if image_surface_disabled is None:
            self.can_be_disabled = False
        else:
            self.image_states["disabled"] = image_surface_disabled,
            assert (image_surface_selected.get_width(),image_surface_selected.get_height()) == (image_surface_disabled.get_width(),image_surface_disabled.get_height())


        if collider_rect is None:
            self.collider_rect = pygame.Rect(pos_tuple,(pos_tuple[0]+image_surface_normal.get_width(),pos_tuple[1]+image_surface_normal.get_height()))
        else:
            self.collider_rect = collider_rect


        self.pos = pos_tuple
        self.state = "normal"
        self.ctx = ctx

    def tick_just_pressed(self,events):
        if self.state == "disabled":
            return False

        self.state = "normal"
        mousepos = pygame.mouse.get_pos()
        mousepos = (mousepos[0]/self.ctx.vscreen_scaling_factor,mousepos[1]/self.ctx.vscreen_scaling_factor)
        print(mousepos)
        if self.collider_rect.collidepoint(mousepos):
            self.state = "hover"
            print("Hovering!")
            for event in events:
                if event == pygame.MOUSEBUTTONDOWN:
                    self.state = "selected"
                    print("Selected!")
                if event == pygame.MOUSEBUTTONUP:
                    self.state = "normal"
                    print("Pressed!")
                    return True
        return False

    def draw_to(self,surface):
        surface.blit(self.image_states[self.state],dest=self.pos)

    def disable_button(self):
        self.state = "disabled"
    
    def enable_button(self):
        self.state = "normal"