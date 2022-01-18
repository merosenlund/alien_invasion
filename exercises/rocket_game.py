import sys

import pygame
from rocket import Rocket


class RocketGame:
    """A game to fly rockets around a screen!!!"""

    def __init__(self) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode((800, 800))
        self.screen_rect = self.screen.get_rect()

        self.bg_color = (25, 25, 25)

        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            pass
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_UP:
                        self.rocket.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.rocket.moving_down = True
                    elif event.key == pygame.K_LEFT:
                        self.rocket.moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.rocket.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.rocket.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.rocket.moving_down = False
                    elif event.key == pygame.K_LEFT:
                        self.rocket.moving_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.rocket.moving_right = False

            # Update the rocket
            self.rocket.update()

            # Update the screen
            self.screen.fill(self.bg_color)
            self.rocket.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    rocket_game = RocketGame()
    rocket_game.run_game()
