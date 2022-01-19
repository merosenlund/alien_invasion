import pygame
from pygame.sprite import Sprite


class Halien(Sprite):
    """Aliens that fly horizontally."""

    def __init__(self, hai_game) -> None:
        super().__init__()
        self.screen = hai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
