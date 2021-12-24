import json
from player import Player
from club import Club
from tournament import Tournament

f = open("data.json")
data = json.load(f)
premier_league_clubs = data["Premier League"]["clubs"]



premier_league_clubs_names = {"Manchester City": Club("", 0, []), "Liverpool":Club("", 0, []), "Chelsea":Club("", 0, []), "Arsenal":Club("", 0, []), "West Ham":Club("", 0, []), "Manchester United":Club("", 0, []), "Tottenham":Club("", 0, []), "Wolves":Club("", 0, []), "Leicester":Club("", 0, []),"Aston Villa":Club("", 0, []), "Crystal Palace":Club("", 0, []), "Brentford":Club("", 0, []), "Brighton":Club("", 0, []), "Everton":Club("", 0, []), "Southampton":Club("", 0, []), "Leeds":Club("", 0, []), "Burnley":Club("", 0, []), "Watford":Club("", 0, []), "Newcastle":Club("", 0, []), "Norwich":Club("", 0, [])}
team1 = premier_league_clubs_names["Manchester City"]
team1.name = "Manchester City"
team1.budget = premier_league_clubs
team2 = premier_league_clubs_names["Liverpool"]