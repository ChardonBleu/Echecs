from tinydb import TinyDB

from ..models.player import Player


class PlayerManager:
    """Sert à créer une liste d'instances de joueurs pour un tournoi, avec sa liste d'id de la bdd associée.

    Attributs:
        self.players  (list) -- liste de 8 instances de Player. Ce sont les joueurs du tournoi.
        self.bdd_id (list)  -- liste de 8 nombres correspondant aux id des joueurs dans le bdd

    Une instance de PlayerManager simule un dictionaire ordonné: si on trie les joueur dans la liste self.players,
    la liste associée self.bdd_id se trie également.

    Permet également de :
        Importer des joueurs en les saisissant à la console.
        Sauvegarder ces joueurs dans la BDD.
        Charger des joueurs à partir de la BDD.
        Mettre à jour les classements ELO dans le BDD.
        Trier les joueurs.
    """

    def __init__(self):
        self.players = []
        self.bdd_id = []

    def __str__(self):
        """Permet d'afficher la liste des joueurs sous la forme:
        joueur x : nom prénom

        Returns:
            string --
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
            key (string)         -- joueur x
            value (objet Player) -- instance de la classe Player
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
            couples_id_player (list) -- liste de tupples (id, player)
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
            bdd_id  (string)        -- indice correspond à la valeur de self.bdd_id du joueur : joueur x
            player  (objet Player)  -- player correspond à une instance de Player avec ces attributs renseignés

        """
        self[bdd_id] = player

    def update_scores_players(self, results_round):
        """Récupère le dico des {id_player: score} pour mettre à jour les scores
        des joueurs dans Player

        Args:
            results_round (dict) -- dico des {id_player: score}
        """
        for id_players, round_score in results_round.items():
            player = self[id_players]
            player.update_score(round_score)

    def save_players_bdd(self):
        """Sauvegarde le dictionnaire des joueurs dans la table 'players' de la base de données.

        Returns:
            list -- liste des id des joueurs sauvegardés dans la base de données
        """
        serialized_players = []
        for player in self.players:
            serialized_players.append(player.serialize_player())
        db = TinyDB('db.json')
        players_table = db.table('players')
        self.bdd_id = players_table.insert_multiple(serialized_players)

    def sort_players_by_name(self, player_manager):
        """Permet le tri des joueurs du tournoi courant selon leur nom complet : 'nom_de_famille prénom'
        (ordre alphabétique croissant - insensibilité à la casse).

        Args:
            player_manager (instance de PlayerManager) -- Contient la liste des 8 joueurs du tournoi courant
        """
        sorted_player_list = sorted(player_manager.couple_items(), key=lambda couple: couple[1].full_name.lower())
        player_manager.decouple_items(sorted_player_list)

    def sort_players_by_ranking(self, player_manager):
        """Permet le tri des joueurs du tournoi courant selon leur classement ELO (ordre décroissant des rangs)
        et selon leur score au tournoi (ordre décroissant des rangs).

        Args:
            player_manager (instance de PlayerManager) -- Contient la liste des 8 joueurs du tournoi courant
        """
        sorted_player_list = sorted(player_manager.couple_items(), key=lambda couple: couple[1].ranking,  reverse=True)
        player_manager.decouple_items(sorted_player_list)

    def sort_players_by_score_and_ranking(self, player_manager):
        """Permet le tri des joueurs du tournoi courant selon leur classement ELO (ordre décroissant des rangs)
        et selon leur score au tournoi (ordre décroissant des rangs).

        Args:
            player_manager (instance de PlayerManager) -- Contient la liste des 8 joueurs du tournoi courant
        """
        sorted_player_list = sorted(player_manager.couple_items(), key=lambda couple: couple[1].ranking,  reverse=True)
        sorted_player_list = sorted(sorted_player_list, key=lambda couple: couple[1].tournament_score, reverse=True)
        player_manager.decouple_items(sorted_player_list)

    def update_ranking_players_bdd(self, index, new_ranking):
        """Sauvegarde dans le bdd la mise à jour de classement Elo des joueurs,
        ces nouvelles valeurs du classement étant saisies par l'utilisateur en
        fin de tournoi.

        Arguments:
            last_name  (string)  -- nom de famille du joueur dont on met à jour le classement
            new_ranking  (int)  --  nouvelle valeur du classement
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.update({'ranking': new_ranking}, doc_ids=[self.bdd_id[index]])

    def load_all_players_from_bdd(self):
        """Charge des joueurs depuis la base de données puis transforme la liste
        de dictionnaires de joueurs en liste d'instances de joueurs.
        Peut servir pour affichage de tous les joueurs.

        Returns:
            list -- nouvelle instance de PlayerManager contenant TOUS les joueurs de la BDD
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        serialized_players = players_table.all()
        list_all_players = PlayerManager()
        for index in range(len(serialized_players)):
            first_name = serialized_players[index]['first_name']
            last_name = serialized_players[index]['last_name']
            birth_date = serialized_players[index]['birth_date']
            sexe = serialized_players[index]['sexe']
            ranking = serialized_players[index]['ranking']
            list_all_players.players.append(Player(first_name, last_name, birth_date, sexe, ranking))
            list_all_players.bdd_id.append(serialized_players[index].doc_id)
        return list_all_players

    def evaluate_number_players_bdd(self):
        """Chargement de 8 joueurs consécutifs de la bdd à partir du joueur dont l'id est passé en paramètre
        pour test déroulement application.

        Pour des joueurs non consécutifs passer en paramètre une liste d'id de joueurs
        puis itérer sur cette liste:
        for id in liste_id:
        et récupérer le bon joueur à l'aide de .doc_id ...
        """
        db = TinyDB('db.json')
        number_players_bdd = len(db.table('players'))
        return number_players_bdd

    def load_players_with_bdd_id_list(self, bdd_id_list):
        """Charge dans le player manager les 8 joueurs dont les id de la BDD sont dans la liste passée en arguments

        Arguments:
            bdd_id_list (list) -- liste de id des joueurs dans la bdd
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        self.players = []
        self.bdd_id = []
        for bdd_id in bdd_id_list:
            serialized_player = players_table.get(doc_id=bdd_id)
            first_name = serialized_player['first_name']
            last_name = serialized_player['last_name']
            birth_date = serialized_player['birth_date']
            sexe = serialized_player['sexe']
            ranking = serialized_player['ranking']
            self.players.append(Player(first_name, last_name, birth_date, sexe, ranking))
            self.bdd_id.append(bdd_id)
