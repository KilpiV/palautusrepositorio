import unittest
from statistics import Statistics
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_etsinta_toimii_tyhjalla(self):
        self.assertAlmostEqual(self.statistics.search(" "), None)

    def test_etsinta_toimii(self):
        self.assertEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")

    def test_luo_pelaajan(self):
        pelaaja = self.statistics.search("Lemieux")
        self.assertAlmostEqual(pelaaja.name, "Lemieux")

    def test_loytaa_tiimin(self):
        tiimi = self.statistics.team("PIT")
        pelaajat = ""
        for p in tiimi:
            pelaajat += p.__str__()
        self.assertAlmostEqual(len(tiimi), 1)
        self.assertAlmostEqual(str(self.statistics.team("PIT")[0]),'Lemieux PIT 45 + 54 = 99')
        self.assertEqual(pelaajat, "Lemieux PIT 45 + 54 = 99")

    def test_top_pisteet(self):
        paras = self.statistics.top(1)
        parasMaali = self.statistics.top(1, 2)
        parasAvustukset = self.statistics.top(1,3)
        self.assertEqual(paras[0].name, "Gretzky")
        self.assertEqual(parasMaali[0].name, "Lemieux")
        self.assertEqual(parasAvustukset[0].name, "Gretzky")