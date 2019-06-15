from core.models import MatchDay, Team, Match


def schedule(team_names, matches_per_day):
    # set up the teams
    teams = setup_teams(team_names)

    # set up the matches
    matches = setup_matches(teams)

    # set up the days
    match_days = setup_days(matches, matches_per_day)

    print(match_days)


def setup_teams(team_names):
    teams = []
    for name in team_names:
        teams.append(Team(name))
    return teams


def setup_matches(teams):
    matches = set()
    for home_team in teams:
        for away_team in teams:
            if home_team != away_team:
                matches.add(Match(home_team, away_team))
    return matches


def setup_days(matches, matches_per_day):
    match_days = []
    iteration = 0
    while len(matches) > 0:
        iteration += 1
        day = MatchDay(iteration)
        while len(day.matches) < matches_per_day:
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
        if len(day.matches) > 0:
            match_days.append(day)
    return match_days
