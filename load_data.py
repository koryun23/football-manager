import json
from player import Player
from club import Club
from tournament import Tournament

f = open("data.json")
data = json.load(f)
premier_league_clubs = data["clubs"]
team1 = Club("", [])
team2 = Club("", [])


for club in premier_league_clubs:
    if club["name"] == "Brentford":
        team1.name = club["name"]
        pl_list = club["player_list"]
        for player in pl_list:
            print(f"{player['name']} - {player['position']}")

            new_player = Player(
                player["name"],
                player["age"],
                player["skill"],
                player["club"],
                player["position"]
            )
            team1.player_list.append(new_player)

    elif club["name"] == "Crystal Palace":

        team2.name = club["name"]
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