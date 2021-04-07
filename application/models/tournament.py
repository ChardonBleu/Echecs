from .round import Round
from utils.constants import TIME_CONTROL


class Tournament:
    """[summary]
    """

    def __init__(self, name, site, date_begin, date_end, description, index_time_control, number_rounds=4):
        """[summary]
        """

        self.name = name  # string
        self.site = site  # string
        self.date_begin = date_begin  # date
        self.date_end = date_end  # date
        self.description = description  # string
        self.time_control = TIME_CONTROL[index_time_control]  # string
        self.number_rounds = number_rounds  # int

        self.rounds = []
        for index_round in range(number_rounds):
            self.rounds[index_round] = Round()  # list of instances of Round()

        self.players = []  # list of index of instances of players

    def tournament_players(self, liste_index_players):
        self.players = liste_index_players
