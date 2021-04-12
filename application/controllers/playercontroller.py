from ..models.player import Player
from ..models.playermanager import PlayerManager
from ..views.playerview import PlayerView


class PlayerController:
    """
    Instancie un tournois avec 8 joueurs
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
        """[summary]
        """
        for index in range(8):
            self.players_manager.add_one_player(index + 1, self.new_player())
            
    def show_players(self):
        """[summary]
        """
        self.view.show_player(self.players_manager)
    
    def show_all_players(self):
        """[summary]
        """
        all_players = self.players_manager.load_all_players_from_bdd()
        for player in all_players:
            self.view.show_player(player)