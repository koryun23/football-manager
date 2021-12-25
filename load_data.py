import json
from player import Player
from club import Club
from tournament import Tournament

f = open("data.json")
data = json.load(f)
premier_league_clubs = data["Premier League"]["clubs"]
team1 = Club("", 0, [])
team2 = Club("", 0, [])


#premier_league_clubs_names = {"Manchester City": Club("", 0, []), "Liverpool":Club("", 0, []), "Chelsea":Club("", 0, []), "Arsenal":Club("", 0, []), "West Ham":Club("", 0, []), "Manchester United":Club("", 0, []), "Tottenham":Club("", 0, []), "Wolves":Club("", 0, []), "Leicester":Club("", 0, []),"Aston Villa":Club("", 0, []), "Crystal Palace":Club("", 0, []), "Brentford":Club("", 0, []), "Brighton":Club("", 0, []), "Everton":Club("", 0, []), "Southampton":Club("", 0, []), "Leeds":Club("", 0, []), "Burnley":Club("", 0, []), "Watford":Club("", 0, []), "Newcastle":Club("", 0, []), "Norwich":Club("", 0, [])}
for club in premier_league_clubs:
    if club["name"] == "Manchester City":
        team1.name = club["name"]
        team1.budget = club["budget"]
        team1.player_list =  club["player_list"]
    elif club["name"] == "Liverpool":
        team2.name = club["name"]
        team2.budget = club["budget"]
        team2.player_list =  club["player_list"]