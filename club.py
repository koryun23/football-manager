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
        rms = []
        lws = []
        rws = []
        cfs = []
        for player in self.player_list:
            if player["position"] == "gk":
                if player["skill"] > gk[0]["skill"]:
                    gk[0] = player
            elif player["position"] == "cb":
                cbs.append(player)
            elif player["position"] == "lb":
                lbs.append(player)
            elif player["position"] == "rb":
                rbs.append(player)
            elif player["position"] == "dm":
                dms.append(player)
            elif player["position"] == "cm":
                cms.append(player)
            elif player["position"] == "lm":
                lms.append(player)
            elif player["position"] == "rm":
                rms.append(player)
            elif player["position"] == "lw":
                lws.append(player)
            elif player["position"] == "rw":
                rws.append(player)
            elif player["position"] == "cf":
                cfs.append(player)


        cbs = sorted(cbs, key=lambda current_player: current_player["skill"])
        lbs = sorted(lbs, key=lambda current_player: current_player["skill"])
        rbs = sorted(rbs, key=lambda current_player: current_player["skill"])
        dms = sorted(dms, key=lambda current_player: current_player["skill"])
        cms = sorted(cms, key=lambda current_player: current_player["skill"])
        lms = sorted(lms, key=lambda current_player: current_player["skill"])
        rms = sorted(rms, key=lambda current_player: current_player["skill"])
        lws = sorted(lws, key=lambda current_player: current_player["skill"])
        rws = sorted(rws, key=lambda current_player: current_player["skill"])
        cfs = sorted(cfs, key=lambda current_player: current_player["skill"])
        print(cbs)
        print(lbs)
        print(rbs)
        print(dms)
        print(cms)
        print(lms)
        print(rms)
        print(lws)
        print(rws)
        print(cfs)


