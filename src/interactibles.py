import pygame


class LevelInteractibles:
    def __init__(self):
        self.interactibles = []
    
    def add(self,interactible):
        self.interactibles.append(interactible)  
        
    def tick_and_draw(self,ctx,events):
        interact_pressed = False
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_f:
                interact_pressed = True
                print("Detected PLAYER pressed F")
        
        interacted = False
        for interactible in self.interactibles:
            in_range = interactible.tick()
            
            interactible.draw()
            
            if in_range and interact_pressed and not interacted:
                interactible.interact()
                interacted = True

class Interactible:
    def __init__(self,ctx,reachable_prompt,zone,image=None,pos=None):
        self.ctx = ctx
        self.image = image
        self.reachable_prompt = reachable_prompt
        self.pos = pos
        self.collider_zone = zone
        self.reachable = False
    
    def tick(self):
        self.reachable = self.collider_zone.contains(self.ctx.player.pos)
        return self.reachable
        # print("Is reachable?: "+self.reachable)
    
    def interact():
        print("Base interaction, did you mean for your interactible to do nothing when interacted?") # override me .. most of the time

    def draw(self):
        if self.image: # some interactibles don't have an image
            # print("Drawing at: "+str(self.pos))
            self.ctx.vscreen.blit(self.image,self.pos+pygame.Vector2(0,0)+self.ctx.player.pos*-0.5)
        
        if self.reachable:
            self.ctx.vscreen.blit(
                self.reachable_prompt,
                pygame.Vector2(
                    self.ctx.w/2-self.reachable_prompt.get_width()/2,
                    self.ctx.h/1.4-self.reachable_prompt.get_height()/2))


class ScenePortal(Interactible):
    def __init__(self,ctx,reachable_prompt,zone,target_scene,image=None,pos=None):
        super().__init__(ctx,reachable_prompt,zone,image,pos)
        self.target_scene = target_scene
    
    def interact(self):
        self.ctx.transition_scene_to(self.target_scene)

class ForageNode(Interactible):
    def __init__(self,ctx,reachable_prompt,zone,image=None,pos=None):
        super().__init__(ctx,reachable_prompt,zone,image,pos)
        
    def interact(self):
        self.ctx.player.playMinigame("foresting")

class House(Interactible):
    def __init__(self,ctx,reachable_prompt,zone,image=None,pos=None):
        super().__init__(ctx,reachable_prompt,zone,image,pos)
    
    def interact(self):
        self.ctx.transition_scene_to("Camp",reset_time=True)


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