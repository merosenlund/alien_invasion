from random import randint

import pygame
from pygame.sprite import Sprite


class Halien(Sprite):
    """Aliens that fly horizontally."""

    def __init__(self, hai_game) -> None:
        super().__init__()
        self.settings = hai_game.settings
        self.screen = hai_game.screen
        self.screen_rect = hai_game.screen_rect

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        half_height = self.rect.height // 2

        # Randomize where on the right the halien appears.
        random_spot = randint(
            self.screen_rect.top + half_height, self.screen_rect.bottom - half_height
        )
        self.rect.x = random_spot
        self.rect.y = self.screen_rect.right

        print(f"New alien created at {self.rect.x}, {self.rect.y}")

        self.x = float(self.rect.y)

    def update(self):
        """Update this halien"""
        self.x -= self.settings.halien_speed
        self.rect.x = self.x
