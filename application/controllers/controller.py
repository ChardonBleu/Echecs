from models.player import Player
from views.tournamentview import TournamentView
from models.tournament import Tournament
from models.playermanager import PlayerManager


class TournamentController:
    """
    Instancie un tournois avec 8 joueurs
    """

    def __init__(self):
        """[summary]
        """
        self.players = PlayerManager()
        self.views = TournamentView()
        self.tournament = None


    def new_tournament(self):
        """Crée instance de Tournament avec saisie utilisateur des caractéristique du tournois
        sauf attribut players et attibut rounds
        """
        self.tournament = Tournament(self.views.prompt_name_tournament(),
                                     self.views.prompt_site_tournament(),
                                     self.views.prompt_date_debut_tournament(),
                                     self.views.prompt_date_fin_tournament(),
                                     self.views.prompt_description_tournament(),
                                     self.views.prompt_time_control(),
                                     self.views.prompt_number_rounds())

    def run(self):
        """Lance la création d'un nouveau tournoi
        """
        self.players.load_players_from_bdd()
        self.new_tournament()
        