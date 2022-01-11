import time
from game import Game
from player import Player
from tournament import Tournament
from club import Club
from load_data import *


team1_squad = team1.player_list_for_game()[0]
team1_rating = team1.player_list_for_game()[1]
team1_formation = team1.player_list_for_game()[2]

team2_squad = team2.player_list_for_game()[0]
team2_rating = team2.player_list_for_game()[1]
team2_formation = team2.player_list_for_game()[2]
game = Game(team1, team2)

print("Man City")
print(f"Rating:{team1_rating}")
print(f"Formation:{team1_formation}")
print("---------------------------------")
for player in team1_squad:
    print(player.position + "   " + player.name + "    " + f"{[player.pos_x, player.pos_y]}")
print("\n\n\n")

print("Liverpool")
print(f"Rating:{team2_rating}")
print(f"Formation:{team2_formation}")
print("----------------------------------")
for pl in team2_squad:
    print(pl.position + "  " + pl.name + "    " + f"{[pl.pos_x, pl.pos_y]}")
print("\n\n\n")
print("Game starts!")
while game.minute <= 45:
    game.play()
    time.sleep(1)
