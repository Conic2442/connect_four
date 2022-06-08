import showrunner
from settings import GameSettings


def welcome():
    gs = GameSettings()
    print(f"Booting version {gs.game_version} of 'connect 4' - Conic edition. \n"
          "Best of luck.")


if __name__ == "__main__":
    welcome()
    sr = showrunner.Showrunner()
    sr.run()
