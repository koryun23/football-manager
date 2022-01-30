from player import Player


class Club:
    def __init__(self, name, player_list):
        self.name = name
        self.player_list = []
        self.formation = ""
        self.best_squad = []
    def player_list_for_game(self):
        possible_squads = []
        gk = []
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
             "rw": rws, "cf": cfs, "gk": gk}
        for player in self.player_list:
            d[player.position].append(player)
        squad = []
        gk = sorted(gk, key=lambda current_player: -1*current_player.skill)
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
        if lbs and rbs and len(cbs) >= 2 and (len(cms)+len(dms)+len(ams) >= 3) and len(cfs) and \
                len(lws) + len(lms) + len(rws) + len(rms) + len(ams) >= 2:  # 4-3-3
            squad.append(lbs[0])
            squad.append(rbs[0])
            squad.append(cbs[0])
            squad.append(cbs[1])
            centres = cms + dms + ams
            squad.append(centres[0])
            centres[0].position = "cm"
            squad.append(centres[1])
            centres[1].position = "cm"
            squad.append(centres[2])
            centres[2].position = "cm"


            # first check if it's possible to form a lw/lm rw/rm structure
            # if not check if it's possible to form a lw/lm/rw/rm lw/lm/rw/rm structure
            # if not check if it's possible to form a lw/lm/rw/rm/am lw/lm/rw/rm/am structure
            # if not check if it's possible to form a lw/lm/rw/rm/am/cf lw/lm/rw/rm/am/cf structure
            left = lws if lws else lms if lms else ams
            right = rws if rws else rms if rms else ams
            left_winger = left[0]
            left_winger.position = "lw"
            right_winger = right[0]
            right_winger.position = "rw"

            squad.append(left_winger)
            squad.append(right_winger)
            squad.append(cfs[0])
            possible_squads.append(squad)
            possible_squads.append(["4-3-3"])
            all_skills = 0
            for player in squad:
                all_skills += player.skill
            ovr = all_skills // 11
            possible_squads.append([ovr])
            squad = [gk[0]]
        if lbs and rbs and len(cbs) >= 2 and len(cms) == 2 and (len(lws) or len(lms)) and (
                len(rws) or len(rms)) and len(cfs) >= 2: # 4-4-2
            squad.append(lbs[0])
            squad.append(rbs[0])
            squad.append(cbs[0])
            squad.append(cbs[1])
            squad.append(cms[0])
            squad.append(cms[1])
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
        if len(cbs) + len(rbs) + len(lbs) >= 3 and (lms or lws) and (rms or rws) and len(cms) >= 3 and len(cfs) >= 2: # 3-5-2
            # squad.append(cbs[0])
            # squad.append(cbs[1])
            # squad.append(cbs[2])
            if len(cbs) >= 3:
                squad.append(cbs[0])
                squad.append(cbs[1])
                squad.append(cbs[2])
            elif len(cbs) == 2:
                squad.append(cbs[0])
                squad.append(cbs[0])
                if len(lbs):
                    squad.append(lbs[0])
                else:
                    squad.append(rbs[0])
            elif len(cbs) == 1:
                squad.append(cbs[0])
                if not lbs or not rbs:
                    if lbs:
                        squad.append(lbs[0])
                        squad.append(lbs[1])
                    else:
                        squad.append(rbs[0])
                        squad.append(rbs[1])
                else:
                    squad.append(lbs[0])
                    squad.append(rbs[0])




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
        if lbs and rbs and len(cbs) >= 2 and len(dms) >= 2 and (len(lws) + len(lms) + len(rws) + len(rms) >= 2) and ams and cfs:
            squad.append(lbs[0])
            squad.append(rbs[0])
            squad.append(cbs[0])
            squad.append(cbs[1])
            squad.append(dms[0])
            squad.append(dms[1])

            left = lws if lws else lms if lms else ams
            right = rws if rws else rms if rms else ams
            left_winger = left[0]
            left_winger.position = "lw"
            right_winger = right[0]
            right_winger.position = "rw"

            squad.append(left_winger)
            squad.append(right_winger)
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
        if len(possible_squads) == 0:
            print(self.name)
        max_rating = 0
        formation = None
        for i in range(2, len(possible_squads), 3):
            if possible_squads[i][0] > max_rating:
                max_rating = possible_squads[i][0]
                best_squad = possible_squads[i - 2]
                formation = possible_squads[i-1]
        self.formation = formation
        self.best_squad = best_squad
        return best_squad, max_rating, formation
