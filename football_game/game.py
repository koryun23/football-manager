import math
import random


class Game:
    formation_4_3_3 = {
        "gk": [[0, 25]],
        "lb": [[20, 10]],
        "rb": [[20, 40]],
        "cb": [[20, 30], [20, 20]],
        "cm": [[30, 35], [30, 15], [30, 25]],
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
        "lm": [[40, 40]],
        "am": [[40, 25]],
        "rw": [[40, 10]],
        "rm": [[40, 10]],
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
        return math.sqrt((obj2.pos_x - obj1.pos_x) ** 2 + (obj2.pos_y - obj1.pos_y) ** 2);

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
        for pl in team.best_squad:
            pl.orig_pos_x = pl.pos_x
            pl.orig_pos_y = pl.pos_y

    def __init__(self, first_team, second_team):
        # pitch size is 50x100 m
        self.actions = 0
        self.minute = 0  # the minute updates to minute+1 when there are 10 actions done
        self.team1_score = 0
        self.team2_score = 0
        self.team1 = first_team
        self.team2 = second_team
        self.ball_pos_x = 0
        self.ball_pos_y = 0
        self.team_with_ball = None
        self.player_with_ball = None
        self.all_players = self.team1.best_squad + self.team2.best_squad
        self.team1_scorers = []
        self.team2_scorers = []
        Game.form(first_team)
        Game.form(second_team)
        for player in second_team.best_squad:
            player.pos_x = 100 - player.pos_x
            player.pos_y = 50 - player.pos_y
        for pl in self.team1.best_squad:
            if pl.position == "cf":
                self.ball_pos_x = pl.pos_x
                self.ball_pos_y = pl.pos_y
                self.player_with_ball = pl
        self.game_events = []

    def is_saved(self, player):
        y = 25
        if player.club == self.team1.name:
            opponent_team = self.team2
            x = 100
        else:
            opponent_team = self.team1
            x = 0
        gk = opponent_team.best_squad[0] # get the goalkeeper of the opponent team
        gk_skill = gk.skill
        player_skill = player.skill
        skill_diff = gk_skill - player_skill # 4
        generator = random.randint(0, 100)
        if generator < 50 + skill_diff:
            return True
        else:
            return False

    def move_to_origin(self, diff):
        for pl in self.all_players:
            pl.pos_x = pl.orig_pos_x
            pl.pos_y = pl.orig_pos_y + diff

    def follow_origin_positions(self, player):
        dx = (player.orig_pos_x - player.pos_x) // player.skill
        dy = (player.orig_pos_y - player.pos_y) // player.skill
        player.pos_x += dx
        player.pos_y += dy

    def reset_origin_positions(self):
        for pl in self.all_players:
            pl.orig_pos_x = pl.pos_x
            pl.orig_pos_y = pl.pos_y

    def set_attacking_defending_positions(self):
        for pl in self.all_players:
            dx = 1 if pl.club == self.team1.name else -1
            pl.attacking_pos_x = pl.orig_pos_x + dx*40
            pl.attacking_pos_y = pl.orig_pos_y
            pl.defending_pos_x = pl.orig_pos_x + dx*(-10)
            pl.defending_pos_y = pl.orig_pos_y
    def shoot(self, player):
        """
        There are 2 possible outcomes: It's either a goal or not
        1) If it's a goal, then
        1.1) update the ball_position to the position of the opponent goals
        1.2) print the event on the terminal
        1.3) wait for some time
        1.4) move the players back to their origin positions
        1.5) update the ball position to the position of one of the cfs of the team that conceded the goal
        2) If it's not a goal, then
        2.1) It can be a goalkeeper save
        If it's a goalkeeper save, then
        2.1.1) update the ball position to the position of the goalkeeper that saved the ball
        2.1.2) print the event on the terminal
        2.1.3) move the defenders and midfielders to their origin positions + 20
        2.1.4) move the attackers closer to the opponent territory
        2.1.5) wait for some time and kick the ball in
        2.2) It can be a miss from the player
        If it's a miss from the player, then
        2.2.1) Update the ball position
        2.2.2) print the event on the terminal
        2.2.3) move every player to their origin positions + 20
        2.2.4) wait for some time and kick the ball in
        :param player:
        :return: void
        """
        self.game_events.append(f"{player.name} shoots!")
        print(f"{player.name} shoots!")
        y = 25
        x = 0 if player.club == self.team2.name else 100
        gk = self.team1.best_squad[0]
        opp_team = self.team1
        current_team = self.team2
        if player.club == self.team1.name:
            gk = self.team2.best_squad[0]
            opp_team = self.team2
            current_team = self.team1
        is_saved = self.is_saved(player)

        if not is_saved:  # then it's either a goal or a miss from the player
            # the possibility of a miss is (100-player.skill)%
            possibility_of_miss = 50+opp_team.best_squad[0].skill-player.skill
            generator = random.randint(0, 100)
            if generator < possibility_of_miss:  # then it's a miss from the player
                self.ball_pos_x = x
                self.ball_pos_y = 51 - player.pos_y
                self.game_events.append(f"{player.name} missed!  {self.minute}'")
                print(f"{player.name} missed!  {self.minute}'")
                self.actions+=1
                self.move_to_origin(0)
                self.player_with_ball = gk
                self.kick_ball_in(gk)
            else:  # then it's a goal
                self.ball_pos_x = x
                self.ball_pos_y = y
                self.game_events.append(f"GOAL! {player.name} scored!  {self.minute}'")
                print(f"GOAL! {player.name} scored!  {self.minute}'")
                self.actions+=1
                if self.player_with_ball.club == self.team1.name:
                    self.team1_score += 1
                    self.team1_scorers.append(self.player_with_ball)
                else:
                    self.team2_score += 1
                    self.team2_scorers.append(self.player_with_ball)

                self.move_to_origin(0)
                self.ball_pos_x = opp_team.best_squad[-1].pos_x
                self.ball_pos_y = opp_team.best_squad[-1].pos_y
                self.player_with_ball = opp_team.best_squad[-1]

        else:  # then it's a save from the goalkeeper
            self.ball_pos_x = gk.pos_x
            self.ball_pos_y = gk.pos_y
            self.player_with_ball = gk
            self.game_events.append(f"{gk.name} saved it!  {self.minute}'")
            print(f"{gk.name} saved it!  {self.minute}'")
            self.actions += 1
            # move everyone from the opponent team to their origin positions except for the attackers(cf, lw, rw)
            attackers = ["cf", "lw", "rw"]
            for pl in opp_team.best_squad:
                if pl.position not in attackers:
                    pl.pos_x = pl.orig_pos_x
                    pl.orig_pos_y = pl.orig_pos_y
            self.kick_ball_in(gk)

    def kick_ball_in(self, gk):
        current_team = self.team2
        if self.player_with_ball.club == self.team1.name:
            current_team = self.team1
        position_list = []
        for pl in current_team.best_squad:
            position_list.append(pl.pos_x)
        position_list.sort()
        position = position_list[5]  # getting the middle position
        for pl in current_team.best_squad:
            if pl.pos_x == position:
                self.player_with_ball = pl
                self.ball_pos_y = pl.pos_y
                self.ball_pos_x = pl.pos_x
                self.game_events.append(f"{gk.name} passed the ball to {pl.name}!  {self.minute}'")
                print(f"{gk.name} passed the ball to {pl.name}!  {self.minute}'")
                self.actions+=1
                break

    def pass_ball(self, player, teammate):
        if teammate.club == self.team1.name:
            dir_x = 1
        else:
            dir_x = -1
        self.ball_pos_x = teammate.pos_x
        self.ball_pos_y = teammate.pos_y
        self.player_with_ball = teammate
        self.game_events.append(f"{player.name} passed the ball to {teammate.name}  {self.minute}'")
        print(f"{player.name} passed the ball to {teammate.name}  {self.minute}'")
        self.actions+=1
        # self.player_with_ball.pos_x += dir_x*5

    def resolve_player_collisions(self):
        # check if player positions overlap
        met = set()

        for pl in self.all_players:
            if (pl.pos_x, pl.pos_y) not in met:
                met.add((pl.pos_x, pl.pos_y))
            else:
                # There are 2 players with same position
                # change the position of the current_player
                pl.pos_x += 2
                pl.pos_y += 2

        # Now there will be no collisions of players!

    def follow_player_with_ball(self, player):
        dx = (self.player_with_ball.pos_x - player.pos_x) // 5
        dy = (self.player_with_ball.pos_y - player.pos_y) // 5
        player.pos_x += dx
        player.pos_y += dy

    def is_player_close_to_opponent(self, player, dist):
        y = 25
        x = 0
        if player.club == self.team1.name:
            x = 100

        return abs(x-player.pos_x) <= dist

    def move_towards_opponent_gk(self, player):
        x = 0
        y = 25
        if player.club == self.team1.name:
            x = 100
        dx = (x - player.pos_x)//5
        dy = (y - player.pos_y)//5
        player.pos_x += dx
        player.pos_y += dy
        if self.is_out_of_bounds(player):
            player.pos_x -= dx
            player.pos_y -= dy
        self.ball_pos_x = player.pos_x
        self.ball_pos_y = player.pos_y

    def run_with_ball(self, player):
        if player.club == self.team1.name:
            dir_x = 1
        else:
            dir_x = -1
        if self.is_player_close_to_opponent(player, 0.3):
            self.move_towards_opponent_gk(player)
        else:
            player.pos_x += dir_x*5
            self.ball_pos_x = player.pos_x
        self.game_events.append(f"{player.name} running with the ball  {self.minute}'")
        print(f"{player.name} running with the ball  {self.minute}'")
        self.actions+=1

    def close_teammates(self, player, dist):
        if player.club == self.team1.name:
            team = self.team1
        else:
            team = self.team2

        close_teammates = [] # teammates that are 15 or less meters away are considered close
        for pl in team.best_squad:
            if pl.name == player.name:
                continue
            distance = Game.calculate_distance(pl, player)
            if distance <= dist:
                close_teammates.append(pl)

        return close_teammates

    def win_ball(self, player):
        self.ball_pos_x = player.pos_x
        self.ball_pos_y = player.pos_y
        self.player_with_ball = player


    def is_out_of_bounds(self, player):
        return player.pos_x < 0 or player.pos_x > 100 or player.pos_y<0 or player.pos_y>50

    def press_opponent_players(self, player):
        opponent_players = []
        for pl in self.all_players:
            if pl.club != player.club:
                opponent_players.append(pl)
        opponent_players.sort(key=lambda p : Game.calculate_distance(p, player))
        self.follow_opponent_player(player, opponent_players[0])
    def follow_opponent_player(self, pl, player):
        dx = (player.pos_x - pl.pos_x) // 12
        dy = (player.pos_y - pl.pos_y) // 12
        pl.pos_x += dx
        pl.pos_y += dy
    def follow_attacking_position(self, player):
        dx = (player.attacking_pos_x - player.pos_x) // 10
        dy = (player.attacking_pos_y - player.pos_y) // 10
        player.pos_x += dx
        player.pos_y += dy
    def follow_defending_position(self, player):
        dx = (player.defending_pos_x - player.pos_x) // 10
        dy = (player.defending_pos_y - player.pos_y) // 10
        player.pos_x += dx
        player.pos_y += dy
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

        self.resolve_player_collisions()
        self.set_attacking_defending_positions()




        for player in self.all_players:   # main loop of the play method
            attackers = ["cf", "lw", "rw", "lm", "rm", "am"]
            defenders = ["cb", "dm"]
            if player.position == "gk":
                if player.name == self.player_with_ball.name:
                    self.kick_ball_in(player)
                continue
            # self.perform_best_decision(player)
            if player.name == self.player_with_ball.name:

                if self.is_player_close_to_opponent(player, 25):
                    # generator = random.randint(0, 100)
                    # if generator < 90:
                    self.shoot(player)
                else:
                    generator = random.randint(0, 100)
                    # choose close teammate
                    teammates = self.close_teammates(player, 15)
                    teammate = None
                    if teammates:
                        teammate = random.choice(teammates)
                    if generator < 50 and teammate:  # pass the ball else run forward
                        self.pass_ball(player, teammate)
                    else:
                        self.run_with_ball(player)
            else:
                # follow the player with ball or not
                if player.club != self.player_with_ball.club:

                    distance_from_player_with_ball = Game.calculate_distance(self.player_with_ball, player)
                    if distance_from_player_with_ball <= 15:
                        if not self.close_teammates(player, 5) or len(self.close_teammates(player, 5)) < 1:
                            self.follow_player_with_ball(player)
                    elif distance_from_player_with_ball <= 10:
                        self.win_ball(player)
                    else:
                        self.follow_origin_positions(player)

                    if player.position == "cf" or player.position[1] == "w":
                        self.press_opponent_players(player)
                    else:
                        self.follow_defending_position(player)

                else:
                    if player.position not in defenders:
                        self.follow_attacking_position(player)
        self.game_events.append(f"{self.team1_score} - {self.team2_score}")
        print(f"{self.team1_score} - {self.team2_score}")
        self.minute = self.actions//4

