import pygame

class Storm:
    def __init__(self, ctx):
        self.ctx = ctx
        # The two center points for the storm
        self.camp_center = pygame.Vector2(820, 142)
        self.forage_center = pygame.Vector2(0, 40) # Adjust to your forage map size
        
        self.current_world_pos = pygame.Vector2(self.camp_center)
        self.radius = 2000
        
        # Overlay setup
        self.overlay = pygame.Surface((self.ctx.w, self.ctx.h))
        self.MAGIC_PINK = (255, 0, 255)
        self.overlay.set_colorkey(self.MAGIC_PINK)
        self.overlay.set_alpha(150)

    def update(self):
        # 1. Shrink over time
        self.radius = self.ctx.day_night_clock * (-16.667) + 2000
        print(self.radius)

        # 2. Move between maps based on time
        # DAY_DURATION is 4 mins (240s) in your World class
        cycle_progress = (self.ctx.day_night_clock % 240) / 240 
        
        if cycle_progress < 0.5:
            # First half: Move towards/stay at Camp
            self.current_world_pos = self.camp_center
        else:
            # Second half: Move towards/stay at Foraging
            self.current_world_pos = self.forage_center

    def draw(self):
        self.overlay.fill((75, 0, 130))
        
        # Use the specific parallax multiplier based on the current scene
        multiplier = 0.5 if self.ctx.current_scene == "Camp" else 0.8
        
        screen_x = self.current_world_pos.x - (self.ctx.player.pos.x * multiplier)
        screen_y = self.current_world_pos.y - (self.ctx.player.pos.y * multiplier)

        pygame.draw.circle(
            self.overlay, 
            self.MAGIC_PINK, 
            (int(screen_x), int(screen_y)), 
            int(self.radius)
        )
        self.ctx.vscreen.blit(self.overlay, (0, 0))