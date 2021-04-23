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
        """
        self.controller  :  contient le controlleur courant de navigation
        self.gamecontroller : contrôleur général du tournoi. Permet d'accéder 
                              à tous les objets et méthodes du tournoi courant.
                              Passé en argument à chaque instance de classe de navigation
        """
        self.controller = None
        self.gamecontroller = GameController()

    def run(self, *args):
        """Orchestre la navigation dans le menu.
        Arguments:
            *args :  permet de passe en arguments le nombre de rounds réalisés du tournois
            courant losrque c'est necessaire
        """
        self.controller = HomeMenuController(self.gamecontroller)
        while self.controller:
            self.controller = self.controller.run(args)


# *************************************************************************
# *************** CLASSES DE NAVIGATION DANS LE MENU **********************
# *************************************************************************


class HomeMenuController:
    """Menu principal
    
    1. Charger tournoi passé
    2. Créer nouveau tournoi
    3. Rapports tournoi
    4. Gérer tournoi
    5. Gérer joueurs    
    6. Quitter
    """

    def __init__(self, gamecontroller, nb_rounds=0):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu Principal:")
        self.view = MenuView(self.menu)
        self.gamecontroller = gamecontroller
        self.nb_rounds = nb_rounds

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- trnasporte en argument instance du controleur général du tournoi
        """
        self.menu.add("auto", "Charger tournoi passé", LoadTournamentController(self.gamecontroller))
        self.menu.add("auto", "Créer nouveau tournoi", CreateTournamentController(self.gamecontroller))
        self.menu.add("auto", "Rapports tournois", ReportsController(self.gamecontroller))
        self.menu.add("auto", "Gérer un tournoi", TournamentManagerController(self.gamecontroller, self.nb_rounds))
        self.menu.add("auto", "Gérer les joueurs", PlayersManagerController(self.gamecontroller))
        self.menu.add("auto", "Quitter", LeavingController(self.gamecontroller))

        user_choice = self.view.get_user_choice()
        return user_choice.handler


# **************** Menu secondaire du 1. Charger tournoi passé **************** 
class LoadTournamentController:
    """ Menu secondaire du 1.
        1. Charger dernier tournoi sauvegardé et affiche les données
        2. Charger un tournoi à partir de son id_bdd et affiche les données
        3. Retour
    """
    
    def __init__(self, gamecontroller, nb_rounds=1):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            nb_rounds  (int) -- nombre de rounds déjà réalisés dans le tournoi
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu de chargement de tournois passés:")
        self.view = MenuView(self.menu)
        self.gamecontroller = gamecontroller
        self.nb_rounds = nb_rounds

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- trnasporte en argument instance du controleur général du tournoi
        """        
        self.menu.add("auto", "Charger dernier tournoi sauvegardé", LoadLastTournamentController(self.gamecontroller, self.nb_rounds))
        self.menu.add("auto", "Charger un tournoi de la BDD à partir de son ID", LoadTournamentIdController(self.gamecontroller, self.nb_rounds))
        self.menu.add("auto", "Retour Menu principal", HomeMenuController(self.gamecontroller, self.nb_rounds))

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class LoadLastTournamentController:
    """Gère la navigation dans le menu et lance la séquence de menu 1.1
    """
    def __init__(self, gamecontroller, nb_rounds):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller
        self.nb_rounds = nb_rounds
    
    def run(self, *args):
        """Lance la séquence de menu 1.1:
        Charge le dernier tournoi sauvegardé dans la BDD et crée une instance de Tournament.
        Charge les 8 joueurs correspondant aux id de joueurs mémorisés dans cette instance de Tournament.
        Récupère les résultats des rounds ayant déjà eu lieu et met à jour les scores des joueurs avec ces résultats.
        Récupère la liste des tupples des couples de joueurs ayant déjà joué ensemble.
        Affiche le résumé des caractéristiques du tournoi, les rounds et match et les joueurs.
        Calcule le nombre de rounds déjà créés et le renvoie.

        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.nb_rounds = self.gamecontroller.load_last_tournament_and_display()
        return HomeMenuController(self.gamecontroller, self.nb_rounds)


class LoadTournamentIdController:
    
    def __init__(self, gamecontroller, nb_rounds):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller
        self.nb_rounds = nb_rounds

    def run(self, *args):

        """Lance la séquence de menu 1.2
        Charge un tournoi sauvegardé dans la BDD en demandant à l'utilisateur l'id de ce tournoi
        et crée une instance de Tournament.
        Charge les 8 joueurs correspondant aux id de joueurs mémorisés dans cette instance de Tournament.
        Récupère les résultats des rounds ayant déjà eu lieu et met à jour les scores des joueurs avec ces résultats.
        Récupère la liste des tupples des couples de joueurs ayant déjà joué ensemble.
        Affiche le résumé des caractéristiques du tournoi, les rounds et match et les joueurs.
        Calcule le nombre de rounds déjà créés et le renvoie.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.nb_rounds = self.gamecontroller.load_tournament_with_id_and_display()
        return HomeMenuController(self.gamecontroller, self.nb_rounds)


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

    def __init__(self, gamecontroller):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu de crétion d'un nouveau tournoi:")
        self.view = MenuView(self.menu)
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- trnasporte en argument instance du controleur général du tournoi
        """
        self.menu.add("auto", "Ajouter des joueurs", AddPlayersController)
        self.menu.add("auto", "Créer nouveau tournoi", CreateNewTournamentController)
        self.menu.add("auto", "Retour Menu principal", HomeMenuController)

        user_choice = self.view.get_user_choice()
        return user_choice.handler(self.gamecontroller)


class CreateNewTournamentController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Lance la séquence de menu 2.2
        Demande à l'utilisateur de saisir les données pour un nouveau tournoi.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.create_new_tournament()
        return CreateTournamentController(self.gamecontroller)


# **************** Menu tertiaire du 2.1. Ajouter des joueurs **************** 
class AddPlayersController:
    
    def __init__(self, gamecontroller):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu d'ajout de joueurs au nouveau tournoi:")
        self.view = MenuView(self.menu)
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- trnasporte en argument instance du controleur général du tournoi
        """
        self.menu.add("auto", "Charger 8 joueurs de la BDD à partir de leur ID", Load8PlayersController)
        self.menu.add("auto", "Entrer manuellement 8 nouveaux joueurs et les sauvegarder dans la BDD", Add8PlayersController)
        self.menu.add("auto", "Retour", CreateTournamentController)

        user_choice = self.view.get_user_choice()
        return user_choice.handler(self.gamecontroller)


