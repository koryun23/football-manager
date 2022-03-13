class AttackingSkill:
    def __init__(self, crossing, finishing, long_shooting, heading, short_passing, long_passing, dribbling, penalties):
        self.__crossing = crossing
        self.__finishing = finishing
        self.__long_shooting = long_shooting
        self.__heading = heading
        self.__short_passing = short_passing
        self.__long_passing = long_passing
        self.__dribbling = dribbling
        self.__penalties = penalties

    def get_crossing(self):
        return self.__crossing

    def get_finishing(self):
        return self.__finishing

    def get_long_shooting(self):
        return self.__long_shooting

    def get_heading(self):
        return self.__heading

    def get_short_passing(self):
        return self.__short_passing

    def get_dribbling(self):
        return self.__dribbling
    def get_penalties(self):
        return self.__penalties

    def get_long_passing(self):
        return self.__long_passing
