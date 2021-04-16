import unittest
from datetime import datetime

from application.models.tournament import Tournament
from application.models.round import Round
from application.models.match import Match
from application.models.player import Player
from application.models.playermanager import PlayerManager

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
        self.tournament = Tournament("Mon tournoi",
                                     "Ici",
                                     "Aujourd'hui",
                                     "demain",
                                     "Quel beau tournoi!", 2, 4)

        self.player_manager = PlayerManager()
        self.player_manager.players.append(Player("joueur11", "", "", "", 2000))
        self.player_manager.players.append(Player("joueur12", "", "", "", 2100))
        self.player_manager.bdd_id.append(11)
        self.player_manager.bdd_id.append(12)

        self.tournament.rounds = [Round(1)]

        self.matches = Match(self.player_manager.bdd_id[0], self.player_manager.bdd_id[1], 0, 0)

        self.tournament.rounds[0].matches.append(self.matches)

    def test_tournament_players(self):
        """teste que la méthode met bien dans l'attribut self.players de Tournament.
        """
        liste_id_players = [9, 10, 11, 12, 13, 14, 15, 16]
        self.tournament.tournament_players(liste_id_players)
        self.assertListEqual(self.tournament.players, [9, 10, 11, 12, 13, 14, 15, 16])

    def test_add_round(self):
        """Initialement dans le Setup on a un round.
        On en ajoute un second avec la méthode et on vérifie qu'on a maintenant deux round.
        """
        self.tournament.add_round()
        self.assertEqual(len(self.tournament.rounds), 2)

    def test_add_match_to_last_round(self):
        """Dans le premier round on a un match.
        On en ajoute un second et on vérifie qu'on a maintenant deux matchs.
        """
        self.tournament.add_match_to_last_round(13, 14, 0, 0)
        self.assertEqual(len(self.tournament.rounds[0].matches), 2)

    def test_update_scores(self):
        """Initialement le score du match est 0,0.
        """
        self.matches.update_score(1, 3)
        self.assertEqual(str(self.matches), str(Match(11, 12, 1, 3)))

    def test_pair_of_players(self):
        """[summary]
        """
        self.assertEqual(self.matches.pair_of_players, "j11 / j12")

    def test_close_round(self):
        """[summary]
        """
        self.assertEqual(self.tournament.rounds[0].close_round(), datetime.now().strftime("%d/%m/%Y-%H:%M"))

    def test_len_matches(self):
        """[summary]
        """
        self.assertEqual(self.tournament.rounds[0].len_matches_list, 1)


if __name__ == "__main__":
    unittest.main()
