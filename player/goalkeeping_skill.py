class GoalkeepingSkill:
    def __init__(self, goalkeeping):
        self.__goalkeeping = goalkeeping
        self.__number_of_skills = 1

    def get_goalkeeping(self):
        return self.__goalkeeping

    def total(self):
        return self.__goalkeeping

    def overall(self):
        return self.total() // self.__number_of_skills
