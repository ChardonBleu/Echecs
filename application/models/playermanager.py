from tinydb import TinyDB

from ..models.player import Player


class PlayerManager:
    """
    Permet de :
        Sauvegarder ces joueurs dans la BDD.
        Charger des joueurs à partir de la BDD.
        Mettre à jour les classements ELO dans le BDD.
    """

    def save_players_bdd(self, players_controller):
        """Sauvegarde le dictionnaire des joueurs dans la table 'players' de la base de données.

        Arguments:
            players_controller (objet PlayerController)  -- contient la liste des instances des joueurs du tournoi
        """
        serialized_players = []
        for player in players_controller.players:
            serialized_players.append(player.serialize_player())
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_controller.bdd_id = players_table.insert_multiple(serialized_players)

    def update_ranking_players_bdd(self, index, new_ranking, player_controller):
        """Sauvegarde dans la bdd la mise à jour du classement Elo des joueurs,
        ces nouvelles valeurs du classement pouvant être saisies par l'utilisateur à tout moment.

        Arguments:
            index (int) -- id du joueur dans la BDD
            new_ranking  (int)  --  nouvelle valeur du classement
            players_controller (objet PlayerController)  -- contient la liste des instances des joueurs du tournoi
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.update({'ranking': new_ranking}, doc_ids=[player_controller.bdd_id[index]])

    def load_all_players_from_bdd(self, other_player_controller):
        """Charge des joueurs depuis la base de données puis transforme la liste
        de dictionnaires de joueurs en liste d'instances de joueurs.
        Peut servir pour affichage de tous les joueurs.

        Attributs:
            other_player_controller  (objet Player_controller)  -- instance différente de celle du tournoi courant

        Returns:
            list -- nouvelle instance de PlayerManager contenant TOUS les joueurs de la BDD
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        serialized_players = players_table.all()
        list_all_players = other_player_controller
        for player in serialized_players:
            first_name = player['first_name']
            last_name = player['last_name']
            birth_date = player['birth_date']
            sexe = player['sexe']
            ranking = player['ranking']
            list_all_players.players.append(Player(first_name, last_name, birth_date, sexe, ranking))
            list_all_players.bdd_id.append(player.doc_id)
        return list_all_players

    def evaluate_number_players_bdd(self):
        """
        Returns:
            number_players_bdd  (int) -- nombre de joueurs enregistrés dans la base de donnée
        """
        db = TinyDB('db.json')
        number_players_bdd = len(db.table('players'))
        return number_players_bdd

    def load_players_with_bdd_id_list(self, bdd_id_list, players_controller):
        """Charge dans le player manager les joueurs dont les id de la BDD sont dans la liste passée en arguments

        Arguments:
            bdd_id_list (list) -- liste de id des joueurs dans la bdd
            players_controller (objet PlayerController)  -- contient la liste des instances des joueurs du tournoi

        Returns:
            players_controller (objet PlayerController)  -- contient la liste des instances des joueurs du tournoi
        """
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_controller.players = []
        players_table.bdd_id = []
        for bdd_id in bdd_id_list:
            serialized_player = players_table.get(doc_id=bdd_id)
            first_name = serialized_player['first_name']
            last_name = serialized_player['last_name']
            birth_date = serialized_player['birth_date']
            sexe = serialized_player['sexe']
            ranking = serialized_player['ranking']
            players_controller.players.append(Player(first_name, last_name, birth_date, sexe, ranking))
            players_controller.bdd_id.append(bdd_id)
        return players_controller
