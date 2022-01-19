import sys
import random

import pygame
from star import Star


class StarField:
    """A beautiful field of stars"""

    def __init__(self) -> None:
        """Initialize the 'game'"""
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 800))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Star Field")

        self.stars = pygame.sprite.Group()

        self.create_star_field()

    def run_game(self):
        """Run the game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit()

            self.stars.draw(self.screen)
            pygame.display.flip()

    def create_star_field(self):
        """Create a grid of stars"""
        for count in range(200):
            new_star = Star(self)
            new_star.rect.x = random.randint(0, 1001)
            new_star.rect.y = random.randint(0, 801)
            self.stars.add(new_star)


if __name__ == "__main__":
    star_field = StarField()
    star_field.run_game()
