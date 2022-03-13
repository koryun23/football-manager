class StrengthSkill:
    def __init__(self, stamina, strength):
        self.__stamina =  stamina
        self.__strength = strength
        self.__number_of_skills = 2
    def get_stamina(self):
        return self.__stamina

    def get_strength(self):
        return self.__strength

    def total(self):
        return self.__strength + self.__stamina

    def overall(self):
        return self.total() // self.__number_of_skills
