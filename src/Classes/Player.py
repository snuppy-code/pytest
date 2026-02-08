import pygame
from pygame.math import Vector2
from src.constants.vectors import *
from enum import Enum

pygame.init()

class AnimationHelper:
    _members_list = None

    def next(self):
        if not self.__class__._members_list:
            self.__class__._members_list = list(self.__class__)
        
        members = self.__class__._members_list
        index = members.index(self)
        return members[(index + 1) % len(members)]

class WalkDownAnimations(Enum, AnimationHelper):
    WALK_DOWN_1 = "walk_down_1.png"
    WALK_DOWN_2 = "walk_down_2.png"
    WALK_DOWN_3 = "walk_down_3.png"
    WALK_DOWN_4 = "walk_down_4.png"

class WalkUpAnimations(Enum):
    WALK_UP_1 = "walk_up_1.png"
    WALK_UP_2 = "walk_up_2.png"
    WALK_UP_3 = "walk_up_3.png"
    WALK_UP_4 = "walk_up_4.png"

class WalkLeftAnimations(Enum):
    WALK_UP_1 = "walk_up_1.png"
    WALK_UP_2 = "walk_up_2.png"
    WALK_UP_3 = "walk_up_3.png"
    WALK_UP_4 = "walk_up_4.png"

class WalkRightAnimations(Enum):
    WALK_UP_1 = "walk_up_1.png"
    WALK_UP_2 = "walk_up_2.png"
    WALK_UP_3 = "walk_up_3.png"
    WALK_UP_4 = "walk_up_4.png"

class WalkUpRightAnimations(Enum):
    WALK_UP_1 = "walk_up_1.png"
    WALK_UP_2 = "walk_up_2.png"
    WALK_UP_3 = "walk_up_3.png"
    WALK_UP_4 = "walk_up_4.png"

class WalkUpLeftAnimations(Enum):
    WALK_UP_1 = "walk_up_1.png"
    WALK_UP_2 = "walk_up_2.png"
    WALK_UP_3 = "walk_up_3.png"
    WALK_UP_4 = "walk_up_4.png"

class WalkDownRightAnimations(Enum):
    WALK_UP_1 = "walk_up_1.png"
    WALK_UP_2 = "walk_up_2.png"
    WALK_UP_3 = "walk_up_3.png"
    WALK_UP_4 = "walk_up_4.png"

class WalkDownLeftAnimations(Enum):
    WALK_UP_1 = "walk_up_1.png"
    WALK_UP_2 = "walk_up_2.png"
    WALK_UP_3 = "walk_up_3.png"
    WALK_UP_4 = "walk_up_4.png"

class IdleAnimation(Enum, AnimationHelper):
    IDLE = "idle.png"

class Player: 
    def __init__(self,ctx,startpos_vector2):
        self.pos = startpos_vector2
        self.inventory = {}
        self.health = 100
        self.ctx = ctx
        self.prev_animation_class = IdleAnimation
        self.animation_class = IdleAnimation
        self.locked = False
        self.fps = 10
        self.tick = 0
        self.t0 = 0
        self.dt = 1 / self.fps
        self.current_frame = "idle.png"
        

        self.animations = {
            "up": WalkUpAnimations,
            "down": WalkDownAnimations,
            "left": WalkLeftAnimations,
            "right": WalkRightAnimations,
            "upleft": WalkUpLeftAnimations,
            "upright": WalkUpRightAnimations,
            "downleft": WalkDownLeftAnimations,
            "downright": WalkDownRightAnimations,
            "idle": IdleAnimation
        }
    
    def teleport(self, toPos):
        self.pos = toPos

    def draw_to(self,surface):
        self.ctx.images[anim]
        pygame.draw.circle(surface,"red",self.pos+self.ctx.player.pos*-0.5,20)

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False    

    def animate(self):
        if (self.tick - self.t0) >= self.dt:
            self.current_frame = self.animation_class.next().value
            self.draw_to(self.ctx.vscreen)
        
    def update(self, events):
        keys = pygame.key.get_pressed()
                    
        facing_vec = Vector2(0,0)
        
        if keys[pygame.K_w]:
            facing_vec += UP

        if keys[pygame.K_a]:
            facing_vec += LEFT

        if keys[pygame.K_s]:
            facing_vec += DOWN

        if keys[pygame.K_d]:
            facing_vec += RIGHT

        if facing_vec.length_squared() < 0.001:
            self.animation_class = self.animations["idle"]
        else:
            facing_vec = facing_vec.normalize()

        directions = {
            "up": facing_vec.dot(UP),
            "down": facing_vec.dot(DOWN),
            "left": facing_vec.dot(LEFT),
            "right": facing_vec.dot(RIGHT),
            "upleft": facing_vec.dot((UP + LEFT).normalize()),
            "upright": facing_vec.dot((UP + RIGHT).normalize()),
            "downleft": facing_vec.dot((DOWN + LEFT).normalize()),
            "downright": facing_vec.dot((DOWN + RIGHT).normalize())
        }

        look_dir = max(directions, key=directions.get)
        self.animation_class = self.animations[look_dir]

        
        self.animate()
        self.pos += (facing_vec * 200) * self.ctx.dt_s
        self.tick += self.ctx.dt_s
            
        