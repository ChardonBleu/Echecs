class Match:
    """[summary]
    """

    def __init__(self, player1, player2, score1=0, score2=0):
        """[summary]

        Arguments:
            player1 {[type]} -- [description]
            player2 {[type]} -- [description]

        Keyword Arguments:
            score1 {int} -- [description] (default: {0})
            score2 {int} -- [description] (default: {0})
        """

        self.pairs = ([player1, score1], [player2, score2])  # tupple of two lists

    def __str__(self):
        """[summary]
        """
        return("{:20} contre {:20} - score {:2} / {:2}".format(str(self.pairs[0][0].full_name), str(self.pairs[1][0].full_name), str(self.pairs[0][1]), str(self.pairs[1][1])))

    def update_score(self, new_score1, new_score2):
        """[summary]

        Arguments:
            new_score1 {[type]} -- [description]
            new_score2 {[type]} -- [description]
        """
        self.pairs[0][1] = new_score1
        self.pairs[1][1] = new_score2
