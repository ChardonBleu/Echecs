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
                winner = input("Résultalt du match: j" +
                               str(match.pairs[0][0]) +
                               " ou j" +
                               str(match.pairs[1][0]) +
                               " ou = :  ")
                if winner == "j" + str(match.pairs[0][0]) or winner == "j" + str(match.pairs[1][0]) or winner == "=":
                    loop = False
                else:
                    raise ValueError
            except ValueError:
                print("Vous devez saisir j" + str(match.pairs[0][0]) + " ou j" + str(match.pairs[1][0]) + " ou =")
        return winner

    def show_rounds_with_matches(self, tournament, nb_round):
        """Affiche les caractéristiques des rounds du tournoi courant passé en paramètre.

        Args:
            tournament {instance de Tournament}
        """
        tour = tournament.rounds[nb_round - 1]
        print(tour)
        for match in tour.matches:
            print(match)

    def show_all_rounds(self, tournament):
        """Affiche les caractéristiques des rounds du tournoi courant passé en paramètre.

        Args:
            tournament {instance de Tournament}
        """
        for tour in tournament.rounds:
            print(tour)
            for match in tour.matches:
                print(match)
            print()
            
    def show_all_rounds_all_tournaments(self, all_tournaments):
        """Affiche les caractéristiques des rounds du tournoi courant passé en paramètre.

        Args:
            tournament {instance de Tournament}
        """
        for tournament in all_tournaments:
            print("Tournoi " + str(all_tournaments.index(tournament) + 1))
            print(tournament)
            for tour in tournament.rounds:
                print(tour)
                for match in tour.matches:
                    print(match)
                print()
            print()

    def show_round_controller(self, memo_match):
        """Permet d'afficher les tupples mémorisés des couples de joueur ayant déjà joué ensemble
        """
        print("couples de joueurs ayant déjà joué ensemble")
        for match in memo_match:
            print(str(match))
            
    def max_rounds_alert(self):
        """Alerte de fin de tournoi
        """
        print("Tous les rounds prévus ont été joués.")
        print("Si tous les scores ont été saisis, le tournoi est terminé!")
