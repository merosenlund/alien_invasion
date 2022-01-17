import pygame

class Rocket:
  """A rocket that can be flown around the screen."""

  def __init__(self, rocket_game) -> None:
      """Initialize the rocket."""
      self.screen = rocket_game.screen
      self.screen_rect = self.screen.get_rect()

      self.image = pygame.image.load('images/ship.bmp')
      self.rect = self.image.get_rect()

      # Movement flags
      self.moving_right = False
      self.moving_left = False
      self.moving_up = False
      self.moving_down = False

  def update(self):
    """Update the rockets position if moving."""
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.rect.x += 2
    if self.moving_left and self.rect.left > self.screen_rect.left:
      self.rect.x -= 2
    if self.moving_up and self.rect.top > self.screen_rect.top:
      self.rect.y -= 2
    if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.rect.y += 2

  def blitme(self):
    """Draw the rocket to the screen."""
    self.screen.blit(self.image, self.rect)