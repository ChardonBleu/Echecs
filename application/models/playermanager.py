from ..models.player import Player
from tinydb import TinyDB


class PlayerManager:
    """Sert à créer une liste d'instances de joueurs pour un tournoi.
    Charges les joueurs à partir de la BDD.
    Sauvegarde les joueurs dans la BDD.
    """

    def __init__(self):
        self.players = []
        self.indice = []

    def __str__(self):
        """[summary]
        """
        liste_joueur = ""
        for index in range(len(self.players)):
            liste_joueur += str(self.indice[index]) + ": " + self.players[index].full_name() + "\n"            
        return str(liste_joueur)


    def __getitem__(self, key):
        """Renvoie la valeur de self.players[index] correspondant à la valeur de
        self.indice[index] pour le même index
        
        Returns:
            instance de Players
        """
        index_a_afficher = self.indice.index(key)
        return self.players[index_a_afficher]


    def add_players(self):
        """Create a list of 8 players

        A terme cette fonction doit aller chercher ces instances de joueurs dans la bdd

        Returns:
            liste of Player instances -- return to controller a list of 8 players
        """
        self.players = [Player("Sebag", "Marie", "1986", "F", "2438"),
                        Player("Victor", "Stephan", "1991", "M", "2430"),
                        Player("Pauline", "Guichard", "1988", "F", "2415"),
                        Player("Nikolay", "Legky", "1955", "M", "2402"),
                        Player("Sophie", "Millet", "1983", "F", "2396"),
                        Player("Aldo", "Haik", "1952", "M", "2385"),
                        Player("Judit", "Polgar", "1976", "F", "2735"),
                        Player("Anatoli", "Karpov", "1951", "M", "2617")
                        ]
        self.indice = ['joueur1', 'joueur2', 'joueur3', 'joueur4', 'joueur5', 'joueur6', 'joueur7', 'joueur8']

    def liste_index_players(self):
        """construction of the list of index players for tournament attribute players

        Returns:
            list --
        """
        return self.indice

    def save_players_BDD(self, player_table):
        """Sauvegarde le dictionnaire des joueurs dans la table players de la base de données.
        """
        serialized_players = []
        for player in self.players:
            serialized_players.append(player.serialize_player())
        db = TinyDB('db.json')
        players_table = db.table(player_table)
        players_table.truncate()
        players_table.insert_multiple(serialized_players)
       
    def load_players_from_bdd(self, player_table):
        """Charge des joueurs depuis la base de données puis transforme la liste
        de dictionnaires de joueurs en liste d'instances de joueurs
        """
        db = TinyDB('db.json')
        players_table = db.table(player_table)
        serialized_players = players_table.all()
        self.players = []
        for player in serialized_players:
            first_name = player['first_name']
            last_name = player['last_name']
            birth_date = player['birth_date']
            sexe = player['sexe']
            ranking = player['ranking']
            self.players.append(Player(first_name, last_name, birth_date, sexe, ranking))
