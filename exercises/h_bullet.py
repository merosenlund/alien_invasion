import pygame
from pygame.sprite import Sprite

class HorizontalBullet(Sprite):
  """A class to manage bullets fired from the ship."""

  def __init__(self, ai_game) -> None:
      super().__init__()
      self.screen = ai_game.screen
      self.color = (60, 60, 60)

      # Create a bullet rect at (0, 0) and then set correct position.
      self.rect = pygame.Rect(0, 0, 15, 3)
      self.rect.midtop = ai_game.jet.rect.midright

      # Store the bullet's position as a decimal value
      self.x = float(self.rect.x)


  def update(self):
    """Move the bullet up the screen."""
    # Update the decimal position fo the bullet.
    self.x += 3
    # Update the rect position.
    self.rect.x = self.x

  def draw_bullet(self):
    """Draw the bullet to the screen."""
    pygame.draw.rect(self.screen, self.color, self.rect)