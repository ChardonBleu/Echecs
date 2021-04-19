from tinydb import TinyDB, Query

from ..models.tournament import Tournament


class TournamentManager:
    """Sert à créer une liste d'instances de tournois, afin de sauvegarder les tournois passés.

    Attributs:
        self.tournaments  (list) -- liste d'instances de Tournament
        self.bdd_id  (list)  --  liste de id des tournois dans la BDD

    Permet de :
        Sauvegarder un tournoi dans la BDD.
        Charger le dernier tournoi sauvegardé à partir de la BDD.
        Charger un tournoi, connaissant son id dans la bdd.
        Charger tous les tournois pour pouvoir les afficher
    """

    def __init__(self):
        """
        """
        self.tournaments = []
        self.bdd_id = []

    def __str__(self):
        """Permet d'afficher la liste des tournois:

        Returns:
            string --
        """
        liste_tournaments = ""
        for index in range(len(self.tournaments)):
            liste_tournaments += str(self.tournaments[index]) + "\n"
        return liste_tournaments

    def save_tournaments_bdd(self):
        """Sauvegarde le dictionnaire des tournois dans la table tournament de la base de données.

        Returns:
            list -- liste des id des joueurs sauvegardés dans la base de données
        """
        serialized_tournaments = []
        for tournament in self.tournaments:
            serialized_tournaments.append(tournament.serialize_tournament())
        db = TinyDB('db.json')
        tournament_table = db.table('tournaments')
        self.bdd_id = tournament_table.insert_multiple(serialized_tournaments)
