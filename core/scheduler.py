from core.models import MatchDay, Team, Match


def schedule(team_names, no_of_days):
    # set up the teams
    teams = []
    for team_id, a in enumerate(team_names):
        teams.append(Team(team_id, a))

    # set up the matches
    matches = set()
    for home_team in teams:
        for away_team in teams:
            if home_team != away_team:
                matches.add(Match(home_team, away_team))

    match_days = []
    for x in range(no_of_days):
        day = MatchDay(x)
        while len(day.matches) < 2:
            added_match = None
            for match in matches:
                if day.add_match(match):
                    added_match = match
                    break
            if not added_match:
                # no match to add
                break
            else:
                matches.remove(added_match)
        match_days.append(day)

    print(match_days)



