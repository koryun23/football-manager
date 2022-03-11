from game import Game


class GameData:
    def __init__(self, game: Game):
        self.__game = game
        self.__events = self.__game.game_events

    def get_game(self):
        return self.__game

    def get_game_events(self):
        return self.__events
