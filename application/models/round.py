from datetime import datetime

from .match import Match


class Round:
    """Modélise un round du tournoi d'échec
    """

    def __init__(self, num_round):
        """
        Arguments:
            num_round {int} -- Permet de nommer le round
        """
                
        self.round_name = "round " + str(num_round) # string
        self.matches = []  # list of 4 instances of match
        self.horodatage_begin = datetime.now().strftime("%d/%m/%Y-%H:%M") # date et heure de début
        self.horodatage_end = "" # date et heure de fin

    def __str__(self):
        """Pour affichage des données d'un round
        """
        return("{}:\ndébut: {:10} - fin: {:10}\n".format(self.round_name, self.horodatage_begin, self.horodatage_end))

    def add_match(self, player1, player2, score1, score2):
        """Rajoute un match au round courant avec les joueurs et les scores passés en argument
        
        Arguments:
            player1 {instance de Player} --
            player2 {instance de Player} --

            score1 {int} -- score en début de round
            score2 {int} -- score ne début de round
        """
        self.matches.append(Match(player1, player2, score1, score2))

    def close_round(self):
        """[summary]
        """
        self.horodatage_end = datetime.now().strftime("%d/%m/%Y-%H:%M")