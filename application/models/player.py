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

    def __str__(self):
        """Permet d'afficher un joueur avec tous ses attributs
        """
        resume_player = ( "{:20} {:2} né(e) en: {:5} - classement: {:5}").format(self.full_name, self.sexe, self.birth_date, str(self.ranking))
        return resume_player

    @property
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

    def serialize_player(self):
        """Transforme une instance de joueurs en dictionnaire avant sauvegarde dans la BDD.

        Returns:
            dict -- 
        """
        serialized_player = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'sexe': self.sexe,
            'ranking': self.ranking
        }
        return serialized_player
