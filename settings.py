class GameSettings:
    def __init__(self, players=None):
        if players is None:
            self._players = ["Y", "H"]

        self.game_version = 1.0

        # Board size
        self.rows = 6
        self.columns = 7

    @property
    def board_size_total(self):
        return self.rows * self.columns

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players_in: list):
        self._players = players_in
