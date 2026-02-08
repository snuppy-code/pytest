import pygame
from pygame.math import Vector2
from src.constants.vectors import *
from enum import Enum
from src.audio import Audios

pygame.init()

class AnimationHelper:
    _members_list = None

    def next(self):
        if not self.__class__._members_list:
            self.__class__._members_list = list(self.__class__)
        
        members = self.__class__._members_list
        index = members.index(self)
        print(self)
        print(members)
        print(index)
        return members[(index + 1) % len(members)]

class WalkDownAnimations(AnimationHelper, Enum):
    WALK_DOWN_1 = "walk_down_1.png"
    WALK_DOWN_2 = "walk_down_2.png"
    WALK_DOWN_3 = "walk_down_3.png"
    WALK_DOWN_4 = "walk_down_4.png"

class WalkUpAnimations(AnimationHelper, Enum):
    WALK_UP_1 = "walk_up_1.png"
    WALK_UP_2 = "walk_up_2.png"
    WALK_UP_3 = "walk_up_3.png"
    WALK_UP_4 = "walk_up_4.png"

class WalkLeftAnimations(AnimationHelper, Enum):
    WALK_LEFT_1 = "walk_left_1.png"
    WALK_LEFT_2 = "walk_left_2.png"
    WALK_LEFT_3 = "walk_left_3.png"
    WALK_LEFT_4 = "walk_left_4.png"

class WalkRightAnimations(AnimationHelper,Enum):
    WALK_RIGHT_1 = "walk_right_1.png"
    WALK_RIGHT_2 = "walk_right_2.png"
    WALK_RIGHT_3 = "walk_right_3.png"
    WALK_RIGHT_4 = "walk_right_4.png"

class WalkUpRightAnimations(AnimationHelper,Enum):
    WALK_UP_RIGHT_1 = "walk_up_right_1.png"
    WALK_UP_RIGHT_2 = "walk_up_right_2.png"
    WALK_UP_RIGHT_3 = "walk_up_right_3.png"
    WALK_UP_RIGHT_4 = "walk_up_right_4.png"

class WalkUpLeftAnimations(AnimationHelper,Enum):
    WALK_UP_LEFT_1 = "walk_up_left_1.png"
    WALK_UP_LEFT_2 = "walk_up_left_2.png"
    WALK_UP_LEFT_3 = "walk_up_left_3.png"
    WALK_UP_LEFT_4 = "walk_up_left_4.png"

class WalkDownRightAnimations(AnimationHelper,Enum):
    WALK_DOWN_RIGHT_1 = "walk_down_right_1.png"
    WALK_DOWN_RIGHT_2 = "walk_down_right_2.png"
    WALK_DOWN_RIGHT_3 = "walk_down_right_3.png"
    WALK_DOWN_RIGHT_4 = "walk_down_right_4.png"

class WalkDownLeftAnimations(AnimationHelper,Enum):
    WALK_DOWN_LEFT_1 = "walk_down_left_1.png"
    WALK_DOWN_LEFT_2 = "walk_down_left_2.png"
    WALK_DOWN_LEFT_3 = "walk_down_left_3.png"
    WALK_DOWN_LEFT_4 = "walk_down_left_4.png"

class IdleAnimation(AnimationHelper, Enum):
    IDLE = "idle.png"

class Player: 
    def __init__(self,ctx,startpos_vector2):
        self.pos = startpos_vector2
        self.inventory = {}
        self.health = 100
        self.ctx = ctx
        self.prev_animation_class = IdleAnimation.IDLE
        self.animation_class = IdleAnimation.IDLE
        self.locked = False
        self.fps = 10
        self.tick = 0
        self.t0 = 0
        self.dt = 1 / self.fps
        print(self.ctx)
        self.current_frame = self.ctx.images["idle.png"]

        self.walk_channel = pygame.mixer.Channel(1) # Reserve Channel 1 for walking
        self.walk_sound = Audios.WALKING
        
        self.animations = {
            "up": WalkUpAnimations.WALK_UP_2,
            "down": WalkDownAnimations.WALK_DOWN_2,
            "left": WalkLeftAnimations.WALK_LEFT_2,
            "right": WalkRightAnimations.WALK_RIGHT_2,
            "upleft": WalkUpLeftAnimations.WALK_UP_LEFT_2,
            "upright": WalkUpRightAnimations.WALK_UP_RIGHT_2,
            "downleft": WalkDownLeftAnimations.WALK_DOWN_LEFT_2,
            "downright": WalkDownRightAnimations.WALK_DOWN_RIGHT_2,
            "idle": IdleAnimation.IDLE
        }
    
    def teleport(self, toPos):
        self.pos = toPos

    def draw(self):
        image = self.current_frame
        self.ctx.vscreen.blit(image, dest=self.pos+self.ctx.player.pos*-0.5)

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False    

    def animate(self):
        if (self.tick - self.t0) >= self.dt:
            self.animation_class = self.animation_class.next()
            self.current_frame = self.ctx.images[self.animation_class.value]

            self.t0 = self.tick
            self.draw()
        
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
        target_anim = None

        if facing_vec.length_squared() < 0.001:
            target_anim = self.animations["idle"]
            self.walk_channel.stop()
        else:
            target_anim = self.animations[look_dir]
            if not self.walk_channel.get_busy():
                self.walk_channel.play(self.walk_sound.s, loops=-1)
            facing_vec = facing_vec.normalize()

        if type(self.animation_class) != type(target_anim):
            self.animation_class = target_anim
        
        self.pos += (facing_vec * 200) * self.ctx.dt_s
        bound_rect = self.ctx.scenes[self.ctx.current_scene].bounds.rect
        buffer = {
            "left": 40,
            "right": 40,
            "top": 10,
            "bottom": 70,
        }
        self.pos = pygame.Vector2(
            max(buffer["left"], min(bound_rect.x+bound_rect.width-buffer["right"],self.pos.x)),
            max(buffer["top"], min(bound_rect.y+bound_rect.height-buffer["bottom"],self.pos.y)))
        self.animate()
        self.tick += self.ctx.dt_s
        