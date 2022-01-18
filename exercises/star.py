import pygame
from pygame.sprite import Sprite

class Star(Sprite):
  """A cute little star."""

  def __init__(self, star_field) -> None:
      """Intialize the star along with sprite attributes."""
      super().__init__()
      self.screen = star_field.screen
      self.screen_rect = star_field.screen_rect

      self.image = pygame.image.load('exercises/images/star.bmp')
      self.rect = self.image.get_rect()

  def blitme(self):
    """Draw the star to the screen."""
    self.screen.blit(self.image, self.rect)