from tinydb import TinyDB

from ..models.player import Player


class PlayerManager:
    """Sert à créer une liste d'instances de joueurs pour un tournoi, avec sa liste d'id de la bdd associée.
    Une instance de PlayerManager simule un dictionaire ordonné: si on trie les joueur dans la liste self.players,
    la liste associée self.bdd_id se trie également.
    Permet également de :
        Importer des joueurs en les saisissant à la console
        Sauvegarder ces joueurs dans la BDD.
        Charger des joueurs à partir de la BDD.
    """

    def __init__(self):
        """
        """
        self.players = []
        self.bdd_id = []

    def __str__(self):
        """Permet d'afficher la liste des joueurs sous la forme:
        joueur x : nom prénom

        Returns:
            string -- [description]
        """
        liste_joueur = ""
        for index in range(len(self.players)):
            liste_joueur += "joueur " + "{:3}".format(self.bdd_id[index]) + ": " + str(self.players[index]) + "\n"
        return liste_joueur

    def __getitem__(self, key):
        """Renvoie la valeur de self.players[index] correspondant à la valeur de
        self.bdd_id[index] pour le même index

        Returns:
            instance de Players
        """
        index_a_afficher = self.bdd_id.index(key)
        return self.players[index_a_afficher]

    def __setitem__(self, key, value):
        """Permet d'ajouter ou de modifier la valeur d'un joueur

        Arguments:
            key {string} -- joueur x
            value {objet Player} -- instance de la classe Player
        """
        if key in self.bdd_id:
            indice_a_modifier = self.bdd_id.index(key)
            self.players[indice_a_modifier] = value
        else:
            self.bdd_id.append(key)
            self.players.append(value)

    def couple_items(self):
        """Crée une liste de tupples de couples (id de la bdd, joueur correspondant à cet id).
        Sert à pouvoir trier simultanémant self.players et self.bdd_id afin que l'id du joueur
        suive le joueur au cours du tri.

        Returns:
            list -- liste de tupples (id, player)
        """
        couples_id_player = []
        for index in range(len(self.players)):
            couples_id_player.append((self.bdd_id[index], self.players[index]))
        return couples_id_player

    def decouple_items(self, couples_id_player):
        """Utilisé aprés le tri des joueurs pour reconstruire les listes self.players et self.bdd_id triées

        Arguments:
            couples_id_player {list} -- liste de tupples (id, player)
        """
        for index in range(len(couples_id_player)):
            self.bdd_id[index] = couples_id_player[index][0]
            self.players[index] = couples_id_player[index][1]

    @property
    def liste_id_players(self):
        """Construction of the list of index players for tournament attribute players.

        Returns:
            list --
        """
        return self.bdd_id

    def add_one_player(self, bdd_id, player):
        """Ajout manuel de 8 joueurs.

        Arguments;
            string -- indice correspond à la valeur de self.bdd_id du joueur : joueur x
            objet Player  -- player correspond à une instance de Player avec ces attributs renseignés

        """
        self[bdd_id] = player

    def save_players_BDD(self):
        """Sauvegarde le dictionnaire des joueurs dans la table player_table de la base de données.

        Le nom de la table est construit par la méthode name_tournament_players() de la classe Tournament.

        Returns:
            list -- liste des id des joueurs sauvegardés dans la base de données
        """
        serialized_players = []
        for player in self.players:
            serialized_players.append(player.serialize_player())
        db = TinyDB('db.json')
        players_table = db.table('players')
        self.bdd_id = players_table.insert_multiple(serialized_players)

    def load_all_players_from_bdd(self):
        """Charge des joueurs depuis la base de données puis transforme la liste
        de dictionnaires de joueurs en liste d'instances de joueurs.
        Peut servir pour affichage de tous les joueurs.

        Returns:
            list -- liste des instances de classe Player de tous les joueurs de la BDD
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        serialized_players = players_table.all()
        liste_tous_joueurs = PlayerManager()
        for index in range(len(serialized_players)):
            first_name = serialized_players[index]['first_name']
            last_name = serialized_players[index]['last_name']
            birth_date = serialized_players[index]['birth_date']
            sexe = serialized_players[index]['sexe']
            ranking = serialized_players[index]['ranking']
            liste_tous_joueurs.players.append(Player(first_name, last_name, birth_date, sexe, ranking))
            liste_tous_joueurs.bdd_id.append(serialized_players[index].doc_id)
        return liste_tous_joueurs

    def load_8_players_from_bdd(self, id_first_player=9):
        """Chargement de 8 joueurs consécutifs de la bdd à partir du joueur dont l'id est passé en paramètre
        pour test déroulement application.

        Pour des joueurs non consécutifs passer en paramètre une liste d'id de joueurs
        puis itérer sur cette liste:
        for id in liste_id:
        et récupérer le bon joueur à l'aide de .doc_id ...
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        serialized_players = players_table.all()
        self.players = []
        self.bdd_id = []
        for index in range(id_first_player - 1, id_first_player + 7):
            first_name = serialized_players[index]['first_name']
            last_name = serialized_players[index]['last_name']
            birth_date = serialized_players[index]['birth_date']
            sexe = serialized_players[index]['sexe']
            ranking = serialized_players[index]['ranking']
            self.players.append(Player(first_name, last_name, birth_date, sexe, ranking))
            self.bdd_id.append(serialized_players[index].doc_id)
