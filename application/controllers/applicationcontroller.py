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
        while self.running:
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

class LoadTournamentController:
    pass

class CreateTournamentController:
    pass

class ReportsController:
    pass

class TournamentManagerController:
    pass

class PlayersManagerController:
    pass

class LeavingController:
    pass
