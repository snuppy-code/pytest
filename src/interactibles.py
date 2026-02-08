import pygame


class LevelInteractibles:
    def __init__(self):
        self.interactibles = []
    
    def add(self,interactible):
        self.interactibles.append(interactible)  
        
    def tick_and_draw(self,ctx,events):
        interact_pressed = False
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
                interact_pressed = True
        
        interacted = False
        for interactible in self.interactibles:
            in_range = interactible.tick()
            
            interactible.draw()
            
            if in_range and interact_pressed and not interacted:
                interactible.interact()
                interacted = True

class Interactible:
    def __init__(self,ctx,reachable_prompt,zone,image=None):
        self.ctx = ctx
        self.image = image
        self.reachable_prompt = reachable_prompt
        self.zone = zone
        self.reachable = False
    
    def tick(self):
        self.is_reachable = self.zone.contains(self.ctx.player.pos)
    
    def interact():
        print("Base interaction, did you mean for your interactible to do nothing when interacted?") # override me .. most of the time

    def draw(self):
        if self.image: # some interactibles don't have an image
            self.ctx.vscreen.blit(self.image,(0,0))
        
        if self.reachable:
            self.ctx.vscreen.blit(self.reachable_prompt,(20,20))

class Zone:
    def contains(self, pos):
        assert False

class RectZone(Zone):
    def __init__(self, zone_rect):
        self.rect = zone_rect
        
    def contains(self, pos):
        return self.rect.collidepoint(pos)

class CircleZone(Zone):
    def __init__(self, center_pos, radius):
        self.center = pygame.Vector2(center_pos)
        self.radius = radius
        
    def contains(self, pos):
        return self.center.distance_to(pos) <= self.radius


class ScenePortal(Interactible):
    def __init__(self,ctx,reachable_prompt,zone,target_scene,image=None):
        super().__init__(ctx,reachable_prompt,zone,image)
        self.target_scene = target_scene
    
    def interact(self):
        self.ctx.transition_scene_to(self.target_scene)
    
class ForageNode(Interactible):
    def __init__(self,ctx,reachable_prompt,zone,image=None):
        super().__init__(ctx,reachable_prompt,zone,image)
        
    def interact(self):
        self.ctx.player.playMinigame("foresting")

# class House(Interactible):
#     def __init__(self,ctx,reachable_prompt,zone,image=None):
#         self.