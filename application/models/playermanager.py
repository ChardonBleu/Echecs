from ..models.player import Player
from tinydb import TinyDB


class PlayerManager:
    """Sert à créer une liste d'instances de joueurs pour un tournoi.
    Charges les joueurs à partir de la BDD.
    Sauvegarde les joueurs dans la BDD.
    """

    def __init__(self):
        self.players = []
        self.indice = ['joueur 1', 'joueur 2', 'joueur 3', 'joueur 4', 'joueur 5', 'joueur 6', 'joueur 7', 'joueur 8']

    def __str__(self):
        """Permet d'afficher la liste des joueurs sous la forme:
        joueur x : nom prénom

        Returns:
            string -- [description]
        """
        liste_joueur = ""
        for index in range(len(self.players)):
            liste_joueur += self.indice[index] + ": " + self.players[index].full_name() + "\n"            
        return liste_joueur

    def __getitem__(self, key):
        """Renvoie la valeur de self.players[index] correspondant à la valeur de
        self.indice[index] pour le même index
        
        Returns:
            instance de Players
        """
        index_a_afficher = self.indice.index(key)
        return self.players[index_a_afficher]

    def add_players(self, indice, player):
        """Ajout manuel de joueurs.
        
        Arguments;
            string -- indice correspond à la valeur de self.indice du joueur : joueur x
            objet Player  -- player correspond à une instance de Player avec ces attributs renseignés

        """
        self.players[indice] = player
        

    def liste_index_players(self):
        """Construction of the list of index players for tournament attribute players.

        Returns:
            list --
        """
        return self.indice

    def save_players_BDD(self, player_table):
        """Sauvegarde le dictionnaire des joueurs dans la table player_table de la base de données.
        
        Le nom de la table est construit par la méthode name_tournament_players() de la classe Tournament.
        """
        serialized_players = []
        for player in self.players:
            serialized_players.append(player.serialize_player())
        db = TinyDB('db_players.json')
        players_table = db.table(player_table)
        players_table.truncate()
        players_table.insert_multiple(serialized_players)
       
    def load_players_from_bdd(self, player_table):
        """Charge des joueurs depuis la base de données puis transforme la liste
        de dictionnaires de joueurs en liste d'instances de joueurs.
        
        Le nom de la table a été construit par la méthode name_tournament_players() de la classe Tournament et
        correspond à la liste des joueurs d'un tournoi déjà créé.
        """
        db = TinyDB('db_players.json')
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
        
