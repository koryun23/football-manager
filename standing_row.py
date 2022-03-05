class StandingRow:
    def __init__(self, name, points, goals_scored, goals_conceded):
        self.__name = name
        self.__points = points
        self.__goals_scored = goals_scored
        self.__goals_conceded = goals_conceded
        self.__goals_difference = self.__goals_scored - self.__goals_conceded

    @property
    def get_name(self):
        return self.__name

    @property
    def get_points(self):
        return self.__points

    @property
    def get_goals_scored(self):
        return self.__goals_scored

    @property
    def get_goals_conceded(self):
        return self.__goals_conceded
