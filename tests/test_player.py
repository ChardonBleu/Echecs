import unittest

from application.models.player import Player
from application.models.playermanager import PlayerManager
from application.controllers.playercontroller import PlayerController
from application .views.playerview import PlayerView



class TestPlayer(unittest.TestCase):
    """[summary]

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        """Create an instance of Player
        """
        self.player = Player("Judit", "Polgar", "1976", "F", 2735)
        self.serialized_player = {'first_name': 'Judit',
                                  'last_name': 'Polgar',
                                  'birth_date': '1976',
                                  'sexe': 'F',
                                  'ranking': 2735}
        self.player_manager = PlayerManager()
        self.player_manager.players = [Player("bérénice", "", "", "", 451),
                                       Player("zoé", "",  "", "", 120),
                                       Player("hector", "", "", "", 630),
                                       Player("anatole", "", "", "", 256),
                                       Player("jules", "", "", "", 1200),
                                       Player("doris", "", "", "", 820),
                                       Player("garance", "", "", "", 567),
                                       Player("wallace", "", "", "", 973)]
        [4, 1, 6, 7, 3, 5, 8, 2]
        self.player_manager.indice = [1, 2, 3, 4, 5, 6, 7, 8]
        self.player_controller = PlayerController()

    def test_full_name(self):
        """Set a full name for this player
        """
        self.assertEqual(self.player.full_name, "Polgar Judit")

    def test_update_ranking(self):
        """update ranking's player
        """
        new_ranking = "2740"
        self.player.update_ranking(new_ranking)
        self.assertEqual(self.player.ranking, "2740")

    def test_serialize_players(self):
        """serialize player
        """
        self.assertDictEqual(self.player.serialize_player(), self.serialized_player)

    def test_deserialize_player(self):
        """Deserialize_player
        """
        self.assertEqual(str(self.player.deserialize_player(self.serialized_player)), str(self.player))
        
    def test_sort_players_by_ranking(self):
        """sort players of PlayerManager object by ranking
        """
        sorted_player_manager = PlayerManager()
        sorted_player_manager.players = [Player("jules", "", "", "", 1200),
                                 Player("wallace", "", "", "", 973),
                                 Player("doris", "", "", "", 820),
                                 Player("hector", "", "", "", 630),
                                 Player("garance", "", "", "", 567),
                                 Player("bérénice", "", "", "", 451),
                                 Player("anatole", "", "", "", 256),
                                 Player("zoé", "", "", "", 120)]
        sorted_player_manager.indice = [5, 8, 6, 3, 7, 1, 4, 2]
        self.player_controller.sort_players_by_ranking(self.player_manager)
        self.assertEqual(str(self.player_manager), str(sorted_player_manager))
        
    def test_sort_players_by_name(self):
        """sort players of PlayerManager object by ranking
        """
        sorted_player_manager = PlayerManager()
        sorted_player_manager.players = [Player("anatole", "", "", "", 256),
                                         Player("bérénice", "", "", "", 451),
                                         Player("doris", "", "", "", 820),
                                         Player("garance", "", "", "", 567),
                                         Player("hector", "", "", "", 630),
                                         Player("jules", "", "", "", 1200),
                                         Player("wallace", "", "", "", 973),
                                         Player("zoé", "", "", "", 120)]
        sorted_player_manager.indice = [4, 1, 6, 7, 3, 5, 8, 2]
        self.player_controller.sort_players_by_name(self.player_manager)
        self.assertEqual(str(self.player_manager), str(sorted_player_manager))

if __name__ == "__main__":
    unittest.main()
