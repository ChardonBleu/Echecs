class ManagerTournamentView:
    """
        Interface destinée à la gestion du tournois:
            * choix paramètres tournois: nom, site, dates début et fin, timecontrol
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
        
    
    
    
    