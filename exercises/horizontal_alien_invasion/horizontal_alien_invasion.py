import sys

import pygame
from pygame import time

from settings import Settings
from jet import Jet
from haliens import Halien
from h_bullet import HorizontalBullet


class HorizontalAlienInvasion:
    """It's alien invasion but horizontal!"""

    def __init__(self) -> None:
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(self.settings.game_name)

        self.bg_color = self.settings.bg_color

        self.jet = Jet(self)

        self.bullets = pygame.sprite.Group()

        self.haliens = pygame.sprite.Group()
        self.haliens.add(Halien(self))

    def run_game(self):
        """Run the game loop."""
        while True:
            self._check_events()
            self.jet.update()
            self._update_bullets()
            self._update_haliens()
            self._update_screen()

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
                elif event.key == pygame.K_q:
                    sys.exit()
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

    def _update_haliens(self):
        """Udate the haliens and add more if the time is right"""
        self.haliens.update()
        if time.get_ticks() % self.settings.halien_add_speed == 0:
            # breakpoint()
            print(time.get_ticks() % self.settings.halien_add_speed)
            self._add_halien()

    def _add_halien(self):
        """Add a halien to the game."""
        new_halien = Halien(self)
        self.haliens.add(new_halien)

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.jet.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.haliens.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    hai = HorizontalAlienInvasion()
    hai.run_game()
