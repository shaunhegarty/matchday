import unittest
from core.scheduler import schedule, setup_teams, setup_matches, setup_days
from core.models import MatchDay, Match, Team


class TestScheduler(unittest.TestCase):

    def test_smallest(self):
        teams = setup_teams(['Luton', 'Spurs'])
        matches = setup_matches(teams)
        self.assertEqual(len(matches), 2)
        days = setup_days(matches.copy(), 1)
        self.assertEqual(len(days), 2)
        days = setup_days(matches.copy(), 2)
        self.assertEqual(len(days), 2)
        days = setup_days(matches.copy(), 3)
        self.assertEqual(len(days), 2)

    def test_four(self):
        teams = setup_teams(['Luton', 'Spurs', 'Derby', 'Coventry'])
        matches = setup_matches(teams)
        self.assertEqual(len(matches), 12)

        days = setup_days(matches.copy(), 2)
        self.assertEqual(len(days), 6)


class ModelTests(unittest.TestCase):

    def test_add_match_success(self):
        day = MatchDay('Tuesday')
        avb = Match(Team('A'), Team('B'))
        output = day.add_match(avb)
        self.assertEqual(output, avb)

    def test_add_match_duplicate(self):
        day = MatchDay('Tuesday')
        avb1 = Match(Team('A'), Team('B'))
        avb2 = Match(Team('B'), Team('A'))
        avb3 = Match(Team('A'), Team('B'))
        self.assertEqual(day.add_match(avb1), avb1)
        self.assertEqual(day.add_match(avb2), False)
        self.assertEqual(day.add_match(avb3), False)

    def test_print(self):
        schedule(['Luton', 'Everton', 'Leicester', 'Man City', 'Derby', 'Liverpool', 'Crystal Palace', 'Spurs', 'Brighton'], 5)
