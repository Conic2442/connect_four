class Board:
    def __init__(self, rows: int, columns: int, players: list):
        """

        :param rows: Number of rows on grid
        :param columns: Number of columns on grid
        :param players A list of the characters currently playing
        """
        self.bg = "."
        self.border = "-"
        self.num_rows = rows
        self.num_columns = columns
        self.players = players

        self.top_numbers = list(range(1, self.num_columns+1))
        self.top_border = [self.border for i in range(self.num_columns)]

        self.legal_rows = list(range(1, self.num_rows + 1))
        self.legal_columns = list(range(0, self.num_columns))

        self.rows = []

    def init_board(self):
        to_str = list(map(str, self.top_numbers))
        self.rows.append(to_str)
        # self.rows.append(self.top_border)
        for row in range(self.num_rows):
            new_row = []
            for column in range(self.num_columns):
                new_row.append(self.bg)
            self.rows.append(new_row)

        #debug_board '' comment this out
        # self.update_board(2, "H")
        # self.update_board(3, "H")
        # self.update_board(4, "H")
        # self.update_board(5, "Y")
        # self.update_board(5, "H")
        # self.update_board(6, "H")
        # self.update_board(6, "Y")
        # self.update_board(6, "H")
        # self.update_board(7, "Y")
        # self.update_board(7, "Y")
        # self.update_board(7, "Y")



    def update_board(self, column: int, player: str):
        # Todo: This check should happen at the input in game.
        # if column not in self.top_numbers:
        #     raise ValueError("The number is out of range")
        #     quit()

        column = column - 1
        updated_cell = []

        for i, row in enumerate(self.rows):
            if i != 0:

                if self.rows[i][column] in self.players and i == 1:
                    break

                elif self.rows[i][column] in self.players:
                    u = i-1
                    self.rows[u][column] = player
                    updated_cell = {'row': u, 'column': column, 'player': player}
                    break

                elif self.rows[i][column] not in self.players and i == (len(self.rows)-1):
                    self.rows[i][column] = player
                    updated_cell = {'row': i, 'column': column, 'player': player}
                    break

        return updated_cell

    def draw(self):
        print("")
        for row in self.rows:
            row = "  ".join(row)
            print(row)