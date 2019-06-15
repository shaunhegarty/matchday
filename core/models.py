class Team:
    def __init__(self, id, team_name):
        self.id = id
        self.team_name = team_name

    def __eq__(self, other):
        return self.team_name == other.team_name

    def __hash__(self):
        return hash((self.id, self.team_name))

    def __repr__(self):
        return self.team_name

class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def __eq__(self, other):
        return self.home_team == other.home_team and self.away_team == other.away_team

    def __hash__(self):
        return hash((self.home_team, self.away_team))

    def __repr__(self):
        return f'{self.home_team} vs. {self.away_team}'

    def teams(self):
        return {self.home_team, self.away_team}


class MatchDay:
    def __init__(self, day):
        self.day = day
        self.matches = []

    def __repr__(self):
        return f'Day {self.day}: {self.matches.__repr__()}\n'

    def add_match(self, match):
        if len(match.teams().intersection(self.playing_teams())) == 0:
            self.matches.append(match)
            return match
        else:
            return False

    def playing_teams(self):
        teams = set()
        for match in self.matches:
            teams.add(match.home_team)
            teams.add(match.away_team)
        return teams
