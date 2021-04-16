import unittest

from application.models.tournament import Tournament
from application.models.round import Round
from application.models.match import Match

from application.controllers.tournamentcontroller import TournamentController


class TestTournament(unittest.TestCase):
    """[summary]

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        """Create an instance of Player
        """
        self.tournament_controller = TournamentController()
        self.tournament_controller.tournament = Tournament("Mon tournoi",
                                                           "Ici",
                                                           "Aujourd'hui",
                                                           "demain",
                                                           "Quel beau tournoi!", 2, 4)

        self.tournament_controller.tournament.rounds = [Round(1)]

        match1 = Match(11, 12, 0.5, 0.5)
        match2 = Match(13, 14, 1, 0)
        self.tournament_controller.tournament.rounds[0].matches = [match1, match2]

    def test_close_round_with_scores(self):
        """Teste la fermeture d'un round avec saisie des scores
        A la demande saisir :
            =     pour le match j11 / j12 et
            j13   pour le match j13 / j14
        """
        print(""" A la demande saisir :
                        =     pour le match j11 / j12 et
                        j13   pour le match j13 / j14""")
        scores = self.tournament_controller.close_last_round_with_scores()
        self.assertEqual(scores, {11: 0.5, 12: 0.5, 13: 1, 14: 0})


if __name__ == "__main__":
    unittest.main()
