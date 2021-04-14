class Player:
    """Modélise un joueur du tournoi d'échec
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
        resume_player = ("{:20} {:2} né(e) en: {:5} - classement: {:5}").format(self.full_name,
                                                                                self.sexe,
                                                                                self.birth_date,
                                                                                str(self.ranking))
        return resume_player

    @property
    def full_name(self):
        """Construit le nom complet du joueur au format: 'nom_de_famille prénom'
        """
        return (self.last_name + " " + self.first_name)

    def update_ranking(self, new_ranking):
        """Permet de mettre à jour le classement ELO du joueur

        Arguments:
            new_ranking {int} -- nouvelle valeur du classement ELO
        """
        self.ranking = new_ranking

    def serialize_player(self):
        """Transforme une instance de joueurs en dictionnaire avant sauvegarde dans la BDD.

        Returns:
            dict -- dictionnaire représentant un joueur
        """
        serialized_player = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'sexe': self.sexe,
            'ranking': self.ranking}
        return serialized_player
    
    def deserialize_player(self, serialized_player):
        """Permet de créer une instance de classe d'un joueur à partir d'un dictionnaire
        représentant un joueur.

        Arguments:
            serialized_player {dict} -- dictionnaire représentant un joueur

        Returns:
            instance de Player
        """
        first_name = serialized_player['first_name']
        last_name = serialized_player['last_name']
        birth_date = serialized_player['birth_date']
        sexe = serialized_player['sexe']
        ranking = serialized_player['ranking']
        return Player(first_name, last_name, birth_date, sexe, ranking)
