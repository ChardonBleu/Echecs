from .round import Round

from ..utils.constants import TIME_CONTROL


class Tournament:
    """Modélise un tournoi d'échecs.
    """

    def __init__(self, name, site, date_begin, date_end, description, index_time_control, number_rounds=4):
        """
        Arguments:
            name (string) --
            site (string) --
            date_begin (string) --
            date_end (string) --
            description (string) --
            index_time_control (int) --

        Keyword Arguments:
            number_rounds (int) -- (default: {4})
        """

        self.name = name  # string
        self.site = site  # string
        self.date_begin = date_begin  # string
        self.date_end = date_end  # string
        self.description = description  # string
        self.time_control = TIME_CONTROL[index_time_control]  # string
        self.number_rounds = number_rounds  # int

        self.rounds = []  # list of instances of Round()

        self.players = []  # list of players's bdd id

    def __str__(self):
        """Permet d'afficher un résumé des caractéristique du tournois
        """
        resume_tournament = ("Tournois {} à {}\ndu {} au {}\nObservation: {}\n"
                             .format(self.name, self.site, self.date_begin,
                                     self.date_end, self.description, ) +
                             "Time control: {} - Nombre de rounds: {}\n"
                             .format(self.time_control, self.number_rounds) +
                             "Id joueurs: {}\n".format(self.players)
                             )
        return resume_tournament

    def tournament_players(self, liste_id_players):
        """Met dans l'attribut self.players de Tournament la liste des id de la bdd des joueurs de ce tournois

        Arguments:
            liste_index_players (list) --
        """
        self.players = liste_id_players

    def add_round(self):
        """Rempli l'attribut self.rounds de Tournament avec autant d'instances
        vides de Round() qu'il y a de rounds indiqués par l'utilisateur.
        Puis renpli chaque round avec un match
        """
        if len(self.rounds) < self.number_rounds:
            self.rounds.append(Round(len(self.rounds) + 1))

    def add_match_to_last_round(self, player1, player2, score1, score2):
        """Sélectionne le dernier round créé puis y ajoute un match avec les joueurs donnés en argument

        Arguments:
            player1 (instance de Player) --
            player2 (instance de Player) --

            score1 (int) -- score en début de round
            score2 (int) -- score ne début de round
        """
        index = len(self.rounds) - 1
        self.rounds[index].add_match(player1, player2, score1, score2)
