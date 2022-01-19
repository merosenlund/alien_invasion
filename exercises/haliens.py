import pygame
from pygame.sprite import Sprite


class Halien(Sprite):
    """Aliens that fly horizontally."""

    def __init__(self, bs_game) -> None:
        super().__init__()
        self.screen = bs_game.screen

        self.image = pygame.image.load()
