import sys

import pygame

from jet import Jet


class BlueSky:
    """A pygame window with a blue background."""

    def __init__(self) -> None:
        """Initialize the game."""
        pygame.init()

        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Blue Sky")

        self.bg_color = (173, 216, 230)

        self.jet = Jet(self)

    def run_game(self):
        """Run the game loop."""
        while True:
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Draw Screen
            self.screen.fill(self.bg_color)
            self.jet.blitme()

            pygame.display.flip()


if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()
