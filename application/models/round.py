from .match import Match


class Round:
    """[summary]
    """

    def __init__(self, num_round):
        """[summary]
        """
        
        self.round_name = "round " + str(num_round) # string
        self.match = []  # list of 4 instances of match
        self.horodatage_begin = "" # date et heure de début
        self.horodatage_end = "" # date et heure de fin

    def __str__(self):
        """[summary]
        """
        return("{}:\ndébut: {:10} - fin: {:10}\n{}".format(self.round_name, self.horodatage_begin, self.horodatage_end, self.match))

    def add_match(self, player1, player2):
        """[summary]
        """

        self.match.append(Match(player1, player2))
