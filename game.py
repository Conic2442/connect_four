from settings import GameSettings
from player import Player
from board import Board


# Todo: Continue here.
# Each game needs to be its own object. and store results etc in the scoreboard at the end. before killing the game.
class Game:
    def __init__(self, game_id: int, settings: GameSettings):
        self.game_id = game_id
        self.winner = ""
        self.settings = settings

        # Players
        self.players = []
        # print(self.settings.players)
        for player in self.settings.players:
            new_player = Player(player)
            self.players.append(new_player)

        self.board = Board(self.settings.rows, self.settings.columns, self.settings.players)
        self.board.init_board()

    # Game runner 2000
    def run_game(self):

        self.board.draw()
        win = False
        while not win:
            for player in self.players:
                if win:
                    break

                player_input = int(input(f"Next turn: {player.player_character} Select column: "))
                updated_cell = self.board.update_board(player_input, player.player_character)

                # DEBUG WIN CONDITION

                self.board.draw()

                # Check win conditions - Also - what happens if board is filled up?
                # Could calculate turns from settings.get_grid_size ?? And have a fixed number of turns??
                # Todo: Check win conditions here

                # win = True  # comment/uncomment to trigger WIN for debug
                win = self.check_win_conditions(updated_cell)
                if win:
                    print(updated_cell)
                    self.winner = player.player_character

        return self.winner

    def check_win_conditions(self, updated_cell: dict):
        """
        Checks win conditions.
        :param updated_cell: Updated cell dictionary
        :return: bool
        """

        player = updated_cell['player']
        # print(f"Player: {player}")
        row = updated_cell['row']
        column = updated_cell['column']

        legal_rows = self.board.legal_rows
        legal_columns = self.board.legal_columns

        # print(legal_rows, legal_columns)

        count_line = 0

        board = self.board.rows


        if row in legal_rows and column in legal_columns:
            # print(row, column)
            if board[row][column] == player:
                print(board[row][column])
                cont = True
            else:
                cont = False





    # def end_game(self):
    #     return self.game_id, self.winner


# settings = GameSettings()
# game = Game(1, settings)
# game.run_game()
