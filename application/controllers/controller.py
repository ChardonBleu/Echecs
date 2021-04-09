from .playercontroller import PlayerController
from .tournamentcontroller import TournamentController

from ..models.playermanager import PlayerManager
from ..utils.constants import PLAYERS_LISTE_INDICES


class Controller:
    """
    Instancie un tournois avec 8 joueurs
    """

    def __init__(self):
        """[summary]
        """
        self.players = PlayerManager()
        self.tournament = TournamentController()
        self.player_controller = PlayerController()

    def load_players(self):
        """Charge depuis la BDD les joueurs ayant le nom du tournoi courant.
        Le tournoi courant est identifié par son nom et sa date de début.
        """
        self.players.load_players_from_bdd(self.tournament.current_tournament.name_date_tournament())

    def save_players(self):
        """Charge depuis le BDD les joueurs ayant le nom du tournoi courant.
        Le tournoi courant est identifié par son nom et sa date de début.
        """
        self.players.save_players_BDD(self.tournament.current_tournament.name_date_tournament())

    def show_tournament_summary(self):
        """[summary]
        """
        self.tournament.view.show_tournament(self.tournament.current_tournament)

    def run(self):
        """Lance la création d'un nouveau tournoi:
                Instancier nouveau tournoi
                charger joueurs ou les ajouter à la main
                associer joueurs et tounoi
                afficher résumé tournoi
                sauvegarder joueurs
        Affiche le résumé des données du tournoi.
        """
        # Instancie un nouveau tournoi
        self.tournament.new_tournament()

        # Charge les joueurs du tournoi courant dans la BDD
        # self.load_players()

        # Ajoute 8 joueurs au tournoi courant
        for indice in PLAYERS_LISTE_INDICES:
            self.players.add_one_player(indice, self.player_controller.new_player())

        # Affiche le résumé des données du tournois
        self.show_tournament_summary()
        # Affiche la liste des joueurs avec leur classement
        self.player_controller.view.show_player(self.players)

        # Sauvegarde les joueurs du tournoi courant dans la BDD
        self.save_players()
