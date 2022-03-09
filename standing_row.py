from dataclasses import dataclass

from club import Club


class StandingRow:
    def __init__(self, club: Club, points: int, goals_scored: int, goals_conceded: int):
        self.__name: Club = club
        self.__points: int = points
        self.__goals_scored: int = goals_scored
        self.__goals_conceded: int = goals_conceded
        self.__goals_difference: int = self.__goals_scored - self.__goals_conceded

    def get_club(self):
        return self.__name

    def get_points(self):
        return self.__points

    def get_goals_scored(self):
        return self.__goals_scored

    def get_goals_conceded(self):
        return self.__goals_conceded

    def get_goals_difference(self):
        return self.__goals_scored - self.__goals_conceded

    def set_points(self, points) -> None:
        self.__points = points

    def set_goals_scored(self, goals_scored):
        self.__goals_scored += goals_scored

    def set_goals_conceded(self, goals_conceded):
        self.__goals_conceded += goals_conceded
