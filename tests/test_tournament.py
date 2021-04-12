import unittest

from application.models.tournament import Tournament
from application.models.round import Round


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
    
    def test_tournament_players(self):
        """teste que la méthode met bien dans l'attribut self.players de Tournament
        la liste passée en argument
        """
        liste_id_players = [9, 10, 11, 12, 13, 14, 15, 16]
        self.tournament.tournament_players(liste_id_players)
        self.assertListEqual(self.tournament.players, [9, 10, 11, 12, 13, 14, 15, 16])

    def test_tournament_rounds(self):
        """Vérifie que la méthode met bien dans l'attribut self.rounds
        le nombre d'objets contenu dans l'attribut self.number_rounds
        """
        self.assertEqual(len(self.tournament.tournament_rounds()), self.tournament.number_rounds)


if __name__ == "__main__":
    unittest.main()
