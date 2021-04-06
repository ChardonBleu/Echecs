class Player:
    """[summary]
    """

    def __init__(self, first_name, last_name, birth_date, sexe, ranking):
        """[summary]
        """

        self.first_name = None  # string
        self.last_name = None  # string
        self.birth_date = None  # date
        self.sexe = None  # string
        self.ranking = None  # int > 0

    def full_name(self):
        """[summary]
        """
        return (self.first_name + self.last_name)

    def update_ranking(self, new_ranking):
        """[summary]

        Arguments:
            new_ranking {int} -- [description]
        """
        self.ranking = new_ranking
