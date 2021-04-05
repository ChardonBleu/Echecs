from models.player import Player
from views.view import ManagerTournamentView
from models.tournament import Tournament


class TournamentController:
    """
    Instancie un tournois avec 8 joueurs
    """
    
    def __init__(self):
        """[summary]
        """
        
        self.players = [Player("Sebag", "Marie", "1986", "F", "2438"),
                        Player("Victor", "Stephan", "1991", "M", "2430"),
                        Player("Pauline", "Guichard", "1988", "F", "2415"),
                        Player("Nikolay", "Legky", "1955", "M", "2402"),
                        Player("Sophie", "Millet", "1983", "F", "2396"),
                        Player("Aldo", "Haik", "1952", "M", "2385"),
                        Player("Judit", "Polgar", "1976", "F", "2735"),
                        Player("Anatoli", "Karpov", "1951", "M", "2617")
                        ]
        
        self.views = ManagerTournamentView()
        
        self.tournament = Tournament(self.views.prompt_name_tournament(),
                                     self.views.prompt_site_tournament(),
                                     self.views.prompt_date_debut_tournament(),
                                     self.views.prompt_date_fin_tournament(),
                                     self.views.prompt_description_tournament(),
                                     self.views.prompt_time_control(),
                                     self.views.prompt_number_rounds())

    def run(self):
        """[summary]
        """
        
        pass
