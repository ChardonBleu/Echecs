from ..views.roundview import RoundView


class RoundController:
    """
    Modélise le controller des rounds du tournoi
    Attributs:
        self.view  (objet RoundView)  --  instance de RoundView destinée à la saisie
                                          et l'affichage des données propres aux rounds
        self.memo_match (list)  -- liste de tupples mémorisant les couples de joueurs ayant déjà joué ensemble
    """

    def __init__(self):
        self.view = RoundView()
        self.memo_match = []
