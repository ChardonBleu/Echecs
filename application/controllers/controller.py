from models.playermanager import PlayerManager
from views.tournamentview import TournamentView
from models.tournament import Tournament


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
        """Crée instance de Tournament avec saisie utilisateur des caractéristique du tournois,
        sauf attribut players
        L'attribut round se renseigne à l'instanciation à partir du nombre de rounds donné par l'utilisateur
        """
        self.tournament = Tournament(self.views.prompt_name_tournament(),
                                     self.views.prompt_site_tournament(),
                                     self.views.prompt_date_begin_tournament(),
                                     self.views.prompt_date_end_tournament(),
                                     self.views.prompt_description_tournament(),
                                     self.views.prompt_time_control(),
                                     self.views.prompt_number_rounds())

    def run(self):
        """Lance la création d'un nouveau tournoi.
        Affiche le résumé des données du tournoi.

        """
        # Ajoute des joueurs
        self.players.add_players()
        # Instancie un nouveau tournoi
        self.new_tournament()
        self.tournament.tournament_players(self.players.liste_index_players())
        # instancie les rounds vides
        self.tournament.tournament_rounds()
        # Affiche le résumé des données du tournois
        self.views.show_tournament(self.tournament, self.players)
        # Sauvegarde les joueurs dans la BDD dans la table mise en paramètre
        self.players.save_players_BDD('player_table1')
        # Charge les joueurs de la table de la BDD mise en paramètre
        self.players.load_players_from_bdd('player_table1')
        
        self.views.show_tournament(self.tournament, self.players)
