class Match:
    """Modélise un match d'un round du tournoi d'échecs.
    Les données sont stockées sous la forme d'un tupple contenant deux listes [instance de Player, score].
    """

    def __init__(self, player1, player2, score1, score2):
        """
        Arguments:
            player1 {instance de Player} --
            player2 {instance de Player} --

            score1 {int} -- score en début de round
            score2 {int} -- score ne début de round
        """

        self.pairs = ([player1, score1], [player2, score2])  # tupple of two lists

    def __str__(self):
        """Pour affichage des joueurs et des scores d'un match
        """
        return("{:20} contre {:20} - score {:2} / {:2}".format(str(self.pairs[0][0].full_name),
                                                               str(self.pairs[1][0].full_name),
                                                               str(self.pairs[0][1]),
                                                               str(self.pairs[1][1])))

    @property
    def pair_of_players(self):
        """Permet de n'afficher que les joueurs du match sans le score.
        Utilisé au moment de la saisie des scores.
        """
        return ("j1: {:20} / j2: {:20}".format(str(self.pairs[0][0].full_name), str(self.pairs[1][0].full_name)))

    def update_score(self, new_score1, new_score2):
        """Mise à jour des scores à l'issu d'un match

        Arguments:
            new_score1 {int} -- score du joueur 1
            new_score2 {int} -- score du joueur 2
        """
        self.pairs[0][1] = new_score1
        self.pairs[1][1] = new_score2
