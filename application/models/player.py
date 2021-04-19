class Player:
    """Modélise un joueur du tournoi d'échec
    """

    def __init__(self, first_name, last_name, birth_date, sexe, ranking, score=0):
        """
        Arguments:
            first_name (string)
            last_name (string)
            birth_date (string) -- année de naissance du joueur
            sexe (string) -- F ou M
            ranking (int)  -- Classement ELO (entier > 0)

        Keyword Arguments:
            score (int) -- score du joueur au cours du tournoi (default: {0})
        """

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sexe = sexe
        self.ranking = ranking
        self.tournament_score = score

    def __str__(self):
        """Permet d'afficher un joueur avec tous ses attributs
        """
        resume_player = ("{:20} {:2} né(e) en: {:5} - classement: {:5} - score tournoi: {}").format(
                self.full_name,
                self.sexe,
                self.birth_date,
                str(self.ranking),
                self.tournament_score)
        return resume_player

    @property
    def full_name(self):
        """Construit le nom complet du joueur au format: 'nom_de_famille prénom'
        """
        return (self.last_name + " " + self.first_name)

    def update_ranking(self, new_ranking):
        """Permet de mettre à jour le classement ELO du joueur

        Arguments:
            new_ranking (int) -- nouvelle valeur du classement ELO
        """
        self.ranking = new_ranking

    def update_score(self, new_score):
        """Permet de mettre à jour le score du joueur an y rajoutant le score du dernier round terminé

        Arguments:
            new_ranking (int) -- nouvelle valeur du classement ELO
        """
        self.tournament_score += new_score

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
            serialized_player (dict) -- dictionnaire représentant un joueur

        Returns:
            instance de Player
        """
        first_name = serialized_player['first_name']
        last_name = serialized_player['last_name']
        birth_date = serialized_player['birth_date']
        sexe = serialized_player['sexe']
        ranking = serialized_player['ranking']
        return Player(first_name, last_name, birth_date, sexe, ranking)
