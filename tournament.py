import random
from typing import List

from club import Club
from standing_row import StandingRow


class Tournament:
    def __init__(self, name: str, clubs: List[Club]):
        self.name: str = name
        self.clubs: List[Club] = clubs
        random.shuffle(self.clubs)
        self.standings: List[StandingRow] = []
        self.pairings = []

    def print_clubs(self):
        print([club.name for club in self.clubs])

    def generate_standings(self) -> None:
        for club in self.clubs:
            self.standings.append(StandingRow(club, 0, 0, 0, 0, 0, 0, 0))

    def get_row_by_club_name(self, club: Club):
        for row in self.standings:
            if row.get_club() == club:
                return row

    def print_standings(self) -> None:
        for i in range(len(self.standings)):
            club_name = self.standings[i].get_club().name
            club_points = self.standings[i].get_points()
            club_goals_scored = self.standings[i].get_goals_scored()
            club_goals_conceded = self.standings[i].get_goals_conceded()
            club_matches_played = self.standings[i].get_matches_played()
            club_matches_won = self.standings[i].get_matches_won()
            club_matches_lost = self.standings[i].get_matches_lost()
            club_matches_drawn = self.standings[i].get_matches_drawn()
            print(
                f"{i + 1}) {club_name} - points: {club_points}, goals scored: {club_goals_scored}, goals conceded: {club_goals_conceded}, matches played: {club_matches_played} matches won: {club_matches_won}, matches lost: {club_matches_lost}, matches drawn: {club_matches_drawn}")

    def generate_pairings(self):
        half_len = len(self.clubs) // 2
        arr1 = [i for i in range(half_len)]
        arr2 = [i for i in range(half_len, len(self.clubs))][::-1]
        matches = []
        for i in range(len(self.clubs) - 1):
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
        current_round_pairings = [pairings[0]]
        for i in range(1, len(pairings)):
            if i % half == 0:
                round += 1
                self.pairings.append(current_round_pairings)
                current_round_pairings = []
            current_round_pairings.append(pairings[i])
        self.pairings.append(current_round_pairings)

    def print_pairings(self) -> None:
        for i in range(len(self.pairings)):
            print("--------------")
            print(f"Round {i + 1}\n")
            for pair in self.pairings[i]:
                print(f"{pair[0].name} - {pair[1].name}")
