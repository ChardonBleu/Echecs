from ..models.playermanager import PlayerManager
from ..views.tournamentview import TournamentView
from ..models.tournament import Tournament


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
        """Lance la création d'un nouveau tournoi:
                Instancier nouveau tournoi
                charger joueurs ou les ajouter à la main
                associer joueurs et tounoi
                afficher résumé tournoi
                sauvegarder joueurs
        Affiche le résumé des données du tournoi.
        

        """
        # Instancie un nouveau tournoi
        self.new_tournament()
        
        # Ajoute des joueurs
        #self.players.add_players()        
        # Charge les joueurs de la table de la BDD mise en paramètre  - self.tournament.name_tournament_players()
        self.players.load_players_from_bdd(self.tournament.name_date_tournament())
        
        # lie les joueurs ajoutés à ce tournois
        self.tournament.tournament_players(self.players.liste_index_players())        
        # instancie les rounds vides
        self.tournament.tournament_rounds()
        
        # Sauvegarde les joueurs dans la BDD dans la table mise en paramètre
        self.players.save_players_BDD(self.tournament.name_date_tournament())
        
        # Affiche le résumé des données du tournois
        self.views.show_tournament(self.tournament, self.players)
        
        
