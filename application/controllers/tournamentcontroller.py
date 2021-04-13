from ..views.tournamentview import TournamentView
from ..models.tournament import Tournament


class TournamentController:
    """
    Instancie un tournois avec 8 joueurs
    """

    def __init__(self):
        """[summary]
        """
        # self.players = PlayerManager()
        self.view = TournamentView()
        self.tournament = None

    def new_tournament(self):
        """Crée instance de Tournament avec saisie utilisateur des caractéristique du tournois,
        sauf attribut players
        L'attribut round se renseigne à l'instanciation à partir du nombre de rounds donné par l'utilisateur
        On instancie les rounds vides.
        """
        self.tournament = Tournament(self.view.prompt_name_tournament(),
                                     self.view.prompt_site_tournament(),
                                     self.view.prompt_date_begin_tournament(),
                                     self.view.prompt_date_end_tournament(),
                                     self.view.prompt_description_tournament(),
                                     self.view.prompt_time_control(),
                                     self.view.prompt_number_rounds())
        
    def next_round(self):
        """[summary]
        """
        