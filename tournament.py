import random

from player import Player
from club import Club


class Tournament:
    def __init__(self, name, clubs):
        self.name = name
        self.clubs = clubs
        self.standings = []
        self.matches = [[None for _ in range(20)] for _ in range(20)]

    def generate_standings(self):
        for club in self.clubs:
            self.standings.append({"Name": club.name, "Points": 0, "Goals Scored": 0, "Goals Conceded": 0, "Goal Difference": 0})
    def print_standings(self):
        for row in self.standings:
            print(row)
