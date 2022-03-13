class MovementSkill:
    def __init__(self, acceleration, speed):
        self.__acceleration = acceleration
        self.__speed = speed

    def get_acceleration(self):
        return self.__acceleration

    def get_speed(self):
        return self.__speed
