import json
import time
import random

from player import Player
from club import Club
from tournament import Tournament
from load_data import *

team1_squad = team1.player_list_for_game()[0]
team1_rating = team1.player_list_for_game()[1]
team1_formation = team1.player_list_for_game()[2]
print("Man City")
print(f"Rating:{team1_rating}")
print(f"Formation:{team1_formation}")
print("---------------------------------")
for player in team1_squad:
    print(player.position + "   "+player.name)
print("\n\n\n")
team2_squad = team2.player_list_for_game()[0]
team2_rating = team2.player_list_for_game()[1]
team2_formation = team2.player_list_for_game()[2]
print("Liverpool")
print(f"Rating:{team2_rating}")
print(f"Formation:{team2_formation}")
print("----------------------------------")
for player in team2_squad:
    print(player.position + "  " + player.name)
print("\n\n\n")
class Game:
    def __init__(self, first_team, second_team):
        #pitch size is 50x100 m
        self.team1 = first_team
        self.team2 = second_team
        team1_left_cb_pos_given = False
        for player in self.team1:
            if player.position == "gk":
                player.pos_x = 0
                player.pos_y = 25
            elif player.position[1] == "b":
                player.pos_x = 10
                if player.position[0] == "l":
                    player.pos_y = 40
                elif player.position[0] == "r":
                    player.pos_y = 10
                else:
                    if player.club.formation[0][0] == "4": #number of defenders
                        # if true, then there are 2 centre backs
                        if team1_left_cb_pos_given:
                            player.pos_y = 20
                        else:
                            player.pos_y = 30
                            team1_left_cb_pos_given = True

                    else:
                        #if false then there is 1 centre back
                        player.pos_y = 25









