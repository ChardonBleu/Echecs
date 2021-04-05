TIME_CONTROL = ["bullet", "blitz", "coup-rapide"]
FICHIER_PLAYERS = [
    {
        "first_name" :"Sebag",
        "last_name" :"Marie",
        "birth_date" :"1986",
        "sexe" : "F",
        "ranking" :"2438"
    },        
    {
        "first_name" :"Victor",
        "last_name" :"Stephan",
        "birth_date" :"1991",
        "sexe" : "M",
        "ranking" :"2430"
    },
    {
        "first_name" :"Pauline",
        "last_name" :"Guichard",
        "birth_date" :"1988",
        "sexe" : "F",
        "ranking" :"2415"
    },
    {
        "first_name" :"Nikolay",
        "last_name" :"Lgky",
        "birth_date" :"1955",
        "sexe" : "M",
        "ranking" :"2402"
    },
    {
        "first_name" :"Sophie",
        "last_name" :"Millet",
        "birth_date" :"1983",
        "sexe" : "F",
        "ranking" :"2396"
    },
    {
        "first_name" :"Aldo",
        "last_name" :"Haik",
        "birth_date" :"1952",
        "sexe" : "M",
        "ranking" :"2385"
    },
    {
        "first_name" :"Judit",
        "last_name" :"Polgar",
        "birth_date" :"1976",
        "sexe" : "F",
        "ranking" :"2735"
    },
    {
        "first_name" :"Anatoli",
        "last_name" :"Karpov",
        "birth_date" :"1951",
        "sexe" : "M",
        "ranking" :"2617"
    },
]


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


class Tournament:
    """[summary]
    """

    def __init__(self, index_time_control, number_rounds=4):
        """[summary]
        """

        self.name = None  # string
        self.site = None  # string
        self.date_begin = None  # date
        self.date_begin = None  # date
        self.description = None  # string
        self.time_control = TIME_CONTROL[index_time_control]  # string
        self.number_rounds = number_rounds  # int
        
        self.rounds = []  # list of instances of Round()
        for index in range(number_rounds):
            self.rounds[index] = Round()
      
        self.players = []  # list of index of instances of players           



class Round:
    """[summary]
    """
    pass