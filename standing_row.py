from dataclasses import dataclass

from club import Club


class StandingRow:
    def __init__(self, club: Club, points: int, goals_scored: int, goals_conceded: int, matches_played: int, matches_won: int, matches_lost: int, matches_drawn: int):
        self.__club: Club = club
        self.__points: int = points
        self.__goals_scored: int = goals_scored
        self.__goals_conceded: int = goals_conceded
        self.__goals_difference: int = self.__goals_scored - self.__goals_conceded
        self.__matches_played: int = matches_played
        self.__matches_won: int = matches_won
        self.__matches_lost: int = matches_lost
        self.__matches_drawn: int = matches_drawn

    def get_club(self):
        return self.__club

    def get_points(self):
        return self.__points

    def get_goals_scored(self):
        return self.__goals_scored

    def get_goals_conceded(self):
        return self.__goals_conceded

    def get_goals_difference(self):
        return self.__goals_scored - self.__goals_conceded

    def get_matches_played(self):
        return self.__matches_played

    def get_matches_won(self):
        return self.__matches_won

    def get_matches_lost(self):
        return self.__matches_lost

    def get_matches_drawn(self):
        return self.__matches_drawn

    def set_points(self, points) -> None:
        self.__points = points

    def set_goals_scored(self, goals_scored):
        self.__goals_scored += goals_scored

    def set_goals_conceded(self, goals_conceded):
        self.__goals_conceded += goals_conceded

    def set_matches_played(self, matches_played):
        self.__matches_played += matches_played

    def set_matches_won(self, matches_won):
        self.__matches_won = matches_won

    def set_matches_lost(self, matches_lost):
        self.__matches_lost = matches_lost

    def set_matches_drawn(self, matches_drawn):
        self.__matches_drawn = matches_drawn
