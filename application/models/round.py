from datetime import datetime

from .match import Match


class Round:
    """Modélise un round du tournoi d'échec.

    Attributs:
        self.round_name  (string) --  nom du round
        self.matches  (list)  --  liste de 4 instances de Match
        self.horodatage_begin (datetime) -- horodatage automatique à la création du round
        self.horodatage_end (datetime) -- horodatage automatique à la fermeture du round    
    """

    def __init__(self, num_round):
        """
        Arguments:
            num_round (int) -- Permet de nommer le round
        """

        self.round_name = "round " + str(num_round)
        self.matches = []
        self.horodatage_begin = datetime.now().strftime("%d/%m/%Y-%H:%M")
        self.horodatage_end = ""

    def __str__(self):
        """Pour affichage des données d'un round
        """
        return("{}:\ndébut: {:10} - fin: {:10}".format(self.round_name, self.horodatage_begin, self.horodatage_end))

    def add_match(self, player1, player2, score1, score2):
        """Rajoute un match au round courant avec les joueurs et les scores passés en argument

        Arguments:
            player1 (int) -- bdd_id du joueur 1
            player2 (int) -- bdd id du joueur 2

            score1 (int) -- score en début de round
            score2 (int) -- score ne début de round
        """
        self.matches.append(Match(player1, player2, score1, score2))

    def close_round(self):
        """Mise à jour automatique de l'heure de fin de round lors de la saisie des scores
        """
        self.horodatage_end = datetime.now().strftime("%d/%m/%Y-%H:%M")
        return self.horodatage_end

    @property
    def len_matches_list(self):
        """Renvoie le nombre de matchs déjà créés

        Returns:
            int --
        """
        return len(self.matches)

    def serialize_round(self):
        """Transforme une instance de round en dictionnaire avant sauvegarde dans la BDD.

        Returns:
            dict -- Dictionnaire représentant un round.
        """
        serialized_round = {
            'round_name': self.round_name,
            'matches': self.matches,
            'horodatage_begin': self.horodatage_begin,
            'horodatage_end': self.horodatage_end}
        return serialized_round
