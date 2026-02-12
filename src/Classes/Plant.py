from enum import Enum
import pygame

pygame.init()


class GrowthStages(Enum):
    SEED = 0
    SPROUT = 1
    MID_GROWTH = 2
    HARVESTABLE = 3


class Plant(pygame.sprite.Sprite):
    def __init__(self, species, center_pos):
        super().__init__()
        self.center_pos = center_pos
        self.stage = GrowthStages.SEED
        self.species = species
        self._set_image()

    def _set_image(self):
        self.image = pygame.image.load(
            f"assets/sprites/{self.species}_{self.stage.name.lower()}.png"
        ).convert_alpha()
        self.rect = self.image.get_rect(center=self.center_pos)

    def draw(self):
        ctx.vscreen.blit(self.image, self.rect)

    def grow(self):
        if self.stage != GrowthStages.HARVESTABLE:
            self.stage = GrowthStages(self.stage.value + 1)
            self._set_image()
