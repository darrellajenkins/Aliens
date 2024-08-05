class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai):
        """Initialize statistics for Alien Invasion."""
        self.settings = ai.settings
        self.reset_stats()
        with open("high_score.txt") as data:
            self.high_score = data.read()
            self.high_score = int(self.high_score)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
