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

    def add_players_to_memo_match(self, id_player1, id_player2):
        """Ajoute un tupple d'id de players dans self.memo_match
        
        Arguments;
            id_player1  (int)  --  id de la bdd d'un joueur
            id_player2  (int)  --  id de la bdd d'un autre joueur
        """
        self.memo_match.append((id_player1, id_player2))