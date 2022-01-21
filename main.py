import time
from tkinter import *
from game import Game
from player import Player
from tournament import Tournament
from club import Club
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
team1_player_tag_dict = {}
team2_player_tag_dict = {}

counter1 = 1
for pl in game.team1.best_squad:
    team1_player_tag_dict[pl.name] = f"team1player{counter1}"
    counter1 += 1
counter2 = 1
for pl in game.team2.best_squad:
    team2_player_tag_dict[pl.name] = f"team2player{counter2}"

game.reset_origin_positions()
for i in range(100):
    counter1 = 1
    counter2 = 1

    #     # First we need to remove the circles
    for i in range(1, 3):
        for j in range(1, 12):
            myCanvas.delete(f"team{i}player{j}")
    myCanvas.delete("ball")
    for pl in game.team1.best_squad:
        current_position_x = pl.pos_x
        current_position_y = pl.pos_y
        create_circle(5 * current_position_x, 8 * (50 - current_position_y), 10, myCanvas, "lightblue",
                      team1_player_tag_dict[pl.name])
        counter1 += 1
    for pl in game.team2.best_squad:
        current_position_x = pl.pos_x
        current_position_y = pl.pos_y
        create_circle(5 * current_position_x, 8 * (50 - current_position_y), 10, myCanvas, "red",
                      team2_player_tag_dict[pl.name])

    create_circle(5 * game.ball_pos_x, 8 * (50 - game.ball_pos_y), 5, myCanvas, "white", "ball")
    tk.update()
    time.sleep(0.1)
    game.play()

myCanvas.mainloop()