class Load8PlayersController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Lance la séquence de menu 2.1.1
        Demande à l'utilisateur les id des joueurs qu'il veut faire jouer.
        Charge ces 8 joueurs de la BDD dans le PlayerManager.
        Affiche ces 8 joueurs.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.load_8_players_from_bdd_and_display()
        return CreateTournamentController(self.gamecontroller)


class Add8PlayersController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Lance la séquence de menu 2.1.2
        Demande à l'utiliateur de saisir 8 nouveaux joueurs.
        Sauvegarde ces joueurs dans la BDD.
        Affiche ces joueurs.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.load_and_save_8_players_and_display()
        return CreateTournamentController(self.gamecontroller)


# **************** Menu secondaire du 3. Rapports tournois **************** 
class ReportsController:
    """Menu secondaire du 3.
    
    	1. Afficher liste de tous les tournois
	    2. Afficher liste de tous les tournois avec rounds et matchs
        3. Afficher liste de tous les tours et match du tournoi courant
        4. Retour
    """

    def __init__(self, gamecontroller):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu d'affichage des rapports de tournois:")
        self.view = MenuView(self.menu)
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- trnasporte en argument instance du controleur général du tournoi
        """
        self.menu.add("auto", "Afficher liste simple de tous les tournois", DisplayAllTournamentsController)
        self.menu.add("auto", "Afficher liste de tous les tournois avec rounds et matchs", DisplayAllRoundsController)
        self.menu.add("auto", "afficher liste de tous les rounds et match du tournoi courant", DisplayRoundsController)
        self.menu.add("auto", "Retour Menu principal", HomeMenuController)

        user_choice = self.view.get_user_choice()
        return user_choice.handler(self.gamecontroller)


class DisplayAllTournamentsController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, gamecontroller, *args):
        """Lance la séquence de menu 3.1
        Affiche tous les tournois de la BDD, sans les détails de rounds.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.display_all_tournaments_without_rounds()
        return HomeMenuController(self.gamecontroller)


