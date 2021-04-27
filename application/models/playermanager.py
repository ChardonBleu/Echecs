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

        Returns:
            list -- liste des id des joueurs sauvegardés dans la base de données
        """
        serialized_players = []
        for player in players_controller.players:
            serialized_players.append(player.serialize_player())
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_controller.bdd_id = players_table.insert_multiple(serialized_players)
        return players_controller

    def update_ranking_players_bdd(self, index, new_ranking, player_controller):
        """Sauvegarde dans la bdd la mise à jour du classement Elo des joueurs,
        ces nouvelles valeurs du classement pouvant être saisies par l'utilisateur à tout moment.

        Arguments:
            last_name  (string)  -- nom de famille du joueur dont on met à jour le classement
            new_ranking  (int)  --  nouvelle valeur du classement
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
