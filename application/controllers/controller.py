from .playercontroller import PlayerController
from .tournamentcontroller import TournamentController
from .roundcontroller import RoundController


class Controller:
    """
    Controleur général -- en chantier -- Permet de tester des séquences d'évènements
    """

    def __init__(self):
        """[summary]
        """
        self.tournament_controller = TournamentController()
        self.players_controller = PlayerController()
        self.round_controller = RoundController()

    def link_players_with_tournament(self):
        """Associe la liste des joueurs chargés au tournoi courant
        en renseignant l'attribut self.players de la classe Tournament
        avec la liste des id des joueurs.
        Cet id est celui du joueur dans la BDD
        """
        id_list = self.players_controller.players_manager.liste_id_players
        self.tournament_controller.tournament.tournament_players(id_list)

    def start_first_round(self):
        """Créée un round rempli de match avec les joueurs triés de self.players de PlayerManager
        """
        self.tournament_controller.tournament.add_round()
        index_joueur = 0
        while index_joueur < 8:
            self.tournament_controller.tournament.add_match_to_last_round(
                self.players_controller.players_manager.bdd_id[index_joueur],
                self.players_controller.players_manager.bdd_id[index_joueur + 1], 0, 0)
            self.memorise_match_historical(index_joueur)
            index_joueur += 2
    
    def memorise_match_historical(self, index_joueur):
        """Stocke dans une liste de tupples dans l'attribut self.memo_match de RoundController
        les couples de joueurs s'étant déjà affrontés: (joueur1, joueur2) et (joueur2, joueur1)
        """
        self.round_controller.memo_match.append(
            (self.players_controller.players_manager.bdd_id[index_joueur],
            self.players_controller.players_manager.bdd_id[index_joueur + 1]))
        self.round_controller.memo_match.append(
            (self.players_controller.players_manager.bdd_id[index_joueur + 1],
            self.players_controller.players_manager.bdd_id[index_joueur]))

    def resume_first_round_score(self, results_round):
        """[summary]
        """
        for id_players, round_score in results_round.items():
            player = self.players_controller.players_manager[id_players]
            player.update_score(round_score)

    def run(self):
        """Test de séquences d'évènements
        Lance la création d'un nouveau tournoi:
                Instancier nouveau tournoi
                Ajouter 8 joueurs à la main
                Sauvegarder ces 8 joueurs dans la bdd
                Associer joueurs et tournoi
                Afficher résumé tournoi
                Afficher tous les joueurs de la bdd

        A partir d'un tournoi avec ses 8 joueurs associés:
            Trier les joueurs par ordre décroissant de leur classement ELO
            Lancer le premier round avec les matchs
        """

        # Instancie un nouveau tournoi
        self.tournament_controller.new_tournament()

        """# Ajoute manuellement 8 joueurs au tournoi courant
        self.players_controller.add_8_players()
        # Sauvegarde les joueurs entrés manuellement dans la BDD
        self.players_controller.players_manager.save_players_BDD()"""

        # Charge les 8 premiers joueurs de la bdd pour test rapide appli
        self.players_controller.players_manager.load_8_players_from_bdd()

        # Lie les joueurs entrés manuellemetn et ajoutées à la BDD au tournoi courant
        self.link_players_with_tournament()
        # Affiche le résumé des données du tournois
        self.tournament_controller.view.show_tournament(self.tournament_controller.tournament)
        # Affiche la liste des joueurs avec leur classement
        self.players_controller.show_players(self.players_controller.players_manager)

        """# Charger tous les joueurs de la bdd dans une variable
        all_players = self.players_controller.players_manager.load_all_players_from_bdd()
        # Affiche la liste de tous les joueurs de la bddS
        self.players_controller.show_players(all_players)
        # Tri des TOUS les joueurs par classement ELO décroissant
        self.players_controller.sort_players_by_score_and_ranking(all_players)
        # Affiche la liste de tous les joueurs de la bdd
        self.players_controller.show_players(all_players)
        # Tri des TOUS les joueurs par ordre alphabétique croissant
        self.players_controller.sort_players_by_name(all_players)
        # Affiche la liste de tous les joueurs de la bdd
        self.players_controller.show_players(all_players)"""

        # Tri des joueurs du tournoi courant par classement ELO décroissant
        self.players_controller.sort_players_by_score_and_ranking(self.players_controller.players_manager)
        # Démarre le premier round en affectant les joueurs aux match à partir de la liste triée juste précédement
        self.start_first_round()
        # Affiche les matchs des rounds
        self.round_controller.view.show_rounds_with_matches(self.tournament_controller.tournament)

        # Clos le premier round avec saisie des scores:
        results_round = self.tournament_controller.close_last_round_with_scores()
        self.round_controller.view.show_rounds_with_matches(self.tournament_controller.tournament)
        self.resume_first_round_score(results_round)
        self.players_controller.show_players(self.players_controller.players_manager)

        # Tri des joueurs du tournoi courant par score à l'issu du round 1
        self.players_controller.sort_players_by_score_and_ranking(self.players_controller.players_manager)
        self.players_controller.show_players(self.players_controller.players_manager)
        
        # Affichage des couples de joueurs ayant déjà joué ensemble
        self.round_controller.view.show_round_controller(self.round_controller.memo_match)

        """# Tri des joueurs courants par ordre alphabétique croissant
        self.players_controller.sort_players_by_name(self.players_controller.players_manager)
        # Affiche la liste des joueurs avec leur classement
        self.players_controller.show_players(self.players_controller.players_manager)"""
