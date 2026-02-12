import pygame
import time


class Storm:
    def __init__(self, ctx):
        self.ctx = ctx
        # The two center points for the storm
        self.camp_center = pygame.Vector2(820, 142)
        self.forage_center = pygame.Vector2(0, 40)  # Adjust to your forage map size

        self.current_world_pos = pygame.Vector2(self.camp_center)
        self.radius = 2000
        self.last_time_damage_taken = time.time()

        # Overlay setup
        self.overlay = pygame.Surface((self.ctx.w, self.ctx.h))
        self.MAGIC_PINK = (255, 0, 255)
        self.overlay.set_colorkey(self.MAGIC_PINK)
        self.overlay.set_alpha(150)

    def update(self):
        if self.ctx.current_scene == "Camp":
            self.radius = max(0, self.ctx.day_night_clock * (-16.667) + 4000.04)
        else:
            self.radius = max(0, self.ctx.day_night_clock * (-16.667) + 2000)

        self.cycle_progress = self.ctx.day_night_clock / 240

        if self.cycle_progress < 0.5:
            # First half: Move towards/stay at Camp
            self.current_world_pos = self.forage_center
        else:
            # Second half: Move towards/stay at Foraging
            self.current_world_pos = self.camp_center

    def draw(self):
        self.overlay.fill((75, 0, 130))

        multiplier = 0.5 if self.ctx.current_scene == "Camp" else 0.8

        screen_x = self.current_world_pos.x - (self.ctx.player.pos.x * multiplier)
        screen_y = self.current_world_pos.y - (self.ctx.player.pos.y * multiplier)

        pygame.draw.circle(
            self.overlay,
            self.MAGIC_PINK,
            (int(screen_x), int(screen_y)),
            int(self.radius),
        )

        if self.ctx.player.pos.distance_to(self.current_world_pos) > self.radius:
            if (time.time() - self.last_time_damage_taken) >= 1:
                self.ctx.player.health.add_health(-10)
                self.last_time_damage_taken = time.time()

        self.ctx.vscreen.blit(self.overlay, (0, 0))
