class ManagerTournamentView:
    """
        Interface destinée à la gestion du tournois:
            * choix paramètres tournois: nom, site, dates début et fin, timecontrol, description
            * ajout nouveaux joueurs
            * saisie scores match
            * affichage liste joueurs avec classement
            * affichage résultat score round
            * affichage résultat tournois
    """
    
    def prompt_name_tournament(self):
        name_tournament = input("Nom du tournoi: ")
        if name_tournament == "":
            return None
        return name_tournament
    
    def prompt_site_tournament(self):
        site_tournament = input("Lieu du tournoi: ")
        if site_tournament == "":
            return None
        return site_tournament
    
    def prompt_date_debut_tournament(self):
        date_debut_tournament = input("Date de début: ")
        if date_debut_tournament == "":
            return None
        return date_debut_tournament
    
    def prompt_date_fin_tournament(self):
        date_debut_tournament = input("Date de début: ")
        if date_debut_tournament == "":
            return None
        return date_debut_tournament
    
    def prompt_description_tournament(self):
        description_tournament = input("Description du tournoi: ")
        if description_tournament == "":
            return None
        return description_tournament
    
    def prompt_time_control(self):
        print("Choix du contrôle du temps.")
        index_time_control = input("Pour un bullet entrez: 1, pour un blitz entrez: 2, pour un coup rapide entrez: 3")
        return index_time_control
    
    def prompt_number_rounds(self):
        number_rounds = input("Entrez le nombre de rounds si vous voulez qu'il soit supèrieur à 4.")
        if number_rounds != "":
            return number_rounds
            
        
    