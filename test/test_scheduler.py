import unittest
from core.scheduler import schedule


class TestScheduler(unittest.TestCase):

    def test_two(self):
        schedule(['Luton', 'Spurs', 'Derby', 'Leicester'], 6)
