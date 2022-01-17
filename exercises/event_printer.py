import sys

import pygame

class EventPrinter:
  """A pygame class for printing pygame events to the terminal and checking them out."""

  def __init__(self) -> None:
      """Initialize this simple game."""
      pygame.init()
      self.screen = pygame.display.set_mode((500, 500))
      self.screen_rect = self.screen.get_rect()

  def run_game(self):
    while True:
      # Take care of events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          print(event.key)


if __name__ == '__main__':
  ep = EventPrinter()
  ep.run_game()