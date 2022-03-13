import requests
import json
from bs4 import BeautifulSoup


all_data = dict()
all_data["Premier League"] = {"clubs": []}
all_data["La Liga"] = {"clubs": []}
all_data["Bundesliga"] = {"clubs": []}
#all_data["clubs"] = []

def get_data(tournament_name, team):
    url = f"https://www.fifaratings.com/team/{team}"
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    main_table = soup.find("table", {"class": "table"}).find("tbody")
    all_players = main_table.find_all("tr")
    ratings = []
    names = []
    positions = []

    for player in all_players:
        player_data = player.find_all("td")
        if len(player_data) < 5:
            continue
        player_primary_data = player_data[1]
        # get the player's names
        player_name = player_primary_data.find("span", {"class": "entry-font"})
        names.append(player_name)

        # get the player's positions
        player_position = player_primary_data.find("div", {"class": "text-nowrap"}).find("a").text
        player_position = filter_position(player_position.strip())
        positions.append(player_position)

        # get the player's ratings
        player_rating_tag = player.find_all("td")[2]
        ratings.append(player_rating_tag)
    current_team = {}
    current_team["name"] = filter_club_name(team)
    current_team["player_list"] = []
    filtered_team_name = filter_club_name(team)
    for i in range(len(names)):
        current_team["player_list"].append({"name": names[i].text, "club": filtered_team_name,"age":25, "position": positions[i].lower(), "skill": int(ratings[i].text)})

    all_data[tournament_name]["clubs"].append(current_team)

def filter_position(s):
    if s == "CDM" or s == "CAM":
        return s[1:]
    if s == "ST":
        return "CF"
    if s == "LWB":
        return "LB"
    if s == "RWB":
        return "RB"
    return s

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


epl_club_names = ["manchester-city", "liverpool", "manchester-united", "chelsea", "tottenham-hotspur", "leicester-city", "arsenal", "west-ham-united",
              "everton", "wolverhampton-wanderers", "aston-villa", "leeds-united", "newcastle-united", "southampton", "burnley", "brighton-hove-albion",
              "watford", "norwich-city", "brentford", "crystal-palace"
                  ]

la_liga_club_names = ["real-madrid", "atletico-madrid", "fc-barcelona", "sevilla-fc", "villarreal-cf", "real-sociedad", "athletic-club-de-bilbao",
                     "real-betis", "valencia-cf", "levante-ud", "granada-cf", "rc-celta", "ca-osasuna", "rcd-espanyol", "getafe-cf",
                     "elche-cf", "rcd-mallorca", "cadiz-cf", "rayo-vallecano", "deportivo-alaves"]

bundesliga_club_names = ["fc-bayern-munchen", "borussia-dortmund", "rb-leipzig", "borussia-monchengladbach", "vfl-wolfsburg", "bayer-04-leverkusen",
                        "eintracht-frankfurt", "tsg-1899-hoffenheim", "hertha-bsc", "1-fc-union-berlin", "fc-augsburg", "sc-freiburg", "vfb-stuttgart",
                        "1-fc-koln", "1-fsv-mainz-05", "dsc-arminia-bielefeld", "vfl-bochum-1848", "spvgg-greuther-furth"]

for club in epl_club_names:
    get_data("Premier League", club)

for club in la_liga_club_names:
    get_data("La Liga", club)

for club in bundesliga_club_names:
    get_data("Bundesliga", club)

with open("all_team_data.json", "w") as file:
    json.dump(all_data, file)
