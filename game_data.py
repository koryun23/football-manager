from game import Game


class GameData:
    def __init__(self, game: Game):
        self.__game = game
        self.__events = self.__game.game_events
        self.__score = self.__events[-1]

    def get_game(self):
        return self.__game

    def get_game_events(self):
        return self.__events

    def get_score(self):
        return self.__score
