import time
from tkinter import *
from game import Game
from threading import Thread
from load_data import *

tk = Tk()
myCanvas = Canvas(tk, width=500, height=400)
myCanvas.pack()

def create_circle(x, y, r, canvas_name, fill, tag):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, fill=fill, tags=tag)


def get_team_by_name(team_name, teams):
    for team in teams:
        if team.name == team_name:
            return team
    return None


def load_new_game(team1_name, team2_name):
    premier_league = load_league("Premier League")
    # premier_league_clubs = premier_league.clubs
    teams = load_teams(team1_name, team2_name, "Premier League")
    team1 = teams[0]
    team2 = teams[1]

    team1_squad = team1.player_list_for_game()[0]
    team1_rating = team1.player_list_for_game()[1]
    team1_formation = team1.player_list_for_game()[2]

    team2_squad = team2.player_list_for_game()[0]
    team2_rating = team2.player_list_for_game()[1]
    team2_formation = team2.player_list_for_game()[2]
    game = Game(team1, team2)

    print(team1.name)
    print(f"Rating:{team1_rating}")
    print(f"Formation:{team1_formation}")
    print("---------------------------------")
    for player in team1_squad:
        print(player.position + "   " + player.name + "    " + f"{[player.pos_x, player.pos_y]}")
    print("\n\n\n")

    print(team2.name)
    print(f"Rating:{team2_rating}")
    print(f"Formation:{team2_formation}")
    print("----------------------------------")
    for pl in team2_squad:
        print(pl.position + "  " + pl.name + "    " + f"{[pl.pos_x, pl.pos_y]}")
    print("\n\n\n")
    print("Game starts!")

    return game

def run_game(game):
    game.reset_origin_positions()
    while game.minute <= 90:
        # graphics()
        game.play()
    winning_side = game.team1.name
    if game.team1_score < game.team2_score:
        winning_side = game.team2.name
    elif game.team1_score == game.team2_score:
        winning_side = None

    if winning_side:
        print(f"The game ended! {winning_side} won the game {game.team1_score} - {game.team2_score}")
    else:
        print(f"The game ended in a draw. {game.team1_score} - {game.team2_score}")

    print("The goal scorers")
    for pl in game.team1_scorers:
        print(pl.name)
    for pl in game.team2_scorers:
        print(pl.name)

    myCanvas.mainloop()
def main():
    game = load_new_game("Manchester City", "Liverpool")
    print(game.team1.name)
    print(game.team1.best_squad)
    print(game.team1.formation)
    run_game(game)


if __name__ == "__main__":
    main()
