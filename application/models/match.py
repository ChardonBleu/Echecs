class Match:
    """Modélise un match d'un round du tournoi d'échecs.
    Les données sont stockées sous la forme d'un tupple contenant deux listes [instance de Player, score]:
    
        self.pairs  (tupple)  -- tupple contenant les deux listes [instance de Player, score]
    """

    def __init__(self, player1, player2, score1, score2):
        """
        Arguments:
            player1 (int) -- bdd_id du joueur 1
            player2 (int) -- bdd id du joueur 2

            score1 (int) -- score en début de round
            score2 (int) -- score ne début de round
        """

        self.pairs = ([player1, score1], [player2, score2])

    def __str__(self):
        """Pour affichage des joueurs et des scores d'un match
        """
        return("joueur {:2}: contre joueur {:2}: - score {:2} / {:2}".format(str(self.pairs[0][0]),
                                                                             str(self.pairs[1][0]),
                                                                             str(self.pairs[0][1]),
                                                                             str(self.pairs[1][1])))

    @property
    def pair_of_players(self):
        """Permet de n'afficher que les joueurs du match sans le score.
        Utilisé au moment de la saisie des scores.
        """
        return ("j{:2} / j{:2}".format(str(self.pairs[0][0]), str(self.pairs[1][0])))

    def serialize_match(self):
        """Transforme une instance de match en dictionnaire avant sauvegarde dans la BDD.

        Returns:
            dict -- Dictionnaire représentant un match.
        """
        serialized_round = {
            'pairs': self.pairs}
        return serialized_round

