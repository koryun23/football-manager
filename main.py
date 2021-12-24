import json
from player import Player
from club import Club
from tournament import Tournament
f = open("data.json")
data = json.load(f)

man_city = Club("Manchester City", 0, [])
liverpool = Club("Liverpool", 0, [])
premier_league_clubs = data["Premier League"]["clubs"]
for club in premier_league_clubs:
    if club["name"] == man_city.name:
        man_city.budget = club["budget"]
        man_city.player_list = club["player_list"]
    if club["name"] == liverpool.name:
        liverpool.budget = club["budget"]
        liverpool.player_list = club["player_list"]
