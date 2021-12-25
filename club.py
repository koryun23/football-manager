from player import Player


class Club:
    formation_hierarchy = [[4, 3, 3], [4, 2, 3, 1], [4, 4, 2], [3, 2, 3, 2]]

    def __init__(self, name, budget, player_list):
        self.name = name
        self.budget = budget
        self.player_list = player_list
        self.formation = []

    def player_list_for_game(self):
        gk = [self.player_list[0]]
        cbs = []
        lbs = []
        rbs = []
        dms = []
        cms = []
        lms = []
        ams = []
        rms = []
        lws = []
        rws = []
        cfs = []
        d = {"cb":cbs, "lb":lbs, "rb":rbs, "dm":dms, "cm":cms, "lm":lms,"am":ams, "rm":rms, "lw":lws, "rw":rws, "cf":cfs}
        for player in self.player_list:
            if player["position"] == "gk":
                if player["skill"] > gk[0]["skill"]:
                    gk[0] = player
            else:
                d[player["position"]].append(player)

        cbs = sorted(cbs, key=lambda current_player: -1*current_player["skill"])
        lbs = sorted(lbs, key=lambda current_player: -1*current_player["skill"])
        rbs = sorted(rbs, key=lambda current_player: -1*current_player["skill"])
        dms = sorted(dms, key=lambda current_player: -1*current_player["skill"])
        cms = sorted(cms, key=lambda current_player: -1*current_player["skill"])
        lms = sorted(lms, key=lambda current_player: -1*current_player["skill"])
        ams = sorted(ams, key=lambda current_player: -1*current_player["skill"])
        rms = sorted(rms, key=lambda current_player: -1*current_player["skill"])
        lws = sorted(lws, key=lambda current_player: -1*current_player["skill"])
        rws = sorted(rws, key=lambda current_player: -1*current_player["skill"])
        cfs = sorted(cfs, key=lambda current_player: -1*current_player["skill"])
        print(cbs)
        print(lbs)
        print(rbs)
        print(dms)
        print(cms)
        print(lms)
        print(ams)
        print(rms)
        print(lws)
        print(rws)
        print(cfs)


