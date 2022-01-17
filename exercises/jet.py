import pygame

class Jet:
  """A class for managing jets in the blue sky game."""

  def __init__(self, bs_game) -> None:
      """Initialize the jet."""
      self.screen = bs_game.screen
      self.screen_rect = bs_game.screen.get_rect()

      self.image = pygame.image.load('exercises/images/fighter_jet.bmp')
      self.rect = self.image.get_rect()

      self.rect.midleft = self.screen_rect.midleft

  def blitme(self):
    """Draw the jet to the screen."""
    self.screen.blit(self.image, self.rect)