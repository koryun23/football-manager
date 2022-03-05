import random
from typing import List, Dict
from club import Club


class Tournament:
    def __init__(self, name: str, clubs: List[Club]):
        self.name: str = name
        self.clubs: List[Club] = clubs
        random.shuffle(self.clubs)
        self.standings = []
        self.pairings = []
    def print_clubs(self):
        print([club.name for club in self.clubs])

    def generate_standings(self) -> None:
        for club in self.clubs:
            self.standings.append(
                {"Name": club.name, "Points": 0, "Goals Scored": 0, "Goals Conceded": 0, "Goal Difference": 0})

    def print_standings(self) -> None:
        for row in self.standings:
            print(row)

    def generate_pairings(self):
        half_len = int(len(self.clubs)/2)
        arr1 = [i for i in range(half_len)]
        arr2 = [i for i in range(half_len, len(self.clubs))][::-1]
        matches = []
        for i in range(len(self.clubs)-1):
            arr1.insert(1, arr2.pop(0))
            arr2.append(arr1.pop())
            for a, b in zip(arr1, arr2):
                possible_pairings = ((self.clubs[a], self.clubs[b]), (self.clubs[b], self.clubs[a]))
                matches.append(random.choice(possible_pairings))
        return matches

    def format_pairings(self):
        half = len(self.clubs) // 2
        pairings = self.generate_pairings()
        round = 1
        current_round_pairings = []
        for i in range(len(pairings)):
            if i % half == 0 and i > 0:
                round += 1
                self.pairings.append(current_round_pairings)
                current_round_pairings = []
            current_round_pairings.append(pairings[i])

    def print_pairings(self) -> None:
        for i in range(len(self.pairings)):
            print("--------------")
            print(f"Round {i+1}")
            print()
            for pair in self.pairings[i]:
                print(f"{pair[0].name} - {pair[1].name}")
