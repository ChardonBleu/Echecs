from .gamecontroller import GameController

from ..utils.menu import Menu
from ..views.menuview import MenuView


class ApplicationController:
    """Contrôleur principal de l'application.
        Est instancié dans le main.py de l'application.
        Instancie le GameController qui gère le comportement des modèles.
        Gère la navigation dans les menus de l'application:
            self.controller reçoit un contrpoleur de menu différent en focntion du choix
            d'option de menu fait par l'utilisateur.
        
    Menu complet:
    
    1. Charger tournoi passé
        1. Charger dernier tournoi sauvegardé et affiche les données
        2. Charger un tournoi à partir de son id_bdd et affiche les données
        3. Retour
        
    2. Créer nouveau tournoi
        1. Ajouter joueurs
            1. Charger 8 joueurs à partir de leur id_bdd
            2. Entrer manuellement 8 nouveaux joueurs puis les sauvegarder
            3. Retour
        2. Créer nouveau tournoi
        3. Lier nouveau tournoi aux joueurs chargés puis afficher données
        4. Retour
        
    3. Rapports tournoi
	    1. Afficher liste de tous les tournois
	    2. Afficher liste de tous les tournois avec rounds et matchs
        3. Afficher liste de tous les tours et match du tournoi courant
        4. Retour
        
    4. Gérer tournoi
        1. Démarer premier round (tri, affectation matchs, affichage)
        2. Round suivant (tri, affectation matchs, affichage)
        3. terminer round en cours (saisie scores, tri,  affichages résultats)
        4. Sauvegarder tournoi
        5. Retour
        
    5. Gérer joueurs:
	    1. Mettre à jour classement ELO joueurs et sauvegarder dans bdd
	    2. Afficher tous les joueurs
            1. par ordre alphabétique
            2. par clasement
        3. Afficher joueurs du tournoi courant
            1. par ordre alphabétique
            2. par classement
	    4. Retour
     
    6. Quitter
    """

    def __init__(self):
        self.controller = None
        self.gamecontroller = GameController()

    def run(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller.run()


class HomeMenuController:
    """Menu principal
    
    1. Charger tournoi passé
    2. Créer nouveau tournoi
    3. Rapports tournoi
    4. Gérer tournoi
    5. Gérer joueurs    
    6. Quitter
    """

    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Charger tournoi passé", LoadTournamentController())
        self.menu.add("auto", "Créer nouveau tournoi", CreateTournamentController())
        self.menu.add("auto", "Rapports tournois", ReportsController())
        self.menu.add("auto", "Gérer un tournoi", TournamentManagerController())
        self.menu.add("auto", "Gérer les joueurs", PlayersManagerController())
        self.menu.add("auto", "Quitter", LeavingController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


# **************** Menu secondaire du 1. Charger tournoi passé **************** 
class LoadTournamentController:
    """ Menu secondaire du 1.
        1. Charger dernier tournoi sauvegardé et affiche les données
        2. Charger un tournoi à partir de son id_bdd et affiche les données
        3. Retour
    """
    
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Charger dernier tournoi sauvegardé", LoadLastTournamentController())
        self.menu.add("auto", "Charger un tournoi de la BDD à partir de son ID", LoadTournamentIdController())
        self.menu.add("auto", "Retour Menu principal", HomeMenuController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class LoadLastTournamentController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 1.1
        return LoadTournamentController()


class LoadTournamentIdController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 1.2
        return LoadTournamentController()


# **************** Menu secondaire du 2. Créer nouveau tournoi **************** 
class CreateTournamentController:
    """Menu secondaire du 2.
    
        1. Ajouter joueurs
            1. Charger 8 joueurs à partir de leur id_bdd
            2. Entrer manuellement 8 nouveaux joueurs puis les sauvegarder
            3. Retour
        2. Créer nouveau tournoi
        3. Lier nouveau tournoi aux joueurs chargés puis afficher données
        4. Retour    
    """

    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Ajouter des joueurs", AddPlayersController())
        self.menu.add("auto", "Créer nouveau tournoi", CreateNewTournamentController())
        self.menu.add("auto", "Rapports tournois", LinkPlayersTournamentController())
        self.menu.add("auto", "Retour Menu principal", HomeMenuController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class CreateNewTournamentController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 2.2
        return CreateTournamentController()


class LinkPlayersTournamentController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 2.3
        return CreateTournamentController()


# **************** Menu tertiaire du 2.1. Ajouter des joueurs **************** 
class AddPlayersController:
    
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Charger 8 joueurs de la BDD à partir de leur ID", Load8PlayersController())
        self.menu.add("auto", "Entrer manuellement 8 nouveaux joueurs et les sauvegarder dans la BDD", Add8PlayersController())
        self.menu.add("auto", "Retour", CreateTournamentController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class Load8PlayersController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 2.1.1
        return AddPlayersController()


class Add8PlayersController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 2.1.2
        return AddPlayersController()


# **************** Menu secondaire du 3. Rapports tournois **************** 
class ReportsController:
    """Menu secondaire du 3.
    
    	1. Afficher liste de tous les tournois
	    2. Afficher liste de tous les tournois avec rounds et matchs
        3. Afficher liste de tous les tours et match du tournoi courant
        4. Retour
    """

    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Afficher liste simple de tous les tournois", DisplayAllTournamentsController())
        self.menu.add("auto", "Afficher liste de tous les tournois avec rounds et matchs", DisplayAllRoundsController())
        self.menu.add("auto", "afficher liste de tous les rounds et match du tournoi courant", DisplayRoundsController())
        self.menu.add("auto", "Retour Menu principal", HomeMenuController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class DisplayAllTournamentsController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 3.1
        return ReportsController()


class DisplayAllRoundsController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 3.2
        return ReportsController()


class DisplayRoundsController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 3.3
        return ReportsController()


# **************** Menu secondaire du 4. Gérer tournoi **************** 
class TournamentManagerController:
    """Menu secondaire du 4.
        1. Démarer premier round (tri, affectation matchs, affichage)
        2. Round suivant (tri, affectation matchs, affichage)
        3. terminer round en cours (saisie scores, tri,  affichages résultats)
        4. Sauvegarder tournoi
        5. Retour    
    """

    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Démarrer premier round", StarsFisrtRoundController())
        self.menu.add("auto", "Saisir scores et clore round en cours", CloseRoundController())
        self.menu.add("auto", "Lancer Round suivant", NextRoundController())
        self.menu.add("auto", "Sauvegarder tournoi", SaveTournamentController())
        self.menu.add("auto", "Retour Menu principal", HomeMenuController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class StarsFisrtRoundController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 4.1
        return TournamentManagerController()


class CloseRoundController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 4.2
        return TournamentManagerController()


class NextRoundController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 4.3
        return TournamentManagerController()


class SaveTournamentController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 4.4
        return TournamentManagerController()


# **************** Menu secondaire du 5.Gérer joueurs **************** 
class PlayersManagerController:
    """Menu secondaire du 5.
    
        1. Mettre à jour classement ELO joueurs et sauvegarder dans bdd
	    2. Afficher tous les joueurs
            1. par ordre alphabétique
            2. par clasement
        3. Afficher joueurs du tournoi courant
            1. par ordre alphabétique
            2. par classement
	    4. Retour
    """

    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Mettre à jour classement ELO et sauvegarder", UpdateRankingController())
        self.menu.add("auto", "Afficher tous les joueurs", DisplayAllPlayersController())
        self.menu.add("auto", "Afficher les joueurs du tournoi courant", DispalyPlayersController())
        self.menu.add("auto", "Retour Menu principal", HomeMenuController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class UpdateRankingController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 5.1
        return PlayersManagerController()

# **************** Menu tertiaire du 5.2. Ajouter des joueurs **************** 
class DisplayAllPlayersController:
    
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Joueurs par nom", DislplayAllNameController())
        self.menu.add("auto", "Joueurs par classement ELO décroissant", DisplayAllRankingController())
        self.menu.add("auto", "Retour", PlayersManagerController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class DislplayAllNameController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 5.2.1.
        return PlayersManagerController()


class DisplayAllRankingController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 5.2.2
        return PlayersManagerController()


# **************** Menu tertiaire du 5.3. Ajouter des joueurs **************** 
class DispalyPlayersController:
    
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    def run(self):
        self.menu.add("auto", "Joueurs par nom", DislplayNameController())
        self.menu.add("auto", "Joueurs par classement ELO décroissant", DisplayRankingController())
        self.menu.add("auto", "Retour", PlayersManagerController())

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class DislplayNameController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 5.3.1.
        return PlayersManagerController()


class DisplayRankingController:
    
    def run(self):

        # Appel méthode correspondant à la séquence 5.3.2
        return PlayersManagerController()


# ****************** Sortie de l'application *****************
class LeavingController:

    def run(self):
        print("Dans le sous menu de '6. Quitter'")
