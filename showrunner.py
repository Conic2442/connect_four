from game import Game
from settings import GameSettings
from scoreboard import ScoreBoard as ScoreBoard
from player import Player


class Showrunner:

    def __init__(self):
        self.game_running = True
        self.next_game_id = 0
        self.scoreboard = ScoreBoard()
        self.settings = GameSettings()

    def run(self):
        input_select = int(input("1: standard, 2: custom game - Please choose action: "))
        if input_select == 1:
            pass

        elif input_select == 2:
            self.setup_custom_game()

        # Game manager
        while self.game_running:
            print("")
            input_select = int(input("1: new game, 2: Scoreboard 3: stop playing - Please choose action: "))
            print("")
            if input_select == 1:

                # noinspection PyAttributeOutsideInit
                self.current_game = self.start_new_game()
                print(f"Starting new game - Game id: {self.current_game.game_id}")
                self.current_game.run_game()

                self.end_game()

            elif input_select == 2:
                print(self.scoreboard)

            elif input_select == 3:
                self.game_running = False

    # Utility
    def end_game(self):
        """
        Ends current game and passes the score to the scoreboard.
        :return: None
        """
        game_id = self.current_game.game_id
        winner = self.current_game.winner

        print(f"The winner of game {game_id} is {winner}! Congratulations!")
        self.scoreboard.submit_game(game_id, winner)

    def start_new_game(self):
        next_game_id = int(self.next_game_id) + 1
        # noinspection PyAttributeOutsideInit
        self.current_game = Game(next_game_id, self.settings)
        self.next_game_id = next_game_id
        return self.current_game

    def setup_custom_game(self):
        print("Creating custom game")
        players = int(input("How many players? "))
        player_list = []
        for player in (range(players)):
            new_player = str(input(f"Player {player + 1} choose your Character: "))
            new_player = Player.check_player_character(new_player)
            player_list.append(new_player)

        self.settings.players = player_list

        rows = 0
        try:
            rows = int(input(f"Grid size - rows (default is {self.settings.rows} Leave blank for default): "))
        except:
            pass

        if rows:
            self.settings.rows = rows

        columns = 0
        try:
            columns = int(input(f"Grid size - columns (default is {self.settings.columns} Leave blank for default): "))
        except:
            pass
        if columns:
            self.settings.columns = columns
