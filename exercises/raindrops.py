import sys

import pygame
from raindrop import Raindrop


class Raindrops:
    """A nice calming rainstorm."""

    def __init__(self) -> None:
        """Initialize the rainstorm."""
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 800))
        self.screen_rect = self.screen.get_rect()

        self.bg_color = (173, 216, 230)

        self.rain = pygame.sprite.Group()

        self.add_row_counter = 0

        self._add_rain()

    def run_game(self):
        """The game loop."""
        while True:
            self._check_events()
            self._update_drops()
            self._draw_screen()

    def _check_events(self):
        """Check and deal with events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_q
            ):
                sys.exit()

    def _update_drops(self):
        """Make the rain fall and add new rain at the top."""
        self.rain.update()
        self.add_row_counter += 1
        if self.add_row_counter == 50:
            self.add_row_counter = 0
            self._add_rain()

        for drop in self.rain.copy():
            if drop.rect.top >= self.screen_rect.bottom:
                self.rain.remove(drop)

    def _add_rain(self):
        """Add rain to the screen."""
        drop = Raindrop(self)
        drop_width = drop.rect.height
        drops_per_row = (self.screen_rect.width - drop_width) // (drop_width * 2)
        for count in range(drops_per_row + 1):
            new_drop = Raindrop(self)
            new_drop.rect.x = (drop_width / 2) + (drop_width * 2 * count)
            new_drop.rect.bottom = self.screen_rect.top
            self.rain.add(new_drop)

    def _draw_screen(self):
        self.screen.fill(self.bg_color)
        self.rain.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    rd = Raindrops()
    rd.run_game()
