from ..views.roundview import RoundView
from ..models.round import Round


class RoundController:
    """
    Modélise le controller des rounds du tournoi
    
    """

    def __init__(self):
        """[summary]
        """
        # self.players = PlayerManager()
        self.view = RoundView()