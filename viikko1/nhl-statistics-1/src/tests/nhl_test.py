import unittest
from statistics_service import StatisticsService, SortBy
from player import Player
from enum import Enum

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
       
    def test_search(self):
        self.stats.search("Kurri")
        self.stats.search("Selanne")
    
    def test_team(self):
        self.stats.team("EDM")
        self.stats.team("ABC")
    
    def test_top(self):
        self.stats.top(4, SortBy.POINTS)
        self.stats.top(4, SortBy.GOALS)
        self.stats.top(4, SortBy.ASSISTS)