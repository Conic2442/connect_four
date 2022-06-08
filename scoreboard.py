class ScoreBoard:
    def __init__(self):
        self.scoreboard = {}

    def submit_game(self, game_id, winner: str):
        self.scoreboard[game_id] = winner

    @property
    def total_games_played(self):
        return len(self.scoreboard)

    def __str__(self):
        tot_games = self.total_games_played
        winners = []

        print_str = f"---SCOREBOARD---\n" \
                    f"Total games played: {tot_games}\n"

        # Games
        for game_id, player in self.scoreboard.items():
            winners.append(player)
            print_str += f'Game {game_id} winner: player {player}\n'

        # Players
        res = {i: winners.count(i) for i in winners}
        for player_name, wins in res.items():
            print_str += f'Player {player_name} has a total of {wins} victories!'

        return print_str



# sc = ScoreBoard()
#
# sc.submit_game(1, 2)
# sc.submit_game(2, 1)
# sc.submit_game(3, 2)
#
# print(sc)
