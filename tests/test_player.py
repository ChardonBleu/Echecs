import unittest

from application.models.player import Player


class TestPlayer(unittest.TestCase):
    """[summary]

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        """Create an instance of Player
        """
        self.player = Player("Judit", "Polgar", "1976", "F", "2735")
        self.serialized_player = {'first_name': 'Judit',
                                  'last_name': 'Polgar',
                                  'birth_date': '1976',
                                  'sexe': 'F',
                                  'ranking': '2735'}

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

if __name__ == "__main__":
    unittest.main()
