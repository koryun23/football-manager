class MovementSkill:
    def __init__(self, acceleration, speed):
        self.__acceleration = acceleration
        self.__speed = speed
        self.__number_of_skills = 2

    def get_acceleration(self):
        return self.__acceleration

    def get_speed(self):
        return self.__speed

    def total(self):
        return self.__speed + self.__acceleration

    def overall(self):
        return self.total() // self.__number_of_skills
