class Match:
    def __init__(self, team1, team2, score, team1_goal_scorers, team2_goal_scorers):
        self.__team1 = team1
        self.__team2 = team2
        self.__score = score
        self.__team1_goal_scorers = team1_goal_scorers
        self.__team2_goal_scorers = team2_goal_scorers

    @property
    def get_team1(self):
        return self.__team1

    @property
    def get_team2(self):
        return self.__team2

    @property
    def get_score(self):
        return self.__score

    @property
    def get_team1_goal_scorers(self):
        return self.__team1_goal_scorers

    @property
    def get_team2_goal_scorers(self):
        return self.__team2_goal_scorers
