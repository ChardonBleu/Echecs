import unittest

from application.models.tournament import Tournament
from application.models.round import Match
from application.models.player import Player


class TestTournament(unittest.TestCase):
    """[summary]

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        """Create an instance of Player
        """
        self.tournament = Tournament("Mon tournoi",
                                     "Ici",
                                     "Aujourd'hui",
                                     "demain",
                                     "Quel beau tournoi!", 2, 4)
        self.tournament.rounds = []
        self.player1 = Player("joueur1", "", "", "", 2000)
        self.player2 = Player("joueur2", "", "", "", 2100)
        self.match = Match(self.player1, self.player2, 0, 0)

    def test_tournament_players(self):
        """teste que la méthode met bien dans l'attribut self.players de Tournament
        la liste passée en argument
        """
        liste_id_players = [9, 10, 11, 12, 13, 14, 15, 16]
        self.tournament.tournament_players(liste_id_players)
        self.assertListEqual(self.tournament.players, [9, 10, 11, 12, 13, 14, 15, 16])

    def test_add_round(self):
        """[summary]
        """
        initial_number_of_rounds = len(self.tournament.rounds)
        self.tournament.add_round()
        self.assertEqual(len(self.tournament.rounds), initial_number_of_rounds + 1)

    def test_add_match_to_last_round(self):
        """[summary]
        """
        self.tournament.add_round()
        initial_number_of_matches = len(self.tournament.rounds[0].matches)
        self.tournament.add_match_to_last_round(self.player1, self.player2, 0, 0)
        self.assertEqual(len(self.tournament.rounds[0].matches), initial_number_of_matches + 1)

    def test_update_scores(self):
        """[summary]
        """
        self.match.update_score(1, 3)
        self.assertEqual(str(self.match), str(Match(self.player1, self.player2, 1, 3)))


if __name__ == "__main__":
    unittest.main()
