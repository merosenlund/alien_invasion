import sys

import pygame

from jet import Jet
from h_bullet import HorizontalBullet


class BlueSky:
    """A pygame window with a blue background."""

    def __init__(self) -> None:
        """Initialize the game."""
        pygame.init()

        self.screen = pygame.display.set_mode((500, 500))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Blue Sky")

        self.bg_color = (173, 216, 230)

        self.jet = Jet(self)

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Run the game loop."""
        while True:
            self._check_events()
            self.jet.update()
            self._update_bullets()
            self._draw_screen()

    def _check_events(self):
        """Check the events that occurred."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.jet.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.jet.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.jet.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.jet.moving_down = False

    def _fire_bullet(self):
        """Fire a bullet scotty!"""
        new_bullet = HorizontalBullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update all of the bullets position and remove bullets that are off the screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)

    def _draw_screen(self):
        """Redraw the game screen."""
        self.screen.fill(self.bg_color)
        self.jet.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()



if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()
