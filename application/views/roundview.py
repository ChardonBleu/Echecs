class RoundView:
    """
        Interface destinée à la gestion des rounds
    """

    def prompt_score_match(self, match):
        """blabla

        Args:
            match {instance de Match}
        
        Returns:
            string -- Résultat du match
        """
        print(match.pair_of_players)
        loop = True
        while loop:            
            try:
                winner = input("Résultalt du match: j1/j2/= :  ")
                if winner == "j1" or winner == "j2" or winner == "=":
                    loop = False
                else:
                    raise ValueError
            except ValueError:
                print('Vous devez saisir j1 ou j2 ou =')
        print()
        return winner
        
    def show_rounds_with_matches(self, tournament):
        """Affiche les caractéristiques des rounds du tournoi courant passé en paramètre.
        
        Args:
            tournament {instance de Tournament}
        """
        for tour in tournament.rounds:
            print(tour)
            for match in tour.matches:
                print(match)
        print()