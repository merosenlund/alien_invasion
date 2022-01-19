import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A single cute little raindrop."""

    def __init__(self, raindrops) -> None:
        super().__init__()

        self.screen = raindrops.screen
        self.image = pygame.image.load("exercises/images/rain_drop.bmp")
        self.rect = self.image.get_rect()

    def update(self):
        """Make the cute little raindrops move down."""
        self.rect.y += 1
        print("Updating the raindrops!")