class DisplayAllRoundsController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, gamecontroller, *args):
        """Lance la séquence de menu 3.2
        Affiche tous les tournois de la BDD, avec les détails de rounds et matchs.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.display_all_tournaments_with_rounds()
        return HomeMenuController(self.gamecontroller)


class DisplayRoundsController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, gamecontroller, *args):
        """Lance la séquence de menu 3.3
        Affiche les rounds et match du tournoi courant.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.display_tournaments_rounds_and_match()
        return HomeMenuController(self.gamecontroller)


# **************** Menu secondaire du 4. Gérer tournoi **************** 
class TournamentManagerController:
    """Menu secondaire du 4.
        1. Démarer premier round (tri, affectation matchs, affichage)
        2. Round suivant (tri, affectation matchs, affichage)
        3. terminer round en cours (saisie scores, tri,  affichages résultats)
        4. Sauvegarder tournoi
        5. Retour    
    """

    def __init__(self, gamecontroller, nb_rounds=1):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            nb_rounds  (int) -- nombre de rounds déjà réalisés dans le tournoi
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu de gestion du tournoi courant:")
        self.view = MenuView(self.menu)
        self.nb_rounds = nb_rounds
        self.gamecontroller = gamecontroller
        

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- transporte en argument instance du controleur général du tournoi
        """
        self.menu.add("auto", "Démarrer premier round", StarsFisrtRoundController(self.gamecontroller, self.nb_rounds))
        self.menu.add("auto", "Saisir scores et clore round en cours", CloseRoundController(self.gamecontroller, self.nb_rounds))
        self.menu.add("auto", "Lancer Round suivant", NextRoundController(self.gamecontroller, self.nb_rounds))
        self.menu.add("auto", "Sauvegarder tournoi", SaveTournamentController(self.gamecontroller))
        self.menu.add("auto", "Retour Menu principal", HomeMenuController(self.gamecontroller))

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class StarsFisrtRoundController:

    def __init__(self, gamecontroller, nb_rounds):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller
        self.nb_rounds = nb_rounds

    def run(self, *args):
        """Lance la séquence de menu 4.1
        Trie les joueurs par scores et classement ELO décroissant.
        Affiche la liste triée.
        Ajoute un premier round avec les matchs et l'affiche.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        if self.nb_rounds == 0:
            self.nb_rounds = self.gamecontroller.start_first_round_and_display()
            return TournamentManagerController(self.gamecontroller, self.nb_rounds)
        else:
            self.gamecontroller.tournament_controller.round_controller.view.alert_control_first_round()
            return TournamentManagerController(self.gamecontroller, self.nb_rounds)


class CloseRoundController:
    
    def __init__(self, gamecontroller, nb_rounds):
        """
        Arguments:
            nb_rounds  (int) -- nombre de rounds déjà réalisés dans le tournoi
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.nb_rounds = nb_rounds
        self.gamecontroller = gamecontroller
    
    def run(self, *args):
        """Lance la séquence de menu 4.2
        Demande à l'utilisateur de saisir les scores et met à jour les scores totaux des joueurs.
        Affiche les joueurs.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        if not self.gamecontroller.tournament_controller.tournament.rounds[self.nb_rounds - 1].closed:
            self.nb_rounds = self.gamecontroller.close_round_and_display(self.nb_rounds)
            return TournamentManagerController(self.gamecontroller, self.nb_rounds)
        else:
            self.gamecontroller.tournament_controller.round_controller.view.alert_closed_round()
            return TournamentManagerController(self.gamecontroller, self.nb_rounds)


class NextRoundController:
    
    def __init__(self, gamecontroller, nb_rounds):
        """
        Arguments:
            nb_rounds  (int) -- nombre de rounds déjà réalisés dans le tournoi
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.nb_rounds = nb_rounds
        self.gamecontroller = gamecontroller
    
    def run(self, *args):
        """Lance la séquence de menu 4.3
        Vérifie qu'il reste des rounds à jouer.
        S'il en reste trie les joueurs par score et classement ELO puis crée un nouveau
        round avec les matchs.
        Affiche le round créé.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        if self.gamecontroller.tournament_controller.tournament.rounds[self.nb_rounds - 1].closed:
            self.nb_rounds = self.gamecontroller.start_next_round_and_display(self.nb_rounds)
            return TournamentManagerController(self.gamecontroller, self.nb_rounds)
        else:
            self.gamecontroller.tournament_controller.round_controller.view.alert_non_closed_round()
            return TournamentManagerController(self.gamecontroller, self.nb_rounds)


