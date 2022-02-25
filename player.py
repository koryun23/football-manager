import random


class Player:
    attacking_positions = ["cf", "lw", "rw", "am"]
    midfield_positions = ["lm", "cm", "dm", "rm"]
    defending_positions = ["lb", "cb", "rb"]

    def __init__(self, name, age, skill, club, position):
        self.name = name
        self.age = age
        self.club = club
        self.skill = skill
        self.position = position
        self.potential = 50
        if self.position != "gk":
            self.skill_set = {
                "goalkeeping": 0,
                "tackling": self.skill,
                "heading": self.skill,
                "passing": self.skill,
                "crossing": self.skill,
                "tech": self.skill,
                "shooting": self.skill,
                "charisma": self.skill,
            }
        else:
            self.skill_set = {
                "goalkeeping": self.skill,
                "tackling": 0,
                "heading": 0,
                "passing": 0,
                "crossing": 0,
                "tech": 0,
                "shooting": 0,
                "charisma": 0,
            }
        self.pos_x = 0
        self.pos_y = 0
        self.orig_pos_x = 0
        self.orig_pos_y = 0
        self.attacking_pos_x = 0
        self.attacking_pos_y = 0
        self.defending_pos_x = 0
        self.defending_pos_y = 0

    def train(self): # the trainings will cost some amount of money
        generator = random.randint(0, 100)
        
        if self.potential < 50:  # then there is (potential)% chance that he will progress
            if generator < self.potential:
                self.improve()
        elif self.potential < 75:  # then there is 60% chance that he will progress
            if generator < 60:
                self.improve()
        else:  # then there is 90% chance that he will progress
            if generator < 90:
                self.improve()

    def improve(self):
        if self.position == "gk":
            self.skill_set["goalkeeping"] += 0.5
        if self.position[0] == "l" or self.position[0] == "r":
            self.skill_set["croosing"] += 0.3
            self.skill_set["tech"] += 0.2
        if self.position[0] == "c":
            self.skill_set["heading"] += 0.2
        if self.position in Player.attacking_positions:
            self.skill_set["shooting"] += 0.3
            self.skill_set["tech"] += 0.2
            self.skill_set["passing"] += 0.2
            if self.position == "cf":
                self.skill_set["heading"] += 0.2
        if self.position in Player.midfield_positions:
            self.skill_set["tech"] += 0.3
            self.skill_set["passing"] += 0.3
            self.skill_set["tackling"] += 0.2
        if self.position in Player.defending_positions:
            self.skill_set["tackling"] += 0.4

        # calculate overall skill
        if self.position == "gk":
            self.skill = self.skill_set["goalkeeping"]
        else:
            all_skills = 0
            for skill in self.skill_set:
                all_skills += self.skill_set[skill]
            self.skill = all_skills/7
# pl=Player("Josh", 23, 78, "Bradford", 748590, 12000, "cf")
# print(pl.skill_set)

            


