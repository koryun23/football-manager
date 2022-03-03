import json
from player import Player
from club import Club
from tournament import Tournament

def filter_club_name(club):
    new_name = ""
    for i in range(len(club)):
        if i == 0 or club[i-1] == "-":
            new_name += club[i].upper()
        elif club[i] == "-":
            new_name += " "
        else:
            new_name += club[i]
    return new_name

f = open("data.json")
data = json.load(f)
premier_league_clubs = data["clubs"]
club_names = ["manchester-city", "liverpool", "manchester-united", "chelsea", "tottenham-hotspur", "leicester-city", "arsenal", "west-ham-united",
              "everton", "wolverhampton-wanderers", "aston-villa", "leeds-united", "newcastle-united", "southampton", "burnley", "brighton-hove-albion",
              "watford", "norwich-city", "brentford", "crystal-palace"
              ]
clubs = []
for club in club_names:
    clubs.append(Club(filter_club_name(club), [], ""))
epl = Tournament("Premier League", clubs)
epl.generate_standings()
epl.generate_pairings()
epl.format_pairings()
epl.print_pairings()
# epl.print_clubs()
team1 = epl.clubs[0]
team2 = epl.clubs[1]
for club in premier_league_clubs:
    if club["name"] == team1.name:
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
    elif club["name"] == team2.name:
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
