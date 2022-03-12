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
        team_col = "TEAM" + (Tournament.club_max_length(self.clubs) - 4) * " "
        points_col = "P"
        goals_scored_col = "GS"
        goals_conceded_col = "GC"
        matches_played_col = "M"
        matches_won_col = "W"
        matches_lost_col = "L"
        matches_drawn_col = "D"
        print(
            f"{team_col}|{points_col} |{goals_scored_col}{(self.goals_scored_max_length()-2)*' '}|{goals_conceded_col}{(self.goals_conceded_max_length()-2)*' '}|{matches_played_col}|{matches_won_col}|{matches_lost_col}|{matches_drawn_col}")
        goals_scored_max_length = self.goals_scored_max_length()
        goals_conceded_max_length = self.goals_conceded_max_length()
        clubs_max_length = Tournament.club_max_length(self.clubs)
        points_max_length = self.points_max_length()
        for row in self.standings:
            row_points_length = 3 if row.get_points() >= 100 else 2 if row.get_points() >= 10 else 1
            goals_scored_length = 3 if row.get_goals_scored() >= 100 else 2 if row.get_goals_scored() >= 10 else 1
            goals_conceded_length = 3 if row.get_goals_conceded() >= 100 else 2 if row.get_goals_conceded() >= 10 else 1

            goals_scored_string = str(row.get_goals_scored()) + (goals_scored_max_length - goals_scored_length) * " "
            goals_conceded_string = str(row.get_goals_conceded()) + (goals_conceded_max_length - goals_conceded_length) * " "
            club_string = row.get_club().name + (clubs_max_length - len(row.get_club().name)) * " "
            points_string = str(row.get_points()) + (points_max_length - row_points_length) * " "
            matches_played_string = str(row.get_matches_played())
            matches_won_string = str(row.get_matches_won())
            matches_lost_string = str(row.get_matches_lost())
            matches_drawn_string = str(row.get_matches_drawn())
            print(f"{club_string}|{points_string}|{goals_scored_string}|{goals_conceded_string}|{matches_played_string}|{matches_won_string}|{matches_lost_string}|{matches_drawn_string}")
            #print(f"{row.get_club().name}{(Tournament.club_max_length(self.clubs) - len(row.get_club().name)) * ' '}|{row.get_points()}{(self.points_max_length()-row.get_points())*' '}|{row.get_goals_scored()}{(self.goals_scored_max_length()-row.get_goals_scored())*' '}|{row.get_goals_conceded()}{(self.goals_conceded_max_length()-row.get_goals_conceded())*' '}|{row.get_matches_played()}|{row.get_matches_won()}|{row.get_matches_lost()}|{row.get_matches_drawn()}")

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
        self.double_matches(matches)
        return matches

    def double_matches(self, matches):
        length = len(matches)
        for i in range(length):
            matches.append((matches[i][1], matches[i][0]))

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

    @staticmethod
    def club_max_length(clubs):
        length = len(clubs[0].name)
        for club in clubs:
            if len(club.name) > length:
                length = len(club.name)
        return length

    def points_max_length(self):
        for row in self.standings:
            if row.get_points() >= 100:
                return 3
        return 2

    def goals_scored_max_length(self):
        for row in self.standings:
            if row.get_goals_scored() >= 100:
                return 3
        return 2

    def goals_conceded_max_length(self):
        for row in self.standings:
            if row.get_goals_conceded() >= 100:
                return 3
        return 2

