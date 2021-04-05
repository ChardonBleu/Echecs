from models.round import Round


TIME_CONTROL = ["bullet", "blitz", "coup-rapide"]


class Tournament:
    """[summary]
    """

    def __init__(self, name, site, date_begin, date_end, description, index_time_control, number_rounds=4):
        """[summary]
        """

        self.name = None  # string
        self.site = None  # string
        self.date_begin = None  # date
        self.date_end = None  # date
        self.description = None  # string
        self.time_control = TIME_CONTROL[index_time_control]  # string
        self.number_rounds = number_rounds  # int

        self.rounds = []  # list of instances of Round()

        self.players = []  # list of index of instances of players
