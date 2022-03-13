class MentalitySkill:
    def __init__(self, composure):
        self.__composure = composure
        self.__number_of_skills = 1

    def get_composure(self):
        return self.__composure

    def total(self):
        return self.__composure

    def overall(self):
        return self.total() // self.__number_of_skills
