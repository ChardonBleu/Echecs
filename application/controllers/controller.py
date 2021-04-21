from .playercontroller import PlayerController
from .tournamentcontroller import TournamentController
from .roundcontroller import RoundController



class Controller:
    """
    Controleur général -- en chantier -- Permet de tester des séquences d'évènements

    Attributs:
        self.tournament_controller  (objet TournamentController)  -- Contrôle le tournoi courant
        self.players_controller  (objet PlayerController)  -- Contrôle les joueurs du tournoi courant
        self.round_controller  (objet RoundController)  -- Contrôle les rounds du tournoi courant
    """

    def __init__(self):
        self.tournament_controller = TournamentController()
        self.players_controller = PlayerController()
        self.round_controller = RoundController()
        

    def link_players_with_tournament(self):
        """Prend la liste des joueurs chargés depuis la bdd ou bien saisie à la main
        et l'associe au tournoi courant en renseignant l'attribut self.players de la classe Tournament.
        Cette liste contient les id des joueurs dans la table players de la bdd.
        """
        id_list = self.players_controller.players_manager.liste_id_players
        self.tournament_controller.tournament.tournament_players(id_list)

    def start_first_round(self):
        """Crée le premier round
        """
        self.tournament_controller.tournament.add_round()
        player_to_pair = 0
        other_player = 4
        while player_to_pair < 4:
            self.add_match_and_memorise(player_to_pair, other_player)
            player_to_pair += 1
            other_player += 1

    def new_round_with_control(self, nb_rounds):
        """Crée un nouveau round en veillant à ce que les joueurs ne se soient pas déjà affrontés.
        Méthode appelée aprés nouveau tri des joueurs par classement et score.

        Arguments:
            nb_rounds (int) -- transporté de méthode en méthode pour évaluer le nombre de matchs déjà créés.
        """
        self.tournament_controller.tournament.add_round()
        liste_index_joueur = [0, 1, 2, 3, 4, 5, 6, 7]  # Permet de décompter les joueurs disponibles pour appairage
        while len(liste_index_joueur) >= 2:
            liste_index_joueur = self.search_couple_for_first_player(liste_index_joueur, nb_rounds)

    def search_couple_for_first_player(self, liste_index_joueur, nb_rounds):
        """Lance la méthode de recherche d'un joueur à appairer avec le premier joueur de la liste.
        Une fois ce joueur trouvé on supprime de la liste les index de ces deux joueurs.

        Arguments:
            liste_index_joueur (list) -- liste des index des joueurs disponibles pour appairage
            nb_rounds          (int)  -- transporté de méthode en méthode pour évaluer le nombre de match déjà créés

        Returns:
            liste_index_joueur {list} -- liste modifiée des index des joueurs disponibles pour appairage
        """
        player_to_pair = liste_index_joueur[0]
        number_matches_before = self.tournament_controller.tournament.rounds[nb_rounds - 1].len_matches_list
        # On lance la méthode de recherche d'appairage et on récupère l'index du joueur sélectionné
        index_other_player = self.examine_other_players_as_candidate(liste_index_joueur, player_to_pair)
        other_player = liste_index_joueur[index_other_player]
        # si le saut mène au dernier joueur de la liste et qu'aucun match n'a été encore ajouté, on le rajoute
        number_matches_after = self.tournament_controller.tournament.rounds[nb_rounds - 1].len_matches_list
        if index_other_player == len(liste_index_joueur) - 1 and number_matches_before == number_matches_after:
            self.add_match_and_memorise(player_to_pair, other_player)
        # On retire les joueurs mis en match de la liste des joueurs dispo pour appairage:
        liste_index_joueur.remove(player_to_pair)
        liste_index_joueur.remove(other_player)
        return liste_index_joueur

    def examine_other_players_as_candidate(self, liste_index_joueur, player_to_pair, index_other_player=1):
        """Recherche un joueur à appairer avec le joueur d'index player_to_pair.
        Si on ne trouve pas d'appairage avec le joueur juste aprés player_to_pair dans la liste,
        on cherche avec le suivant en faisant un appel rescursif de la méthode avec en argument
        index_other_player + 1.
        Le cas où un appairage n'a toujours pas été trouvé quand on arrive au bout de la liste
        est traité dans la méthode search_couple_for_first_player()

        Arguments:
            liste_index_joueur (list) -- liste des index des joueurs disponibles pour appairage
            player_to_pair     (int)  -- valeur du joueur à appairer dans liste_index_joueur
                                         (valeur de liste_index_joueur[0])
            index_other_player (int)  --  correspond à index de other_player dans liste_index_joueur

        Returns:
            index_other_player (int) -- correspond à index de other_player dans liste_index_joueur
        """
        other_player = liste_index_joueur[index_other_player]
        candidate_couple = (self.players_controller.players_manager.bdd_id[player_to_pair],
                            self.players_controller.players_manager.bdd_id[other_player])
        if candidate_couple not in self.round_controller.memo_match:
            self.add_match_and_memorise(player_to_pair, other_player)
        else:
            if index_other_player < len(liste_index_joueur) - 1:
                index_other_player = self.examine_other_players_as_candidate(liste_index_joueur,
                                                                             player_to_pair,
                                                                             index_other_player + 1)
        return index_other_player

    def add_match_and_memorise(self, player_to_pair, other_player):
        """Rajoute au tournoi un match entre les joueurs d'index "player_to_pair" et "other_player"

        Arguments:
            player_to_pair (int) -- index permettant de récupérer l'id du joueur
            other_player (int) -- index permettant de récupérer l'id du joueur
        """
        self.tournament_controller.tournament.add_match_to_last_round(
            self.players_controller.players_manager.bdd_id[player_to_pair],
            self.players_controller.players_manager.bdd_id[other_player], 0, 0)
        self.memorise_matches(player_to_pair, other_player)

    def memorise_matches(self, player_to_pair, other_player):
        """Stocke dans une liste de tupples dans l'attribut self.memo_match de RoundController
        les couples de joueurs s'étant déjà affrontés: (joueur1, joueur2) et (joueur2, joueur1)

        Arguments:
            player_to_pair (int) -- index permettant de récupérer l'id du joueur
            other_player (int) -- index permettant de récupérer l'id du joueur
        """
        self.round_controller.memo_match.append(
            (self.players_controller.players_manager.bdd_id[player_to_pair],
             self.players_controller.players_manager.bdd_id[other_player]))
        self.round_controller.memo_match.append(
            (self.players_controller.players_manager.bdd_id[other_player],
             self.players_controller.players_manager.bdd_id[player_to_pair]))

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

        """# Instancie un nouveau tournoi
        self.tournament_controller.new_tournament()"""

        """# Ajoute manuellement 8 joueurs au tournoi courant
        self.players_controller.add_8_players()
        # Sauvegarde les joueurs entrés manuellement dans la BDD
        self.players_controller.players_manager.save_players_BDD()"""

        """# Charge  8 joueurs de la bdd à partir de leur bdd_id saisis par l'utilisateur
        list_id_bdd = self.players_controller.view.prompt_list_id_bdd_players()
        self.players_controller.players_manager.load_players_with_bdd_id_list(list_id_bdd)"""

        """# Lie les joueurs entrés manuellement et ajoutées à la BDD au tournoi courant.
        self.link_players_with_tournament()
        # Affiche le résumé des données du tournois.
        self.tournament_controller.view.show_tournament(self.tournament_controller.tournament)"""

        """# Charger tous les joueurs de la bdd dans une variable
        all_players = self.players_controller.players_manager.load_all_players_from_bdd()
        # Affiche la liste de tous les joueurs de la bddS
        self.players_controller.show_players(all_players)
        # Tri des TOUS les joueurs par classement ELO décroissant
        self.players_controller.players_manager.sort_players_by_score_and_ranking(all_players)
        # Affiche la liste de tous les joueurs de la bdd
        self.players_controller.show_players(all_players)
        # Tri des TOUS les joueurs par ordre alphabétique croissant
        self.players_controller.players_manager.sort_players_by_name(all_players)
        # Affiche la liste de tous les joueurs de la bdd
        self.players_controller.show_players(all_players)"""

        """nb_rounds = 1
        # Tri des joueurs du tournoi courant par classement ELO décroissant
        self.players_controller.players_manager.sort_players_by_score_and_ranking(
            self.players_controller.players_manager)
        # Affiche la liste des joueurs avec leur classement
        self.players_controller.show_players(self.players_controller.players_manager)
        # Démarre le premier round en affectant les joueurs aux match à partir de la liste triée juste précédement
        self.start_first_round()
        # Affiche les matchs des rounds
        self.round_controller.view.show_rounds_with_matches(self.tournament_controller.tournament, nb_rounds)

        # Clos le  round avec saisie des scores:
        results_round = self.tournament_controller.close_last_round_with_scores()
        self.round_controller.view.show_rounds_with_matches(self.tournament_controller.tournament, nb_rounds)
        self.players_controller.players_manager.update_scores_players(results_round)
        
        # Sauvegarde dans la bdd du tournoi en cours - Update si sauvegarde existe déjà
        self.tournament_controller.tournament_manager.save_tournaments_bdd(self.tournament_controller.tournament)"""
        
        # ***********************   STOP   ********************************************************

        """# Charge le dernier tournoi sauvegardé
        last_tournament = self.tournament_controller.tournament_manager.load_last_saved_tournament()
        self.tournament_controller.tournament =  last_tournament"""
        """# ou bien
        # Charge un tournoi dont l'utilisateur a donné d'id de la bdd
        bdd_id = self.tournament_controller.view.prompt_id_tournament()
        self.tournament_controller.tournament = self.tournament_controller.tournament_manager.load_tournament_by_id(
            bdd_id)"""
        """ # Affiche le résumé des données du tournois
        self.tournament_controller.view.show_tournament(self.tournament_controller.tournament)
        # Affiche tous les rounds avec tous les matchs
        self.round_controller.view.show_all_rounds(self.tournament_controller.tournament)
        # Charge les joueurs de ce tournoi dans le playermanager
        self.players_controller.players_manager.load_players_with_bdd_id_list(
            self.tournament_controller.tournament.liste_id_players)
        # Recalcule leur score à partir des données du tournoi chargé
        results_round = self.tournament_controller.tournament.recover_scores_for_loaded_tournament()
        self.players_controller.players_manager.update_scores_players(results_round)
        # Récupère la liste des joueurs ayant déjà joué ensemble
        self.tournament_controller.recover_couples_players_for_memorize()
        # Affiche la liste des joueurs avec leur classement
        self.players_controller.show_players(self.players_controller.players_manager)
        # Récupère le numéro de round en cours
        nb_rounds = len(self.tournament_controller.tournament.rounds)


        # Tri des joueurs du tournoi courant par score à l'issu du round
        self.players_controller.players_manager.sort_players_by_score_and_ranking(
            self.players_controller.players_manager)
        self.players_controller.show_players(self.players_controller.players_manager)

        nb_rounds += 1
        while nb_rounds <= self.tournament_controller.tournament.number_rounds:
            # Tri des joueurs du tournoi courant par classement ELO décroissant
            self.players_controller.players_manager.sort_players_by_score_and_ranking(
                self.players_controller.players_manager)
            # Démarre le round suivant en affectant les joueurs aux match à partir de la liste triée juste précédement
            self.new_round_with_control(nb_rounds)
            # Affiche les matchs des rounds
            self.round_controller.view.show_rounds_with_matches(
                self.tournament_controller.tournament, nb_rounds)

            # Clos le  round avec saisie des scores:
            results_round = self.tournament_controller.close_last_round_with_scores()
            self.round_controller.view.show_rounds_with_matches(self.tournament_controller.tournament, nb_rounds)
            self.players_controller.players_manager.update_scores_players(results_round)
            
            # Sauvegarde dans la bdd du tournoi en cours - Update si sauvegarde existe déjà
            self.tournament_controller.tournament_manager.save_tournaments_bdd(self.tournament_controller.tournament)

            # Tri des joueurs du tournoi courant par score à l'issu du round
            self.players_controller.players_manager.sort_players_by_score_and_ranking(
                self.players_controller.players_manager)
            self.players_controller.show_players(self.players_controller.players_manager)
            nb_rounds += 1

        # Affiche tous les rounds avec tous les matchs
        self.round_controller.view.show_all_rounds(self.tournament_controller.tournament)"""
        
        # ************* REPRISE JUSQUE LA *************************************
        
        """# Mise à jour des classements
        self.players_controller.update_ranking_players()"""

        """# Sauvegarde dans la bdd du tournoi en cours
        self.tournament_controller.tournament_manager.save_tournaments_bdd(self.tournament_controller.tournament)  """

        """# Tri des joueurs courants par ordre alphabétique croissant
        self.players_controller.players_manager.sort_players_by_name(self.players_controller.players_manager)
        # Affiche la liste des joueurs avec leur classement
        self.players_controller.show_players(self.players_controller.players_manager)"""

        """"""
        
        """# Clos le round avec saisie des scores:
        results_round = self.tournament_controller.close_last_round_with_scores()
        self.round_controller.view.show_rounds_with_matches(self.tournament_controller.tournament, nb_rounds)
        self.players_controller.players_manager.update_scores_players(results_round)

        nb_rounds += 1
        while nb_rounds <= self.tournament_controller.tournament.number_rounds:
            # Tri des joueurs du tournoi courant par classement ELO décroissant
            self.players_controller.players_manager.sort_players_by_score_and_ranking(
                self.players_controller.players_manager)
            # Démarre le round suivanten affectant les joueurs aux match à partir de la liste triée juste précédement
            self.new_round_with_control(nb_rounds)
            # Affiche les matchs des rounds
            self.round_controller.view.show_rounds_with_matches(
                self.tournament_controller.tournament, nb_rounds)
            # Clos le  round avec saisie des scores:
            results_round = self.tournament_controller.close_last_round_with_scores()
            self.round_controller.view.show_rounds_with_matches(self.tournament_controller.tournament, nb_rounds)
            self.players_controller.players_manager.update_scores_players(results_round)

            # Tri des joueurs du tournoi courant par score à l'issu du round
            self.players_controller.players_manager.sort_players_by_score_and_ranking(
                self.players_controller.players_manager)
            self.players_controller.show_players(self.players_controller.players_manager)
            nb_rounds += 1
        
        # Sauvegarde dans la bdd du tournoi en cours - Update si sauvegarde existe déjà
        self.tournament_controller.tournament_manager.save_tournaments_bdd(self.tournament_controller.tournament)"""
      
        # Chargement de tous les tournois de la bdd
        all_tournaments = self.tournament_controller.tournament_manager.load_all_tournaments()
        # Affichage de tous les tournois (liste) sans les rounds
        self.tournament_controller.view.show_tournament(all_tournaments)
        # Affiche de tous les tournois AVEC tous les rounds avec tous les matchs
        self.round_controller.view.show_all_rounds_all_tournaments(all_tournaments.tournaments)
