from .playercontroller import PlayerController
from .tournamentcontroller import TournamentController


class Controller:
    """
    Instancie un tournois avec 8 joueurs
    """

    def __init__(self):
        """[summary]
        """

        self.tournament_controller = TournamentController()
        self.players_controller = PlayerController()

    def link_players_with_tournament(self):
        """Associe la liste des joueurs chargés au tournoi courant
        en renseignant l'attribut self.players de la classe Tournament
        avec la liste des id des joueurs.
        Cet id est celui du joueur dans la BDD
        """
        id_list = self.players_controller.players_manager.liste_id_players
        self.tournament_controller.tournament.tournament_players(id_list)

    def run(self):
        """Lance la création d'un nouveau tournoi:
                Instancier nouveau tournoi
                Ajouter 8 joueurs à la main
                Sauvegarder ces 8 joueurs dans la bdd
                Associer joueurs et tournoi
                Afficher résumé tournoi
                Afficher tous les joueurs de la bdd
        """
        # Instancie un nouveau tournoi
        self.tournament_controller.new_tournament()

        # Ajoute manuellement 8 joueurs au tournoi courant
        # self.players_controller.add_8_players()
        # Sauvegarde les joueurs entrés manuellement dans la BDD
        #self.players_controller.players_manager.save_players_BDD()
        
        # Charge les 8 premiers joueurs de la bdd pour test rapide appli
        self.players_controller.players_manager.load_8_players_from_bdd()
        
        # Lie les joueurs entrés manuellemetn et ajoutées à la BDD au tournoi courant
        self.link_players_with_tournament()

        # Affiche le résumé des données du tournois
        self.tournament_controller.show_tournament_summary()
        
        # Affiche la liste des joueurs avec leur classement
        self.players_controller.show_players()

        # Affiche la liste de tous les joueurs de la bdd
        # self.players_controller.show_all_players()
        
        # Tri des joueurs courants et les mets dans une liste. Ne contient pas l'id de la bdd
        sorted_players = self.players_controller.sort_players_by_ranking()
        
        # Affiche la liste des joueurs avec leur classement, mais sans l'id de la bdd
        self.players_controller.show_player_in_list(sorted_players)
