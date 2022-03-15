import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.fifaratings.com/"


def get_soup(url):
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    return soup


def parse_teams(tournament_name):
    soup = get_soup(BASE_URL + "teams/" + tournament_name)
    main_table = soup.find("table", {"class": "table"})
    main_table_body = main_table.find("tbody")
    main_table_rows = main_table_body.find_all(lambda tag: tag.name == "tr" and len(tag.findChildren("td", resursive=False)) > 1)
    return main_table_rows


def parse_players(tournament_name):
    teams = parse_teams(tournament_name)
    for team in teams:
        current_team = team
        current_team_name = current_team.find("span", {"class": "entry-font"}).find("a").text
        players = parse_players_of_team(team)
        parse_single_player_of_team(players)


def parse_players_of_team(team):
    soup = get_soup(team.find("span", {"class": "entry-font"}).find("a", href=True)['href'])
    main_table = soup.find("table", {"class": "table"})
    main_table_body = main_table.find("tbody")
    main_table_rows = main_table_body.find_all(lambda tag: tag.name == "tr" and len(tag.findChildren("td", recursive=False)) > 1)
    return main_table_rows


def parse_single_player_of_team(players):
    for player in players:
        soup = get_soup(player.find("span", {"class": "entry-font"}).find("a", href=True)['href'])
        player_info = soup.find("div", {"class": "player-info"})
        name = player_info.find("h1").text.strip()

        other_info = player_info.find("div", {"class": "header-subtitle"}).find_all("p", {"class": "mb-0"})
        nationality = other_info[0].find("a").text.strip()
        team = other_info[1].find("a").text.strip()
        kit_number = other_info[2].text[other_info[2].text.index("#"):]
        best_foot = other_info[6].text[other_info[6].text.index(": ")+2:]
        print(f"Name: {name}\nNationality: {nationality}\nTeam: {team}\nKit Number: {kit_number}\nBest Foot: {best_foot}")
        print("------------------------------------------")



parse_players("english-premier-league")
