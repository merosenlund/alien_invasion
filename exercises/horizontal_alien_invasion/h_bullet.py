import pygame
from pygame.sprite import Sprite


class HorizontalBullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, hai_game) -> None:
        super().__init__()
        self.settings = hai_game.settings
        self.screen = hai_game.screen
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect((0, 0), self.settings.bullet_size)
        self.rect.midtop = hai_game.jet.rect.midright

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position for the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
