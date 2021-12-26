from player import Player


class Club:
    formation_hierarchy = [[4, 3, 3], [4, 2, 3, 1], [4, 4, 2], [3, 5, 2]]  # probably won't need

    def __init__(self, name, budget, player_list):
        self.name = name
        self.budget = budget
        self.player_list = []
        self.formation = []

    def player_list_for_game(self):
        possible_squads = []
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
        d = {"cb": cbs, "lb": lbs, "rb": rbs, "dm": dms, "cm": cms, "lm": lms, "am": ams, "rm": rms, "lw": lws,
             "rw": rws, "cf": cfs}
        for player in self.player_list:
            if player.position == "gk":
                if player.skill > gk[0].skill:
                    gk[0] = player
            else:
                d[player.position].append(player)
        squad = [gk[0]]
        cbs = sorted(cbs, key=lambda current_player: -1 * current_player.skill)
        lbs = sorted(lbs, key=lambda current_player: -1 * current_player.skill)
        rbs = sorted(rbs, key=lambda current_player: -1 * current_player.skill)
        dms = sorted(dms, key=lambda current_player: -1 * current_player.skill)
        cms = sorted(cms, key=lambda current_player: -1 * current_player.skill)
        lms = sorted(lms, key=lambda current_player: -1 * current_player.skill)
        ams = sorted(ams, key=lambda current_player: -1 * current_player.skill)
        rms = sorted(rms, key=lambda current_player: -1 * current_player.skill)
        lws = sorted(lws, key=lambda current_player: -1 * current_player.skill)
        rws = sorted(rws, key=lambda current_player: -1 * current_player.skill)
        cfs = sorted(cfs, key=lambda current_player: -1 * current_player.skill)
        if lbs and rbs and len(cbs) >= 2 and (len(cms) > 2 or (len(cms) == 2 and len(dms) >= 1)) and len(cfs) and (
                len(lws) or len(lms)) and (len(rws) or len(rms)):
            squad.append(lbs[0])
            squad.append(rbs[0])
            squad.append(cbs[0])
            squad.append(cbs[1])
            squad.append(cms[0])
            squad.append(cms[1])
            if not dms:
                squad.append(cms[2])
            else:
                squad.append(dms[0])

            if lws and lms:
                if lms[0].skill > lws[0].skill:
                    squad.append(lms[0])
                else:
                    squad.append(lws[0])
            else:
                if lws:
                    squad.append(lws[0])
                else:
                    squad.append(lms[0])

            if rws and rms:
                if rms[0].skill > rws[0].skill:
                    squad.append(rms[0])
                else:
                    squad.append(rws[0])
            else:
                if rws:
                    squad.append(rws[0])
                else:
                    squad.append(rms[0])

            squad.append(cfs[0])
            possible_squads.append(squad)
            possible_squads.append(["4-3-3"])
            all_skills = 0
            for player in squad:
                all_skills += player.skill
            ovr = all_skills // 11
            possible_squads.append([ovr])
            squad = [gk[0]]
        if lbs and rbs and len(cbs) >= 2 and len(cms) + len(dms) == 2 and (len(lws) or len(lms)) and (
                len(rws) or len(rms)) and len(cfs) >= 2:
            squad.append(lbs[0])
            squad.append(rbs[0])
            squad.append(cbs[0])
            squad.append(cbs[1])
            if lws and lms:
                if lws[0].skill > lms[0].skill:
                    squad.append(lws[0])
                else:
                    squad.append(lms[0])
            else:
                if lws:
                    squad.append(lws[0])
                else:
                    squad.append(lms[0])

            if rws and rms:
                if rws[0].skill > rms[0].skill:
                    squad.append(rws[0])
                else:
                    squad.append(rms[0])
            else:
                if rws:
                    squad.append(rws[0])
                else:
                    squad.append(rms[0])
            squad.append(cfs[0])
            squad.append(cfs[1])
            possible_squads.append(squad)
            possible_squads.append(["4-4-2"])
            all_skills = 0
            for player in squad:
                all_skills += player.skill
            ovr = all_skills // 11
            possible_squads.append([ovr])
            squad = [gk[0]]
        if len(cbs) >= 3 and (lms or lws) and (rms or rws) and len(cms) >= 3 and len(cfs) >= 2:
            squad.append(cbs[0])
            squad.append(cbs[1])
            squad.append(cbs[2])
            if lms and lws:
                if lms[0].skill > lws[0].skill:
                    squad.append(lms[0])
                else:
                    squad.append(lws[0])
            else:
                if lms:
                    squad.append(lms[0])
                else:
                    squad.append(lws[0])
            if rms and rws:
                if rms[0].skill > rws[0].skill:
                    squad.append(rms[0])
                else:
                    squad.append(rws[0])
            else:
                if rms:
                    squad.append(rms[0])
                else:
                    squad.append(rws[0])
            squad.append(cms[0])
            squad.append(cms[1])
            squad.append(cms[2])
            squad.append(cfs[0])
            squad.append(cfs[1])
            possible_squads.append(squad)
            possible_squads.append(["3-5-2"])
            all_skills = 0
            for player in squad:
                all_skills += player.skill
            ovr = all_skills // 11
            possible_squads.append([ovr])
            squad = [gk[0]]
        if lbs and rbs and len(cbs) >= 2 and len(dms) >= 2 and lws and rws and ams and cfs:
            squad.append(lbs[0])
            squad.append(rbs[0])
            squad.append(cbs[0])
            squad.append(cbs[1])
            squad.append(dms[0])
            squad.append(dms[1])
            squad.append(lws[0])
            squad.append(rws[0])
            squad.append(ams[0])
            squad.append(cfs[0])
            possible_squads.append(squad)
            possible_squads.append(["4-2-3-1"])
            all_skills = 0
            for player in squad:
                all_skills += player.skill
            ovr = all_skills // 11
            possible_squads.append([ovr])
        max_rating = float("-inf")
        best_squad = []
        for i in range(2, len(possible_squads), 3):
            if possible_squads[i][0] > max_rating:
                max_rating = possible_squads[i][0]
                best_squad = possible_squads[i - 2]
        return best_squad, max_rating