class SaveTournamentController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Lance la séquence de menu 4.4
        Sauvegarde le tournoi courant dans le BDD.
    
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.save_tournament()
        return TournamentManagerController(self.gamecontroller)


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

    def __init__(self, gamecontroller):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu de gestion des joueurs:")
        self.view = MenuView(self.menu)
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- trnasporte en argument instance du controleur général du tournoi
        """
        self.menu.add("auto", "Mettre à jour classement ELO et sauvegarder", UpdateRankingController)
        self.menu.add("auto", "Afficher tous les joueurs", DisplayAllPlayersController)
        self.menu.add("auto", "Afficher les joueurs du tournoi courant", DispalyPlayersController)
        self.menu.add("auto", "Retour Menu principal", HomeMenuController)

        user_choice = self.view.get_user_choice()
        return user_choice.handler(self.gamecontroller)


class UpdateRankingController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Lance la séquence de menu 5.1
        Demande à l'uitilisateur de saisir les nouveaux classements ELO.
        Met à jour les classement ELO dans la BDD.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.update_players_ranking_and_save()
        return HomeMenuController(self.gamecontroller)

# **************** Menu tertiaire du 5.2. Ajouter des joueurs **************** 
class DisplayAllPlayersController:
    
    def __init__(self, gamecontroller):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu de rapports des joueurs de la base de données:")
        self.view = MenuView(self.menu)
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- trnasporte en argument instance du controleur général du tournoi
        """
        self.menu.add("auto", "Joueurs par nom", DislplayAllNameController)
        self.menu.add("auto", "Joueurs par classement ELO décroissant", DisplayAllRankingController)
        self.menu.add("auto", "Retour", PlayersManagerController)

        user_choice = self.view.get_user_choice()
        return user_choice.handler(self.gamecontroller)


class DislplayAllNameController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):

        """Lance la séquence de menu 5.2.1
        Affiche tous les joueurs triés par nom.
        
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.display_all_players_by_name()
        return PlayersManagerController(self.gamecontroller)


class DisplayAllRankingController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):

        """Lance la séquence de menu 5.2.2
        Affiche tous les joueurs triés par classement ELO décroissant.
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.display_all_players_by_ranking()
        return PlayersManagerController(self.gamecontroller)


# **************** Menu tertiaire du 5.3. Ajouter des joueurs **************** 
class DispalyPlayersController:
    
    def __init__(self, gamecontroller):
        """Construit le Menu de la classe et la vue pour ce menu

        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.menu = Menu("Menu de rapport des joueurs du tournoi courant:")
        self.view = MenuView(self.menu)
        self.gamecontroller = gamecontroller

    def run(self, *args):
        """Ajoute les entrées au menu de cette classe.
        Affiche le menu et demande à l'utilisateur de choisir une option

        Returns:
            (instance du controller choisi ) -- trnasporte en argument instance du controleur général du tournoi
        """
        self.menu.add("auto", "Joueurs par nom", DislplayNameController)
        self.menu.add("auto", "Joueurs par classement ELO décroissant", DisplayRankingController)
        self.menu.add("auto", "Retour", PlayersManagerController)

        user_choice = self.view.get_user_choice()
        return user_choice.handler(self.gamecontroller)


class DislplayNameController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):

        """Lance la séquence de menu 5.3.1
        Affiche les joueurs du tournoi courant triés par nom.
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.display_players_by_name()
        return PlayersManagerController(self.gamecontroller)


class DisplayRankingController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):

        """Lance la séquence de menu 5.3.2
        Affiche les joueurs du tournoi courant triés par classement ELO décroissant.
        Returns:
            (objet GameController) -- controller général du jeu
        """
        self.gamecontroller.display_players_by_ranking()
        return PlayersManagerController(self.gamecontroller)


# ****************** Sortie de l'application *****************
class LeavingController:

    def __init__(self, gamecontroller):
        """
        Arguments:
            gamecontroller (instance de GameController) -- contrôleur général du tournoi. Permet d'accéder 
                                                           à tous les objets et méthodes du tournoi courant.
        """
        self.gamecontroller = gamecontroller

    def run(self, *args):
        pass
