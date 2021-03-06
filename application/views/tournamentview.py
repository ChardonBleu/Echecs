from ..utils.constants import NUMBER_ROUNDS


class TournamentView:
    """
        Interface destinée à la gestion du tournois:
        Choix paramètres tournois: nom, site, dates début et fin, description
        timecontrol et number of rounds
    """

    def prompt_name_tournament(self):
        """Name of the tournament.

        Returns:
            string -- Is used for tournament instantiation.
        """
        name_tournament = input("Nom du tournoi: ")
        return name_tournament

    def prompt_site_tournament(self):
        """Site of the tournament.

        Returns:
            string -- Is used for tournament instantiation.
        """
        site_tournament = input("Lieu du tournoi: ")
        return site_tournament

    def prompt_date_begin_tournament(self):
        """Date of the begining of the tournament.

        Returns:
            string -- Is used for tournament instantiation.
        """
        date_debut_tournament = input("Date de début: ")
        return date_debut_tournament

    def prompt_date_end_tournament(self):
        """Date of the end of the tournament.

        Returns:
            string -- Is used for tournament instantiation.
        """
        date_debut_tournament = input("Date de fin: ")
        return date_debut_tournament

    def prompt_description_tournament(self):
        """description of tournament.

        Returns:
            string -- Is used for tournament instantiation.
        """
        description_tournament = input("Description du tournoi: ")
        return description_tournament

    def prompt_time_control(self):
        """choice of time control bullet, blitz or "coup rapide".

        Raises:
            ValueError: In case of non positive integer value or value > 3

        Returns:
            int -- used to select time-control in constant list for tournament instantiation.
        """
        print("Choix du contrôle du temps.")
        while True:
            try:
                index_time_control = int(input("Pour un bullet entrez: 1, " +
                                               "pour un blitz entrez: 2, " +
                                               "pour un coup rapide entrez: 3\n"))
                if index_time_control > 3 or index_time_control < 0:
                    raise ValueError
            except ValueError:
                print("Il faut saisir un entier !")
            else:
                break
        return index_time_control - 1

    def prompt_number_rounds(self):
        """
        Choice of the number of rounds if different from 4

        Raises:
            ValueError: In case of non positive integer value

        Returns:
            int -- number of rounds. Is used for tournament instantiation
        """
        loop = True
        while loop:
            prompt = input("Voulez vous un nombre de rounds supèrieur à 4? Y/N: ")
            if prompt == "N":
                number_rounds = NUMBER_ROUNDS
                loop = False
            if prompt == "Y":
                while loop:
                    number_rounds = input("Entrez le nombre de rounds.\n")
                    try:
                        number_rounds = int(number_rounds)
                        if number_rounds <= 0:
                            raise ValueError
                    except ValueError:
                        print("Il faut saisir un entier supèrieur à zéro.")
                    else:
                        loop = False
        return number_rounds

    def prompt_id_tournament(self):
        """[summary]
        """
        while True:
            try:
                bdd_id = int(input("Saisir l'id du tournoi que vous souhaitez charger: "))
                if bdd_id < 0:
                    raise ValueError
            except ValueError:
                print("Il faut saisir un entier positif !")
            else:
                break
        return bdd_id

    def show_tournament(self, tournament):
        """Affiche les caractéristiques du tournois.

        Arguments:
            tournament (instance de Tournament)
        """
        print()
        print(tournament)
        print()

    def alert_no_tournament(self):
        """Afffiche un alerte en cas de demande d'affichage d'un tournoi vide
        """
        print("Aucun tournoi courant n'a encore été chargé ou créé")
