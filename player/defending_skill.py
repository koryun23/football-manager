class DefendingSkill:
    def __init__(self, tackle):
        self.__tackle = tackle
        self.__number_of_skills = 1

    def get_tackle(self):
        return self.__tackle

    def total(self):
        return self.__tackle

    def overall(self):
        return self.total() // self.__number_of_skills
