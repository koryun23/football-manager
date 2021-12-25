from player import Player


class Club:
    def __init__(self, name, budget, player_list):
        self.name = name
        self.budget = budget
        self.player_list = player_list
        self.formation = []
    def player_list_for_game(self):
        list = [self.player_list[0]]
        for player in self.player_list:
            if player["position"] == "gk":
                if player["skill"] > list[0]["skill"]:
                    list[0] = player
            else:
                break
        return list
