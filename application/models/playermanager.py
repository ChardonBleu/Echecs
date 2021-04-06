from .player import Player


class PlayerManager:
    """[summary]
    """
    
    def __init__(self):
        self.players = []
    
    def load_players_from_bdd(self):
        """Create a list of 8 players
        
        A terme cette fonction doit aller chercher ces instances de joueurs dans la bdd

        Returns:
            liste of Player instances -- return to controller a list of 8 players
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
        return self.players
    
    def liste_index_players(self):
        pass