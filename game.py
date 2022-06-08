from settings import GameSettings
from player import Player
from board import Board


def return_win(count):
    if count >= 4:
        return True
    else:
        return False


class Game:
    def __init__(self, game_id: int, settings: GameSettings):
        self.game_id = game_id
        self.winner = ""
        self.settings = settings

        # Players
        self.players = []

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
                # Check if player input is legal here?

                updated_cell = self.board.update_board(player_input, player.player_character)

                self.board.draw()

                # win = True  # comment/uncomment to trigger WIN for debug
                win = self.check_win_conditions(updated_cell)
                if win:
                    # print(updated_cell)
                    self.winner = player.player_character

        return self.winner

    def check_win_conditions(self, updated_cell: dict):
        """
        Checks win conditions.
        :param updated_cell: Updated cell dictionary
        :return: bool
        """

        player = updated_cell['player']
        row = updated_cell['row']
        column = updated_cell['column']

        board = self.board.rows

        has_four = self.count_sequential(board, player, row, column, 0, 1)
        if return_win(has_four):
            return True
        has_four = self.count_sequential(board, player, row, column, -1, 1)
        if return_win(has_four):
            return True
        has_four = self.count_sequential(board, player, row, column, -1, 0)
        if return_win(has_four):
            return True
        has_four = self.count_sequential(board, player, row, column, -1, -1)
        if return_win(has_four):
            return True
        has_four = self.count_sequential(board, player, row, column, 0, -1)
        if return_win(has_four):
            return True
        has_four = self.count_sequential(board, player, row, column, 1, -1)
        if return_win(has_four):
            return True
        has_four = self.count_sequential(board, player, row, column, 1, 0)
        if return_win(has_four):
            return True
        has_four = self.count_sequential(board, player, row, column, 1, 1)
        if return_win(has_four):
            return True

    def count_sequential(self, board, player, start_y, start_x, direction_y, direction_x):
        """
        Count_sequential - Per Thomas, master of code | with a tiny tweak
        :param board: list
        :param player: string
        :param start_y: int
        :param start_x: int
        :param direction_y: int
        :param direction_x: int
        :return: int
        """

        count = 0
        n = 0

        legal_rows = self.board.legal_rows
        legal_columns = self.board.legal_columns

        while True:
            y = start_y + direction_y * n
            x = start_x + direction_x * n

            if y not in legal_rows or x not in legal_columns:
                return count

            if board[y][x] != player:
                return count

            count += 1
            n += 1
