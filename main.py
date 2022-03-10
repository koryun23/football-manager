from threading import Thread

from game import Game
from load_data import *


def get_team_by_name(team_name, teams):
    for team in teams:
        if team.name == team_name:
            return team
    return None


def load_new_game(team1_name, team2_name, tournament_name):
    # premier_league = load_league(tournament_name)
    # premier_league_clubs = premier_league.clubs
    teams = load_teams(team1_name, team2_name, tournament_name)
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


results = []
def run_game(game):
    game.reset_origin_positions()
    while game.minute <= 90:
        # graphics()
        game.play()

    results.append((game.team1_score, game.team2_score))

def main():
    epl = load_league("Premier League")
    pairings_for_first_round = [pairing for pairing in epl.pairings[0]]
    threads = []
    for pair in pairings_for_first_round:
        game = load_new_game(pair[0].name, pair[1].name, epl.name)
        threads.append(Thread(target=run_game, args=(game,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    for thread in threads:
        if not thread.is_alive():
            thread.handled = True

    for i in range(len(results)):
        print(i, len(pairings_for_first_round))
        row = epl.get_row_by_club_name(pairings_for_first_round[i][0])
        row.set_goals_scored(row.get_goals_scored() + results[i][0])
        row.set_goals_conceded(row.get_goals_conceded() + results[i][1])
        row.set_matches_played(row.get_matches_played() + 1)
        if results[i][0] > results[i][1]: row.set_matches_won(row.get_matches_won() + 1)
        elif results[i][0] < results[i][1]: row.set_matches_lost(row.get_matches_lost() + 1)
        else: row.set_matches_drawn(row.get_matches_drawn() + 1)
        row = epl.get_row_by_club_name(pairings_for_first_round[i][1])
        row.set_goals_scored(results[i][1])
        row.set_goals_conceded(results[i][0])
        row.set_matches_played(row.get_matches_played() + 1)
        if results[i][0] < results[i][1]: row.set_matches_won(row.get_matches_won() + 1)
        elif results[i][0] > results[i][1]: row.set_matches_lost(row.get_matches_lost() + 1)
        else: row.set_matches_drawn(row.get_matches_drawn() + 1)
        winning_side = None
        if results[i][0] > results[i][1]:
            winning_side = pairings_for_first_round[i][0]
        elif results[i][0] < results[i][1]:
            winning_side = pairings_for_first_round[i][1]
        if winning_side:
            for row in epl.standings:
                if winning_side == row.get_club():
                    row.set_points(row.get_points() + 3)
        else:
            for row in epl.standings:
                if pairings_for_first_round[i][0] == row.get_club() or pairings_for_first_round[i][1] == row.get_club():
                    row.set_points(row.get_points() + 1)
    epl.standings.sort(key=lambda standing_row: (-standing_row.get_points(), -standing_row.get_goals_scored(), -standing_row.get_goals_difference()))
    print("-------------------------------------------------------------")
    for i in range(len(epl.standings)):
        club_name = epl.standings[i].get_club().name
        club_points = epl.standings[i].get_points()
        club_goals_scored = epl.standings[i].get_goals_scored()
        club_goals_conceded = epl.standings[i].get_goals_conceded()
        club_matches_played = epl.standings[i].get_matches_played()
        club_matches_won = epl.standings[i].get_matches_won()
        club_matches_lost = epl.standings[i].get_matches_lost()
        club_matches_drawn = epl.standings[i].get_matches_drawn()
        print(f"{i+1}) {club_name} - points: {club_points}, goals scored: {club_goals_scored}, goals conceded: {club_goals_conceded}, matches played: {club_matches_played} matches won: {club_matches_won}, matches lost: {club_matches_lost}, matches drawn: {club_matches_drawn}")

if __name__ == "__main__":
    main()
