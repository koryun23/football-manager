import json
from player import Player
from club import Club
from tournament import Tournament
from load_data import *

team1_squad = team1.player_list_for_game()[0]
team1_rating = team1.player_list_for_game()[1]
print("Man City")
print(f"Rating:{team1_rating}")
print("---------------------------------")
for player in team1_squad:
    print(player)
print("\n\n\n")
team2_squad = team2.player_list_for_game()[0]
team2_rating = team2.player_list_for_game()[1]
print("Liverpool")
print(f"Rating:{team2_rating}")
print("----------------------------------")
for player in team2_squad:
    print(player)
print("\n\n\n")
