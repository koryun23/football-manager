import json
import time
import random

# from player import Player
from club import Club
from tournament import Tournament
from load_data import *



class Game:
    formation_4_3_3 = {
        "gk": [[0, 25]],
        "lb": [[20, 10]],
        "rb": [[20, 40]],
        "cb": [[20, 30], [20, 20]],
        "cm": [[30,35], [30,15],[30,25]],
        "lw": [[45, 35]],
        "lm": [[45, 35]],
        "rw": [[45, 15]],
        "rm": [[45, 15]],
        "cf": [[45, 25]]
    }

    formation_4_4_2 = {
        "gk": [[0, 25]],
        "lb": [[20, 10]],
        "rb": [[20, 40]],
        "cb": [[20, 30], [20, 20]],
        "cm": [[30, 30], [30, 20]],
        "lw": [[30, 40]],
        "lm": [[30, 40]],
        "rw": [[30, 10]],
        "rm": [[30, 10]],
        "cf": [[45, 20], [45, 30]]
    }

    formation_4_2_3_1 = {
        "gk": [[0, 25]],
        "lb": [[20, 10]],
        "rb": [[20, 40]],
        "cb": [[20, 30], [20, 20]],
        "dm": [[30, 30], [30, 20]],
        "lw": [[40, 40]],
        "am": [[40, 25]],
        "rw": [[40, 10]],
        "cf": [[45, 25]]
    }

    formation_3_5_2 = {
        "gk": [[0, 25]],
        "cb": [[20, 35], [20, 25], [20, 15]],
        "cm": [[30, 35], [30, 25], [30, 15]],
        "rw": [[30, 10]],
        "rm": [[30, 10]],
        "lw": [[30, 40]],
        "lm": [[30, 40]],
        "cf": [[45, 30], [45, 20]]
    }

    @classmethod
    def form(cls, team):
        if team.formation == ["4-3-3"]:
            cms = []
            cbs = []
            has_dm = False
            for player in team.best_squad:
                if player.position == "dm":
                    player.pos_x = Game.formation_4_3_3["cm"][-1][0]
                    player.pos_y = Game.formation_4_3_3["cm"][-1][1]
                    has_dm = True
                elif player.position == "cm":
                    cms.append(player)
                elif player.position == "cb":
                    cbs.append(player)
                else:
                    player.pos_x = Game.formation_4_3_3[player.position][0][0]
                    player.pos_y = Game.formation_4_3_3[player.position][0][1]

            cms[0].pos_x = Game.formation_4_3_3["cm"][0][0]
            cms[0].pos_y = Game.formation_4_3_3["cm"][0][1]
            cms[1].pos_x = Game.formation_4_3_3["cm"][1][0]
            cms[1].pos_y = Game.formation_4_3_3["cm"][1][1]
            if not has_dm:
                cms[2].pos_x = Game.formation_4_3_3["cm"][2][0]
                cms[2].pos_y = Game.formation_4_3_3["cm"][2][1]
            cbs[0].pos_x = Game.formation_4_3_3["cb"][0][0]
            cbs[0].pos_y = Game.formation_4_3_3["cb"][0][1]
            cbs[1].pos_x = Game.formation_4_3_3["cb"][1][0]
            cbs[1].pos_y = Game.formation_4_3_3["cb"][1][1]
        elif team.formation == ["4-4-2"]:
            cfs = []
            cbs = []
            cms = []
            for player in team.best_squad:
                if player.position == "cm":
                    cms.append(player)
                elif player.position == "cb":
                    cbs.append(player)
                elif player.position == "cf":
                    cfs.append(player)
                else:
                    player.pos_x = Game.formation_4_3_3[player.position][0][0]
                    player.pos_y = Game.formation_4_4_2[player.position][0][1]
            cfs[0].pos_x = Game.formation_4_4_2["cf"][0][0]
            cfs[0].pos_y = Game.formation_4_4_2["cf"][0][1]
            cfs[1].pos_x = Game.formation_4_4_2["cf"][1][0]
            cfs[1].pos_y = Game.formation_4_4_2["cf"][1][1]
            cms[0].pos_x = Game.formation_4_4_2["cm"][0][0]
            cms[0].pos_y = Game.formation_4_4_2["cm"][0][1]
            cms[1].pos_x = Game.formation_4_4_2["cm"][1][0]
            cms[1].pos_y = Game.formation_4_4_2["cm"][1][1]
            cbs[0].pos_x = Game.formation_4_4_2["cb"][0][0]
            cbs[0].pos_y = Game.formation_4_4_2["cb"][0][1]
            cbs[1].pos_x = Game.formation_4_4_2["cb"][1][0]
            cbs[1].pos_y = Game.formation_4_4_2["cb"][1][1]
        elif team.formation == ["4-2-3-1"]:

            cbs = []
            dms = []
            for player in team.best_squad:
                if player.position == "dm":
                    dms.append(player)
                elif player.position == "cb":
                    cbs.append(player)
                else:
                    player.pos_x = Game.formation_4_2_3_1[player.position][0][0]
                    player.pos_y = Game.formation_4_2_3_1[player.position][0][1]
            cbs[0].pos_x = Game.formation_4_2_3_1["cb"][0][0]
            cbs[0].pos_y = Game.formation_4_2_3_1["cb"][0][1]
            cbs[1].pos_x = Game.formation_4_2_3_1["cb"][1][0]
            cbs[1].pos_y = Game.formation_4_2_3_1["cb"][1][1]
            dms[0].pos_x = Game.formation_4_2_3_1["dm"][0][0]
            dms[0].pos_y = Game.formation_4_2_3_1["dm"][0][1]
            dms[1].pos_x = Game.formation_4_2_3_1["dm"][1][0]
            dms[1].pos_y = Game.formation_4_2_3_1["dm"][1][1]
        elif team.formation == ["3-5-2"]:
            cbs = []
            cfs = []
            cms = []
            for player in team.best_squad:
                if player.position == "cb":
                    cbs.append(player)
                elif player.position == "cm":
                    cms.append(player)
                elif player.position == "cf":
                    cfs.append(player)
                else:
                    player.pos_x = Game.formation_3_5_2[player.position][0][0]
                    player.pos_y = Game.formation_3_5_2[player.position][0][1]
            cbs[0].pos_x = Game.formation_3_5_2["cb"][0][0]
            cbs[0].pos_y = Game.formation_3_5_2["cb"][0][1]
            cbs[1].pos_x = Game.formation_3_5_2["cb"][1][0]
            cbs[1].pos_y = Game.formation_3_5_2["cb"][1][1]
            cbs[2].pos_x = Game.formation_3_5_2["cb"][2][0]
            cbs[2].pos_y = Game.formation_3_5_2["cb"][2][1]
            cms[0].pos_x = Game.formation_3_5_2["cm"][0][0]
            cms[0].pos_y = Game.formation_3_5_2["cm"][0][1]
            cms[1].pos_x = Game.formation_3_5_2["cm"][1][0]
            cms[1].pos_y = Game.formation_3_5_2["cm"][1][1]
            cms[2].pos_x = Game.formation_3_5_2["cm"][2][0]
            cms[2].pos_y = Game.formation_3_5_2["cm"][2][1]
            cfs[0].pos_x = Game.formation_3_5_2["cf"][0][0]
            cfs[0].pos_y = Game.formation_3_5_2["cf"][0][1]
            cfs[1].pos_x = Game.formation_3_5_2["cf"][1][0]
            cfs[1].pos_y = Game.formation_3_5_2["cf"][1][1]

    def __init__(self, first_team, second_team):
        # pitch size is 50x100 m
        self.team1 = first_team
        self.team2 = second_team
        Game.form(first_team)
        Game.form(second_team)
        for player in second_team.best_squad:
            player.pos_x = 100-player.pos_x
            player.pos_y = 50-player.pos_y


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
    print(player.position + "   "+player.name + "    " + f"{[player.pos_x, player.pos_y]}")
print("\n\n\n")

print("Liverpool")
print(f"Rating:{team2_rating}")
print(f"Formation:{team2_formation}")
print("----------------------------------")
for pl in team2_squad:
    print(pl.position + "  " + pl.name + "    " + f"{[pl.pos_x, pl.pos_y]}")
print("\n\n\n")
