from ..models.player import Player
from ..models.playermanager import PlayerManager
from ..views.playerview import PlayerView


class PlayerController:
    """
    Modélise le controller des joueurs.
    Assure le lien entre utilisateur et modèles en appelant la vue des joueurs
        pour la saisie de nouveaux joueurs
        pour l'affichage des joueurs du tournoi courant
    Se charge du tri des joueurs.
    """

    def __init__(self):
        """[summary]
        """
        self.view = PlayerView()
        self.players_manager = PlayerManager()

    def new_player(self):
        """Crée instance de Player avec saisie utilisateur des caractéristique du joueur,

        Returns:
            object Player
        """
        new_player = Player(self.view.prompt_first_name_player(),
                            self.view.prompt_last_name_player(),
                            self.view.prompt_birth_date_player(),
                            self.view.prompt_sexe_player(),
                            self.view.prompt_ranking_player())
        return new_player

    def add_8_players(self):
        """Permet la saisie de huits nouveaux joueurs pour un nouveau tournoi.
        """
        for index in range(8):
            self.players_manager.add_one_player(index + 1, self.new_player())

    def show_players(self, player_manager):
        """Appelle l'affichage des joueurs du tournoi courant.
        
        Args: 
            player_manager {instance de PlayerManager} -- Contient la liste des 8 joueurs du tournoi courant
        """
        self.view.show_player(player_manager)

    def sort_players_by_ranking(self, player_manager):
        """Permet le tri des joueurs du tournoi courant selon leur classement ELO (ordre décroissant des rangs).
                
        Args: 
            player_manager {instance de PlayerManager} -- Contient la liste des 8 joueurs du tournoi courant
        """
        sorted_player_list = sorted(player_manager.couple_items(),
                                    key=lambda couple : couple[1].ranking,  reverse=True)
        player_manager.decouple_items(sorted_player_list)

    def sort_players_by_name(self, player_manager):
        """Permet le tri des joueurs du tournoi courant selon leur nom complet : 'nom_de_famille prénom'
        (ordre alphabétique croissant - insensibilité à la casse).
                
        Args: 
            player_manager {instance de PlayerManager} -- Contient la liste des 8 joueurs du tournoi courant
        """
        sorted_player_list = sorted(player_manager.couple_items(), key=lambda couple : couple[1].full_name.lower())
        player_manager.decouple_items(sorted_player_list)
