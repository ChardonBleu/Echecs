from models.player import Player


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
                        Player("Nikolay", "Lgky", "1955", "M", "2402"),
                        Player("Sophie", "Millet", "1983", "F", "2396"),
                        Player("Aldo", "Haik", "1952", "M", "2385"),
                        Player("Judit", "Polgar", "1976", "F", "2735"),
                        Player("Anatoli", "Karpov", "1951", "M", "2617")
                        ]
        
        self.views = None
        
        self.tournament = None
