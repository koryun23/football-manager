import json
from typing import Dict, List

from player import Player
from club import Club
from tournament import Tournament
from team_not_found_exception import TeamNotFoundException


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
    return league_clubs  # list of maps containing information about teams in a league


def get_clubs_array():  # returns an array consisting of Club objects having a name and empty player list
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


def load_league(tournament_name):  # creates and returns a new tournament
    teams_as_list_of_maps = load_teams_from_json(tournament_name)
    clubs_array = get_clubs_array()
    # will perhaps need to fill the player list of every club in the current tournament here
    for j in range(len(clubs_array)):
        current_team = None
        for i in range(len(teams_as_list_of_maps)):
            if teams_as_list_of_maps[i]["name"] == clubs_array[j].name:
                current_team = teams_as_list_of_maps[i]
                break
        for i in range(len(current_team["player_list"])):
            clubs_array[j].player_list.append(Player(
                current_team["player_list"][i]["name"],
                current_team["player_list"][i]["age"],
                current_team["player_list"][i]["skill"],
                current_team["player_list"][i]["club"],
                current_team["player_list"][i]["position"]
            ))
    league = Tournament(tournament_name, clubs_array)
    league.generate_standings()
    league.generate_pairings()
    league.format_pairings()
    return league


def load_teams(team1_name, team2_name, tournament_name):
    league = load_league(tournament_name)
    team1 = None
    team2 = None
    for club in league.clubs:
        if club.name == team1_name:
            team1 = club
        elif club.name == team2_name:
            team2 = club
    if team1 is None:
        raise TeamNotFoundException(team1_name)
    if team2 is None:
        raise TeamNotFoundException(team2_name)
    return team1, team2
