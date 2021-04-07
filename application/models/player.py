class Player:
    """[summary]
    """

    def __init__(self, first_name, last_name, birth_date, sexe, ranking):
        """[summary]
        """

        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.birth_date = birth_date  # date
        self.sexe = sexe  # string
        self.ranking = ranking  # int > 0

    def full_name(self):
        """[summary]
        """
        return (self.first_name + " " + self.last_name)

    def update_ranking(self, new_ranking):
        """[summary]

        Arguments:
            new_ranking {int} -- [description]
        """
        self.ranking = new_ranking
        
    def __str__(self):
        """Permet d'afficher un joueur avec tous ses attributs
        """
        resume_player = (self.full_name() + " " + self.sexe + " " +
                         "né en: " + self.birth_date + " - classement: " + self.ranking)
        return resume_player
        
