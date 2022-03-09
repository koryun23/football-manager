from game import Game
from threading import Thread
from load_data import *
from standing_row import StandingRow


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
    pairings_for_first_round = [(pairing[0], pairing[1]) for pairing in epl.pairings[0]]
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

    for result in results:
        print(result)
    for i in range(len(results)):
        # set scored goals and conceded gaols for each team
        row = epl.get_row_by_club_name(pairings_for_first_round[i][0])
        row.set_goals_scored(results[i][0])
        row.set_goals_conceded(results[i][1])
        row = epl.get_row_by_club_name(pairings_for_first_round[i][1])
        row.set_goals_scored(results[i][1])
        row.set_goals_conceded(results[i][0])
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

    epl.standings.sort(key=lambda standing_row: (-standing_row.get_points(), standing_row.get_goals_difference()))
    for row in epl.standings:
        print(f"{row.get_club().name} - points: {row.get_points()}, goals scored: {row.get_goals_scored()}, goals conceded: {row.get_goals_conceded()}")


if __name__ == "__main__":
    main()
