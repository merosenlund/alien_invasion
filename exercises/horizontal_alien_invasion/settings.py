class Settings:
  """Settings for Horizontal Alien Invasion."""
  def __init__(self) -> None:
      """Initialize the settings."""
      # Settings for the game
      self.screen_height = 500
      self.screen_width = 500
      self.game_name = "Horizontal Alien Shooter"
      self.bg_color = (173, 216, 230)

      # Settings for the jet
      self.jet_speed = 4

      # Settings for the bullets
      self.bullet_color = (60, 60, 60)
      self.bullet_size = (15, 3)
      self.bullet_speed = 3
      self.bullet_limit = 5

      # Settings for the aliens