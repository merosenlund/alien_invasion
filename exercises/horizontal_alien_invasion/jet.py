import pygame


class Jet:
    """A class for managing jets in the blue sky game."""

    def __init__(self, hai_game) -> None:
        """Initialize the jet."""
        self.settings = hai_game.settings
        self.screen = hai_game.screen
        self.screen_rect = hai_game.screen.get_rect()

        self.image = pygame.image.load("exercises/images/fighter_jet.bmp")
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the jet to the screen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the jet's position on the screen."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.jet_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.jet_speed
