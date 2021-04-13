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
        """Permet la saisie de huits nouveaux joueurs pour un nouveau tournoi.
        """
        for index in range(8):
            self.players_manager.add_one_player(index + 1, self.new_player())

    def show_players(self):
        """Appelle l'affichage des joueurs du tournoi courant.
        
        """
        self.view.show_player(self.players_manager)
        
    def show_all_players(self):
        """Appelle l'affichage de tous les joueur de la BDD
        show_player() reçoiten argument un objet PlayerManager()
        """
        self.view.show_player(self.players_manager.load_all_players_from_bdd())

    def sort_players_by_ranking(self):
        """Permet le tri des joueurs du tournoi courant selon leur classement ELO.
        Ne modifie pas la liste créée au lancement du tournoi        
        
        Returns:
            list -- liste triée
        """
        return sorted(self.players_manager.players, key=lambda players : players.ranking)



    def show_player_in_list(self, player_list): # Fonction a essayer d'éliminer. Esssayer de n'avoir que les objets player manager avec liste instance joueur et liste id de la bdd !!!
        """Affiche les joueurs d'une liste de joueurs passée en argumentet seulement les joueurs
        sans les indice. L'argument N'est PAS un objet PlayerManager

        Arguments:
            player_list {list} -- liste d'objets Players() 
        """
        for player in player_list:
            self.view.show_player(player)

            
