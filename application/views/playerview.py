class PlayerView:
    """
        Interface destinée à la gestion des joueurs:
        Choix paramètres nouveau joueur: first_name, last_name, birth_date, sexe, ranking
    """

    def prompt_first_name_player(self):
        """Player's first name.

        Returns:
            string -- Is used for adding new player.
        """
        print()
        first_name_player = input("Prénom du joueur: ")
        return first_name_player

    def prompt_last_name_player(self):
        """Player's last name.

        Returns:
            string -- Is used for adding new player.
        """
        last_name_player = input("Nom de famille du joueur: ")
        return last_name_player

    def prompt_birth_date_player(self):
        """Player's birth year.

        Returns:
            string -- Is used for adding new player.
        """
        birth_date_player = input("Année de naissance du joueur: ")
        return birth_date_player

    def prompt_sexe_player(self):
        """Player's gender.

        Returns:
            string -- Is used for adding new player.
        """
        while True:
            try:
                sexe_player = input("Genre du joueur (F/M): ")
                if (sexe_player != "F") and (sexe_player != "M"):
                    raise ValueError
            except ValueError:
                print("Il faut saisir 'M' ou 'F'")
            else:
                break
        return sexe_player

    def prompt_ranking_player(self):
        """Player's ranking.
        Pour ajouter un nouveau joueur ou pour mettre à jour le classement

        Returns:
            int --
        """
        while True:
            try:
                ranking_player = int(input("Classement du joueur: "))
                if ranking_player < 0:
                    raise ValueError
            except ValueError:
                print("Il faut saisir un entier positif !")
            else:
                break
        return ranking_player

    def show_player(self, players):
        """Affiche la liste des joueurs de ce tournois.

        Args:
            objet de PlayerManager()
            ou bien objet de Player() -- Utilise les méthodes __str__ de chacune de ces classes
        """
        print()
        print(players)

    def prompt_new_ranking_player(self, player):
        """Demande à l'utilisateur le nouveau classement pour chaque joueur à l'issu du tournoi
        """
        print()
        print(player)
        while True:
            try:
                new_ranking = int(input("Saisir le nouveau classement pour le joueur ci-dessus: "))
                if new_ranking < 0:
                    raise ValueError
            except ValueError:
                print("Il faut saisir un entier positif !")
            else:
                break
        return new_ranking

    def prompt_list_id_bdd_players(self, number_players_bdd):
        """Demande à l'utilisateur de donnes les id de la BDD des 8 joueurs qu'il souhaite charger

        Returns:
            list  --  liste des 8 id
        """
        bdd_id_list = []
        for counter in range(1, 9):
            while True:
                try:                    
                    id_new_player = (int(input("id du joueur" + str(counter) + ": ")))
                    print(id_new_player)
                    if id_new_player > number_players_bdd or id_new_player < 0:
                        raise ValueError
                    if id_new_player in bdd_id_list:
                        raise ArithmeticError
                except ValueError:
                    print("Il faut saisir un entier positif et infèrieur au nombre maxi de joueurs stockés: " + str(number_players_bdd) + " !")
                except ArithmeticError:
                    print("Ce joueur est déjà dans la liste!")
                else:
                    break
            bdd_id_list.append(id_new_player)
        return bdd_id_list
