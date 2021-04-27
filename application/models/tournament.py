from .round import Round

from ..utils.constants import TIME_CONTROL


class Tournament:
    """Modélise un tournoi d'échecs.

    Gère l'ajout de rounds au tournoi:
        self.rounds (list) -- liste d'instances de Round

    Gère l'ajout de match dans le dernier round:
        chaque instance de Round créée contient une liste de 4 instances de Match

    Gère l'ajout de joueurs au tournoi:
        self.players (list)  -- liste de id des joueurs (id de la BDD)
    """

    def __init__(self, name, site, date_begin, date_end, description, index_time_control, number_rounds=4):
        """
        Arguments:
            name (string) -- nom du tournoi
            site (string) -- lieu du tournoi
            date_begin (string) -- date de début du tournoi
            date_end (string) -- date de fin du tournoi
            description (string) --  description du tournoi
            index_time_control (int) -- permet le choix du contrôleur de temps dans une liste de constantes

        Keyword Arguments:
            number_rounds (int) --  nombre de rounds du tournoi (default: {4})
        """

        self.name = name
        self.site = site
        self.date_begin = date_begin
        self.date_end = date_end
        self.description = description
        self.time_control = TIME_CONTROL[index_time_control]
        self.number_rounds = number_rounds

        self.rounds = []

        self.players = []

    def __str__(self):
        """Permet d'afficher un résumé des caractéristique du tournois.
        """
        resume_tournament = ("Tournois: {} - à: {}\ndu {} au {}\nObservation: {}\n"
                             .format(self.name, self.site, self.date_begin,
                                     self.date_end, self.description, ) +
                             "Time control: {} - Nombre de rounds: {}\n"
                             .format(self.time_control, self.number_rounds) +
                             "Id joueurs: {}\n".format(self.players)
                             )
        return resume_tournament

    def tournament_players(self, liste_id_players):
        """Met dans l'attribut self.players de Tournament la liste des id de la bdd des joueurs de ce tournois.

        Arguments:
            liste_index_players (list) --
        """
        self.players = liste_id_players

    @property
    def liste_id_players(self):
        """Permet d"accéder à la liste de idd de la bdd des joueurs du tournoi courant.

        Returns:
            self.players (list)  --
        """
        return self.players

    def add_round(self):
        """Rempli l'attribut self.rounds de Tournament avec autant d'instances
        vides de Round() qu'il y a de rounds indiqués par l'utilisateur.
        Puis renpli chaque round avec un match.
        """
        if len(self.rounds) < self.number_rounds:
            self.rounds.append(Round(len(self.rounds) + 1))

    def add_match_to_last_round(self, player1, player2, score1, score2):
        """Sélectionne le dernier round créé puis y ajoute un match avec les joueurs donnés en argument.

        Arguments:
            player1 (instance de Player) --
            player2 (instance de Player) --

            score1 (int) -- score en début de round
            score2 (int) -- score ne début de round
        """
        index = len(self.rounds) - 1
        self.rounds[index].add_match(player1, player2, score1, score2)

    def serialize_tournament(self):
        """Transforme une instance de tournois en dictionnaire avant sauvegarde dans la BDD.

        Returns:
            dict -- Dictionnaire représentant un tournois.
        """
        serialized_round = []
        for tour in self.rounds:
            serialized_round.append(tour.serialize_round())
        serialized_tournament = {
            'name': self.name,
            'site': self.site,
            'date_begin': self.date_begin,
            'date_end': self.date_end,
            'description': self.description,
            'time_control': self.time_control,
            'number_rounds': self.number_rounds,
            'rounds': serialized_round,
            'players': self.players}
        return serialized_tournament

    def deserialize_tournament(self, serialized_tournament):
        """Transforme un dico obtenu à partir de la BDD en instance de Tournament.

        Returns:
            objet Tournament -- instance de Tournament.
        """
        self.name = serialized_tournament['name']
        self.site = serialized_tournament['site']
        self.date_begin = serialized_tournament['date_begin']
        self.date_end = serialized_tournament['date_end']
        self.description = serialized_tournament['description']
        self.time_control = serialized_tournament['time_control']
        self.number_rounds = serialized_tournament['number_rounds']
        self.players = serialized_tournament['players']
        self.rounds = []
        non_empty_rounds = len(serialized_tournament['rounds'])
        for index in range(non_empty_rounds):
            self.rounds.append(Round(""))
            self.rounds[index] = self.rounds[index].deserialize_round(serialized_tournament['rounds'][index])
        return self

    def recover_scores_for_loaded_tournament(self):
        """Récupération des scores des rounds d'un tournois chargé depuis la BDD

        Returns:
            dict -- dictionnaire des scores de chaque joueur sous la forme {id_bdd: score}
        """
        score_round = {}
        for index in range(len(self.rounds)):
            for match in self.rounds[index].matches:
                score_round[match.pairs[0][0]] = 0
                score_round[match.pairs[1][0]] = 0
        for index in range(len(self.rounds)):
            for match in self.rounds[index].matches:
                score_round[match.pairs[0][0]] += match.pairs[0][1]
                score_round[match.pairs[1][0]] += match.pairs[1][1]
        return score_round
