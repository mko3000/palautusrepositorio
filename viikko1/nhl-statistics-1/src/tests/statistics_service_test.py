import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Semenko")

        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 16)

    def test_search_returns_none_if_no_player(self):
        player = self.stats.search("Nykänen")

        self.assertIsNone(player)

    def test_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)

        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_top(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 3)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")

    def test_top_points(self):
        players = self.stats.top(2, SortBy.POINTS)

        self.assertEqual(len(players), 3)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")

    def test_top_goals(self):
        players = self.stats.top(2, SortBy.GOALS)

        self.assertEqual(len(players), 3)

        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Kurri")

    def test_top_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)

        self.assertEqual(len(players), 3)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Lemieux")

