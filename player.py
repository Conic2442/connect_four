class Player:
    def __init__(self, player_character: str):
        """
        Player object
        """
        # GameSettings.__init__(self)
        # Colors piece number
        self.player_character = player_character
        self.score = 0
        # self.games_won = [] # todo: list of game numbers won.

        """
        self.legal_players = [1, 2]
        if player not in self.legal_players:
            raise ValueError("Player value must be 1 or 2")
        else:
            self.player = player

        if player != 1:
            self.player_character = "B"
        """

    @property
    def player_character(self):
        return self.__player

    @player_character.setter
    def player_character(self, character: str):
        """
        Sets custom player one character
        :param character: string
        :return: none
        """
        first_letter = self.check_player_character(character)
        self.__player = first_letter

    @staticmethod
    def check_player_character(string: str):
        if len(string) > 1:
            split = list(string)
            first_letter = split[0]
            print(f'{string} contains more than 1 letter, using first letter "{first_letter}" as default')

        else:
            first_letter = string
        return first_letter
