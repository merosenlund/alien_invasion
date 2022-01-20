import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game) -> None:
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset
        self.high_score = self.load_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_score(self) -> int:
        """Load the high score if there is one."""
        pass
        try:
            file_name = "high_score.txt"
            with open(file_name) as f:
                high_score = json.load(f)
        except FileNotFoundError:
            # There isn't a current highscore so we can just move on.
            high_score = 0
        return high_score

    def save_score(self):
        """If the current score is the high score then save it."""
        pass
        file_name = "high_score.txt"
        with open(file_name, "w") as f:
            json.dump(self.high_score, f)
