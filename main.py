import json
from player import Player
from club import Club
from tournament import Tournament
from load_data import *

print(team1.player_list_for_game())
print(team2.player_list_for_game())
class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    def formations(self, team):
        pass