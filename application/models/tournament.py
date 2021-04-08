from .round import Round
from ..utils.constants import TIME_CONTROL


class Tournament:
    """[summary]
    """

    def __init__(self, name, site, date_begin, date_end, description, index_time_control, number_rounds=4):
        """[summary]
        """

        self.name = name  # string
        self.site = site  # string
        self.date_begin = date_begin  # string
        self.date_end = date_end  # string
        self.description = description  # string
        self.time_control = TIME_CONTROL[index_time_control]  # string
        self.number_rounds = number_rounds  # int

        self.rounds = []  # list of instances of Round()

        self.players = []  # list of index of instances of players

    def __str__(self):
        """Permet d'afficher un résumé des caractéristique du tournois
        """
        resume_tournament = ("Tournois {} à {}\ndu {} au {}\nObservation: {}\n"
                             .format(self.name, self.site, self.date_begin,
                                     self.date_end, self.description, ) +
                             "Time control: {} - Nombre de rounds: {}\n"
                             .format(self.time_control, self.number_rounds)
                             )
        return resume_tournament

    def tournament_players(self, liste_index_players):
        """Met dans l'attribut self.players de Tournament la liste des indices des instances des joueurs de ce tournois

        Arguments:
            liste_index_players {list} --
        """
        self.players = liste_index_players

    def tournament_rounds(self):
        """Rempli l'attribut self.rounds de Tournament avec autant d'instances
        vides de Round() qu'il y a de rounds indiqués par l'utilisateur
        """
        i = 0
        while i < self.number_rounds:
            self.rounds.append(Round())
            i = i + 1

    def name_date_tournament(self):
        """Crée un nom unique pour identifier la liste des joueurs d'un tournois et la stocker dans la bdd

        Returns:
            string -- pour identifiant des joueurs d'un tournoi
        """
        name_tournament_players = self.name + "_" + self.date_begin
        return name_tournament_players
