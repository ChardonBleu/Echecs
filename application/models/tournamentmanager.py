from tinydb import TinyDB

from ..models.tournament import Tournament


class TournamentManager:
    """
    Permet de :
        Sauvegarder un tournoi dans la BDD.
        Charger le dernier tournoi sauvegardé à partir de la BDD.
        Charger un tournoi, connaissant son id dans la bdd.
        Charger tous les tournois pour pouvoir les afficher.
    """

    def save_tournaments_bdd(self, tournament_controller):
        """Sauvegarde le dictionnaire des tournois dans la table tournament de la base de données.

        Arguments:
            (objet TournamentController) -- instance du tournament controller pour le tournoi courant
        """
        if len(tournament_controller.bdd_id) == 0:
            serialized_tournaments = []
            serialized_tournaments.append(tournament_controller.tournaments[0].serialize_tournament())
            db = TinyDB('db.json')
            tournament_table = db.table('tournaments')
            tournament_controller.bdd_id.append(tournament_table.insert_multiple(serialized_tournaments))
        else:
            self.update_tournaments_bdd(tournament_controller)

    def update_tournaments_bdd(self, tournament_controller):
        """
        Met à jour le dictionnaire des tournois dans la table tournament de la base de données
        pour le tournoi courant.

        Arguments:
            (objet TournamentController) -- instance du tournament controller pour le tournoi courant
        """
        serialized_tournaments = []
        serialized_tournaments.append(tournament_controller.tournaments[0].serialize_tournament())
        db = TinyDB('db.json')
        for key, value in serialized_tournaments[0].items():
            db.table('tournaments').update({key: value}, doc_ids=tournament_controller.bdd_id)

    def load_last_saved_tournament(self, tournament_controller):
        """charge dans le programme le dernier tournoi sauvegardé dans la bdd.
        Les rounds et les match déjà renseignés sont également chargés.

        Arguments:
            (objet TournamentController) -- instance du tournament controller pour le tournoi courant

        Returns:
            tournament_controller (objet TournamentController) -- instance de TournamentController
                                                                  pour le tournoi courant
        """
        tournament_controller.tournaments = []
        tournament_controller.bdd_id = []
        db = TinyDB('db.json')
        tournament_table = db.table('tournaments')
        id_last_tournament = len(tournament_table)
        serialized_last_tournament = tournament_table.get(doc_id=id_last_tournament)
        tournament_controller.bdd_id.append(id_last_tournament)
        tournament_controller.tournaments = [Tournament("", "", "", "", "", 1)]
        tournament_controller.tournaments[0] = tournament_controller.tournaments[0].deserialize_tournament(
            serialized_last_tournament)
        return tournament_controller

    def load_tournament_by_id(self, id, tournament_controller):
        """charge dans le programme le dernier tournoi sauvegardé dans la BDD.
        Les rounds et les match déjà renseignés sont également chargés.

        Arguments:
            id  (int) -- id du tournoi dans la BDD
            (objet TournamentController) -- instance du tournament controller pour le tournoi courant

        Returns:
            tournament_controller (objet TournamentController) -- instance de TournamentController
                                                                  pour le tournoi courant
        """
        tournament_controller.tournaments = []
        tournament_controller.bdd_id = []
        db = TinyDB('db.json')
        tournament_table = db.table('tournaments')
        serialized_tournament = tournament_table.get(doc_id=id)
        tournament_controller.bdd_id.append(id)
        tournament_controller.tournaments = [Tournament("", "", "", "", "", 1)]
        tournament_controller.tournaments[0] = tournament_controller.tournaments[0].deserialize_tournament(
            serialized_tournament)
        return tournament_controller

    def load_all_tournaments(self, other_tournament_controller):
        """charge  tous les tournois sauvegardé dans la bdd.
        Les rounds et les match déjà renseignés sont également chargés.

        Arguments:
            (objet TournamentController)  -- instance de TournamentController différente de celle du tournoi courant

        Returns:
            other_tournament_controller (objet TournamentController) --  contient tous les tournois de la BDD
        """
        db = TinyDB('db.json')
        tournament_table = db.table('tournaments')
        serialized_tournaments = tournament_table.all()
        for index in range(len(serialized_tournaments)):
            other_tournament_controller.bdd_id = serialized_tournaments[index].doc_id
            other_tournament_controller.tournaments.append(Tournament("", "", "", "", "", 1))
            other_tournament_controller.tournaments[index] = other_tournament_controller.tournaments[index] \
                .deserialize_tournament(serialized_tournaments[index])
        return other_tournament_controller
