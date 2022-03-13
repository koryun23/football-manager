from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
base_tournament_url = "https://www.fifaratings.com/league/"
def parse_tournament(tournament):
    url = base_tournament_url + tournament
    driver.get(url)
