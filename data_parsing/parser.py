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
        print(team.find("span", {"class": "entry-font"}).find("a", href=True)['href'])
        soup = get_soup(team.find("span", {"class": "entry-font"}).find("a", href=True)['href'])




parse_players("english-premier-league")
