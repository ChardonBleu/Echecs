from ..views.roundview import RoundView


class RoundController:
    """
    Modélise le controller des rounds du tournoi
    """

    def __init__(self):
        """
        """
        # self.players = PlayerManager()
        self.view = RoundView()
        self.memo_match = []  # liste de tupples mémorisant les couples de joueurs ayant déjà joué ensemble
