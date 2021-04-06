import unittest

from application.models.player import Player


class TestPlayer(unittest.TestCase):
    """[summary]

    Arguments:
        unittest {[type]} -- [description]
    """
    
    def test_full_name(self):
        """Create a player and set a full name for this player
        """        
        player = Player("Judit", "Polgar", "1976", "F", "2735")
        self.assertEqual(player.full_name(), "Judit Polgar")
        
    def test_update_ranking(self):
        """Create a player and update his ranking
        """
        player = Player("Judit", "Polgar", "1976", "F", "2735")
        new_ranking = "2740"
        player.update_ranking(new_ranking)
        self.assertEqual(player.ranking, "2740")


if __name__ == "__main__":
    unittest.main() 