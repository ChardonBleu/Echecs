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
    """

    def __init__(self):
        self.controller = None
        self.gamecontroller = GameController()

    def run(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller.run()


class HomeMenuController:

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
        print("Dans le sous menu de '1.1. Charger dernier tournoi sauvegardé'")
        # Appel méthode correspondant à la séquence 1.1
        return LoadTournamentController()


class LoadTournamentIdController:
    
    def run(self):
        print("Dans le sous menu de '1.2. Charger  tournoi à partir de son id dans la BDD'")
        # Appel méthode correspondant à la séquence 1.2
        return LoadTournamentController()


# **************** Menu secondaire du 2. Créer nouveau tournoi **************** 
class CreateTournamentController:

    def run(self):
        print("Dans le sous menu de '2. Créer nouveau Tournoi'")
        return HomeMenuController()


# **************** Menu secondaire du 3. Rapports tournois **************** 
class ReportsController:

    def run(self):
        print("Dans le sous menu de '3. Rapports tournoi'")
        return HomeMenuController()


# **************** Menu secondaire du 4. Gérer tournoi **************** 
class TournamentManagerController:

    def run(self):
        print("Dans le sous menu de '4. Gérer Tournois'")
        return HomeMenuController()


# **************** Menu secondaire du 5.Gérer joueurs **************** 
class PlayersManagerController:

    def run(self):
        print("Dans le sous menu de '5. Gérer joueurs'")
        return HomeMenuController()


class LeavingController:

    def run(self):
        print("Dans le sous menu de '6. Quitter'")
