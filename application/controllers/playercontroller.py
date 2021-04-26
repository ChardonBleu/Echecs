from ..models.player import Player
from ..models.playermanager import PlayerManager
from ..views.playerview import PlayerView


class PlayerController:
    """
    Modélise le controller des joueurs.
    Sert à créer une liste d'instances de joueurs pour un tournoi, avec sa liste d'id de la bdd associée.

    Attributs:
        self.players  (list) -- liste de 8 instances de Player. Ce sont les joueurs du tournoi.
        self.bdd_id (list)  -- liste de 8 nombres correspondant aux id des joueurs dans le bdd

    Si on trie les joueur dans la liste self.players, la liste associée self.bdd_id se trie également.

    Permet  de :
        Importer des joueurs en les saisissant à la console.
        Trier les joueurs.
    Assure le lien entre utilisateur et modèles en appelant la vue des joueurs
        pour la saisie de nouveaux joueurs
        pour l'affichage des joueurs du tournoi courant

    Attributs:
        self.view  (objet PlayerView)  -- instance de PlayerView destinée à la saisie
                                          et l'affichage des données propres aux joueurs.
        self.players_manager (objet PlayerManager)  -- instance de PlayerManager contenant
                                                       les joueurs du tournoi courant
    """

    def __init__(self):
        self.view = PlayerView()
        self.players = []
        self.bdd_id = []
        self.players_manager = PlayerManager()

    def new_player(self):
        """Crée instance de Player avec saisie utilisateur des caractéristique du joueur,

        Returns:
            object Player
        """
        new_player = Player(self.view.prompt_first_name_player(),
                            self.view.prompt_last_name_player(),
                            self.view.prompt_birth_date_player(),
                            self.view.prompt_sexe_player(),
                            self.view.prompt_ranking_player())
        return new_player
    
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

    def add_8_players(self):
        """Permet la saisie de huits nouveaux joueurs pour un nouveau tournoi.
        """
        for index in range(8):
            self.add_one_player(index + 1, self.new_player())

    def show_players(self, player_controller):
        """Appelle l'affichage des joueurs du tournoi courant.

        Args:
            player_manager (instance de PlayerManager) -- Contient la liste des 8 joueurs du tournoi courant
        """
        self.view.show_player(player_controller)

    def update_ranking_players(self):
        """Récupère le dico des {id_player: score} pour mettre à jour les scores
        des joueurs dans Player

        Args:
            results_round (dict) -- dico des {id_player: score}
        """
        for player in self.players:
            new_ranking = self.view.prompt_new_ranking_player(player)
            player.update_ranking(new_ranking)
            index = self.players.index(player)
            self.players_manager.update_ranking_players_bdd(index, new_ranking)

    def sort_players_by_name(self, player_controller):
        """Permet le tri des joueurs du tournoi courant selon leur nom complet : 'nom_de_famille prénom'
        (ordre alphabétique croissant - insensibilité à la casse).

        Args:
            player_manager (instance de PlayerManager) -- Contient la liste des 8 joueurs du tournoi courant
        """
        sorted_player_list = sorted(player_controller.couple_items(), key=lambda couple: couple[1].full_name.lower())
        player_controller.decouple_items(sorted_player_list)

    def sort_players_by_ranking(self, player_controller):
        """Permet le tri des joueurs du tournoi courant selon leur classement ELO (ordre décroissant des rangs)
        et selon leur score au tournoi (ordre décroissant des rangs).

        Args:
            player_manager (instance de PlayerManager) -- Contient la liste des 8 joueurs du tournoi courant
        """
        sorted_player_list = sorted(player_controller.couple_items(), key=lambda couple: couple[1].ranking,  reverse=True)
        player_controller.decouple_items(sorted_player_list)
    
    def sort_players_by_score_and_ranking(self, player_controller):
        """Permet le tri des joueurs du tournoi courant selon leur classement ELO (ordre décroissant des rangs)
        et selon leur score au tournoi (ordre décroissant des rangs).

        Args:
            player_manager (instance de PlayerManager) -- Contient la liste des 8 joueurs du tournoi courant
        """
        sorted_player_list = sorted(player_controller.couple_items(), key=lambda couple: couple[1].ranking,  reverse=True)
        sorted_player_list = sorted(sorted_player_list, key=lambda couple: couple[1].tournament_score, reverse=True)
        player_controller.decouple_items(sorted_player_list)
