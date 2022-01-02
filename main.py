import json
import math
import time
import random

from player import Player
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

    game_actions = ["shoot", "pass", "run", "origin"]

    @staticmethod
    def calculate_distance(obj1, obj2):
        return math.sqrt((obj2.pos_x-obj1.pos_x)**2 + (obj2.pos_y-obj1.pos_y)**2);

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
        self.ball_pos_x = 0
        self.ball_pos_y = 0
        self.team_with_ball = None
        self.player_with_ball = None
        Game.form(first_team)
        Game.form(second_team)
        for player in second_team.best_squad:
            player.pos_x = 100-player.pos_x
            player.pos_y = 50-player.pos_y
        for pl in self.team1.best_squad:
            if pl.position == "cf":
                self.ball_pos_x = pl.pos_x
                self.ball_pos_y = pl.pos_y
                self.player_with_ball = pl

    def shoot(self, player):
        # get the opponent team
        y = 25
        if player.team.name == self.team1.name:
            opponent_team = self.team2
            x = 100
        else:
            opponent_team = self.team1
            x = 0

        # get the goalkeeper of the opponent team
        opponent_gk = opponent_team.best_squad[0]

        # check to see if there are opponent team players on the path of ball --> goals

        # 1) calculate the distance between the player and the goals (=c)
        # 2) calculate the distance between the opp_player and the goals (=a)
        # 3) calcluate the distance between the opp_player and the player (=b)
        # 4) calculate the distance between the opp_player and the ball-to-goal path (=h)

        # 1)
        c = math.sqrt((x-player.pos_x)**2 + (y-player.pos_y)**2)
        opp_players = []
        for opp_player in opponent_team.best_squad:
            # 2)
            a = math.sqrt((x-opp_player.pos_x)**2 + (y-opp_player.pos_y)**2)
            b = math.sqrt((opp_player.pos_x-player.pos_x)**2 + (opp_player.pos_y-player.pos_y))
            proj = (b**2 + c**2 - a**2)/(2*c);
            h = math.sqrt(b**2 - proj**2)
            if h <= 5:
                opp_players.append(player)
        opp_players.sort()

        # the shot can be blocked(30%)
        generator = math.random(0, 100)
        if generator < 30:
            # the shot is blocked
            opp_player = random.choice(opp_players)
            self.ball_pos_x = opp_player.pos_x
            self.ball_pos_y = opp_player.pos_y
            self.player_with_ball = opp_player
            print(f"{opp_player.name} blocked the shot!")
        else:
            gk_skill = opponent_gk.skill
            player_skill = player.skill
            generator = random.randint(0, 100)
            if generator < player_skill:
                # the goalkeeper might save it
                generator = random.randint(0, 100)
                if generator < player_skill-gk_skill+50:
                    self.ball_pos_y = y
                    self.ball_pos_x = x
                    print("GOAL")
                else:
                    # gk saved it
                    self.ball_pos_y = y
                    self.ball_pos_x = x
                    self.player_with_ball = opponent_gk
                    print("save")
            else:
                print("MISSED")
                self.ball_pos_y = y
                self.ball_pos_x = x
                self.player_with_ball = opponent_gk
    def pass_ball(self, player, teammate):
        if player.club == self.team1.name:
            opponent_team = self.team2
        else:
            opponent_team = self.team1

        # check if the pass is intercepted
        # 1) calculate the distance between the player and the goals (=c)
        # 2) calculate the distance between the opp_player and the goals (=a)
        # 3) calculate the distance between the opp_player and the player (=b)
        # 4) calculate the distance between the opp_player and the ball-to-goal path (=h)

        # 1)
        c = math.sqrt((teammate.pos_x-player.pos_x)**2 + (teammate.pos_y-player.pos_y)**2)
        opp_players = []
        for opp_player in opponent_team.best_squad:
            # 2)
            a = math.sqrt((teammate.pos_x-opp_player.pos_x)**2 + (teammate.pos_y-opp_player.pos_y)**2)
            b = math.sqrt((opp_player.pos_x-player.pos_x)**2 + (opp_player.pos_y-player.pos_y))
            proj = (b**2 + c**2 - a**2)/(2*c);
            h = math.sqrt(abs(b**2 - proj**2))
            if 15 >= h >= 0:
                opp_players.append(player)
        # opp_players.sort()

        # the pass can be intercepted with 30% probability

        generator = random.randint(0,100)
        if generator < 10 and opp_players:
            # the ball is intercepted
            opp_player = random.choice(opp_players)
            self.ball_pos_x = opp_player.pos_x
            self.ball_pos_y = opp_player.pos_y
            print(f"The ball is intercepted by {opp_player.name}")
            self.player_with_ball = opp_player
        else:
            self.ball_pos_x = teammate.pos_x
            self.ball_pos_y = teammate.pos_y
            self.player_with_ball = teammate

    def play(self):
        """
        On each turn the player with the ball can either pass the ball, shoot the ball or go forward.
        1) the player shoots the ball if the distance from the opponent goals is 20 meters or less.
        2) the player passes the ball to the one who is the most free and the distance between the 2 players needs to be
           less than 30 meters
        3) the player goes forward if there is no optimal way to pass the ball or shoot it

        On each turn the player with no ball can either go to its origin position or follow the opponent with the ball
        1) The player follows his opponent with the ball if the distance between the players is 20 meters or less. If
           the distance is larger than 20 meters and there are no other players in that radius, the closest player needs
           to follow the opponent with the ball.
        2) The player goes to his origin position if he can't follow anyone.

        :return: void
        """

        all_players = self.team1.best_squad+self.team2.best_squad
        for current_player in all_players:
            if current_player.club == self.team1.name:
                current_club = self.team1
                opponent_club = self.team2
            else:
                current_club = self.team2
                opponent_club = self.team1
            if current_player.name == self.player_with_ball.name:
                print(f"Player with the ball is {current_player.name}")
                # check if the player can shoot
                y = 25
                if current_player.club == self.team1.name:
                    x = 100
                else:
                    x = 0
                # get the distance between the player position and the opponent goals position
                distance = math.sqrt((y-current_player.pos_y)**2 + (x - current_player.pos_x)**2)

                # get all the teammates within 15 meter radius
                close_teammates = []
                for teammate in current_club.best_squad:
                    if teammate.name != current_player.name and Game.calculate_distance(teammate, current_player) < 15:
                        close_teammates.append(teammate)

                if distance < 20:
                    print("distance less than 20")
                    # if the distance is less than 20, then
                    # 1) If there are no players close to him, he will shoot
                    # 2) If there are players close to him(15m), he will shoot(90%) or pass the ball(10%)

                    if not close_teammates:
                        # shoot
                        self.shoot(current_player);
                        print(f"{current_player.name} shoots!")
                    else:
                        teammate = random.choice(close_teammates)
                        generator = random.randint(0, 100)
                        if generator > 90:
                            # pass the ball
                            self.pass_ball(current_player, teammate)
                            pass
                        else:
                            # shoot the ball
                            self.shoot(current_player)
                            print(f"{current_player.name} shoots!")
                            pass
                else:
                    if not close_teammates:
                        # go forward
                        if current_club.name == self.team1.name:
                            direction = 1
                        else:
                            direction = -1
                        current_player.pos_x += (direction*1)
                        print(f"{current_player.name} running with the ball!")
                        for pl in opponent_club.best_squad:
                            if Game.calculate_distance(pl, current_player) <= 5 and pl.club != current_player.club:
                                if math.sqrt((y-current_player.pos_y)**2 + (x-current_player.pos_x)**2) <= 20:
                                    self.shoot(current_player)
                                else:
                                    teammate = random.choice(close_teammates)
                                    self.pass_ball(current_player, teammate)
                    else:
                        teammate = random.choice(close_teammates)
                        self.pass_ball(current_player, teammate)
                        print(f"{current_player.name} passed the ball to {teammate.name}!")
                        # pass the ball to the selected teammate
            else:

                if current_player.club != self.player_with_ball.club:
                    if Game.calculate_distance(current_player, self.player_with_ball) <= 20:
                        # follow the player with ball
                        dx = current_player.pos_x - self.player_with_ball.pos_x
                        dy = current_player.pos_y - self.player_with_ball.pos_y
                        current_player.pos_x += dx/2
                        current_player.pos_y += dy/2

                        if Game.calculate_distance(current_player, self.player_with_ball) <= 5:
                            # 50% chance that the ball will be recovered
                            generator = random.randint(0, 100)
                            if generator < 50:
                                self.ball_pos_x = current_player.pos_x
                                self.ball_pos_y = current_player.pos_y
                                print(f"{current_player.name} recovered the ball!")
                                self.player_with_ball = current_player








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
print("Game starts!")
for _ in range(30):
    game.play()

