class RoundView:
    """
        Interface destinée à la gestion des rounds

    """

    def prompt_score_match(self):
        """blabla

        Returns:
            int -- 
        """
        pass
        
    def show_rounds_with_match(self, tournament):
        """Affiche les caractéristiques des rounds du tournoi courant passé en paramètre.
        
        Args:
            tournament {instance de Tournament}
        """
        for tour in tournament.rounds:
            print(tour)
            for match in tour.match:
                print(match)
        print()