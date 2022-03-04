import json
from player import Player
from club import Club
from tournament import Tournament


def filter_club_name(club):
    new_name = ""
    for i in range(len(club)):
        if i == 0 or club[i - 1] == "-":
            new_name += club[i].upper()
        elif club[i] == "-":
            new_name += " "
        else:
            new_name += club[i]
    return new_name


def load_teams_from_json(tournament_name):
    f = open("data.json")
    data = json.load(f)
    league_clubs = data[tournament_name]["clubs"]
    print(league_clubs)
    return league_clubs


def get_clubs_array():
    club_names = ["manchester-city", "liverpool", "manchester-united", "chelsea", "tottenham-hotspur", "leicester-city",
                  "arsenal", "west-ham-united",
                  "everton", "wolverhampton-wanderers", "aston-villa", "leeds-united", "newcastle-united",
                  "southampton", "burnley", "brighton-hove-albion",
                  "watford", "norwich-city", "brentford", "crystal-palace"
                  ]
    clubs = []
    for club in club_names:
        clubs.append(Club(filter_club_name(club), [], ""))
    return clubs


def load_league(tournament_name):  # must return an array containing all Club objects in the current tournament
    league = Tournament(tournament_name, get_clubs_array())
    league.generate_standings()
    league.generate_pairings()
    league.format_pairings()
    return league


def load_teams(team1_name, team2_name):
    league_clubs = load_teams_from_json("Premier League")
    team1 = Club(team1_name, [], "")
    team2 = Club(team2_name, [], "")
    for club in league_clubs:
        if club["name"] == team1_name:
            pl_list = club["player_list"]
            for player in pl_list:
                new_player = Player(
                    player["name"],
                    player["age"],
                    player["skill"],
                    player["club"],
                    player["position"]
                )
                team1.player_list.append(new_player)
        elif club["name"] == team2_name:
            pl_list = club["player_list"]
            for player in pl_list:
                new_player = Player(
                    player["name"],
                    player["age"],
                    player["skill"],
                    player["club"],
                    player["position"]
                )
                team2.player_list.append(new_player)
    return team1, team2
