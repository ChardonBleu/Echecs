from .playercontroller import PlayerController
from .tournamentcontroller import TournamentController
from .roundcontroller import RoundController



class GameController:
    """
    Controleur général -- en chantier -- Permet de tester des séquences d'évènements

    Attributs:
        self.tournament_controller  (objet TournamentController)  -- Contrôle le tournoi courant
        self.players_controller  (objet PlayerController)  -- Contrôle les joueurs du tournoi courant
    """

    def __init__(self):
        self.tournament_controller = TournamentController()
        self.players_controller = PlayerController()        

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
        if candidate_couple not in self.tournament_controller.round_controller.memo_match:
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
        self.tournament_controller.round_controller.add_players_to_memo_match(
            self.players_controller.players_manager.bdd_id[player_to_pair],
            self.players_controller.players_manager.bdd_id[other_player])
        self.tournament_controller.round_controller.add_players_to_memo_match(
            self.players_controller.players_manager.bdd_id[other_player],
            self.players_controller.players_manager.bdd_id[player_to_pair])

    # **********************************************************************************
    # ***************** METHODES DE SEQUENCES DU MENU **********************************
    # **********************************************************************************
    
    def load_last_tournament_and_display(self):
        """Séquence menu 1.1
        Charge le dernier tournoi sauvegardé dans la BDD et crée une instance de Tournament.
        Charge les 8 joueurs correspondant aux id de joueurs mémorisés dans cette instance de Tournament.
        Récupère les résultats des rounds ayant déjà eu lieu et met à jour les scores des joueurs avec ces résultats.
        Récupère la liste des tupples des couples de joueurs ayant déjà joué ensemble.
        Affiche le résumé des caractéristiques du tournoi, les rounds et match et les joueurs.
        Calcule le nombre de rounds déjà créés et le renvoie.
        
        Returns:
            nb_rounds (int) -- Nombre de rounds ayant déjà été créé
        """
        last_tournament = self.tournament_controller.tournament_manager.load_last_saved_tournament()
        self.tournament_controller.tournament =  last_tournament
        self.players_controller.players_manager.load_players_with_bdd_id_list(
            self.tournament_controller.tournament.liste_id_players)
        results_round = self.tournament_controller.tournament.recover_scores_for_loaded_tournament()
        self.players_controller.players_manager.update_scores_players(results_round)
        self.tournament_controller.recover_couples_players_for_memorize()
        self.tournament_controller.view.show_tournament(self.tournament_controller.tournament)
        self.tournament_controller.round_controller.view.show_all_rounds(self.tournament_controller.tournament)
        self.players_controller.show_players(self.players_controller.players_manager)
        nb_rounds = len(self.tournament_controller.tournament.rounds)
        return nb_rounds

    def load_tournament_with_id_and_display(self):
        """Séquence menu 1.2
        Charge un tournoi sauvegardé dans la BDD en demandant à l'utilisateur l'id de ce tournoi
        et crée une instance de Tournament.
        Charge les 8 joueurs correspondant aux id de joueurs mémorisés dans cette instance de Tournament.
        Récupère les résultats des rounds ayant déjà eu lieu et met à jour les scores des joueurs avec ces résultats.
        Récupère la liste des tupples des couples de joueurs ayant déjà joué ensemble.
        Affiche le résumé des caractéristiques du tournoi, les rounds et match et les joueurs.
        Calcule le nombre de rounds déjà créés et le renvoie.
        
        Returns:
            nb_rounds (int) -- Nombre de rounds ayant déjà été créé
        """
        bdd_id = self.tournament_controller.view.prompt_id_tournament()
        self.tournament_controller.tournament = self.tournament_controller.tournament_manager.load_tournament_by_id(
            bdd_id)
        self.players_controller.players_manager.load_players_with_bdd_id_list(
            self.tournament_controller.tournament.liste_id_players)
        results_round = self.tournament_controller.tournament.recover_scores_for_loaded_tournament()
        self.players_controller.players_manager.update_scores_players(results_round)
        self.tournament_controller.recover_couples_players_for_memorize()
        self.tournament_controller.view.show_tournament(self.tournament_controller.tournament)
        self.tournament_controller.round_controller.view.show_all_rounds(self.tournament_controller.tournament)
        self.players_controller.show_players(self.players_controller.players_manager)
        nb_rounds = len(self.tournament_controller.tournament.rounds)
        return nb_rounds
    
    def load_8_players_from_bdd_and_display(self):
        """Séquence menu 2.1.1
        Demande à l'utilisateur les id des joueurs qu'il veut faire jouer.
        Charge ces 8 joueurs de la BDD dans le PlayerManager.
        Affiche ces 8 joueurs.
        """
        number_players_bdd = self.players_controller.players_manager.evaluate_number_players_bdd()
        list_id_bdd = self.players_controller.view.prompt_list_id_bdd_players(number_players_bdd)
        self.players_controller.players_manager.load_players_with_bdd_id_list(list_id_bdd)
        self.players_controller.show_players(self.players_controller.players_manager)
        if self.tournament_controller.tournament:
            self.link_players_with_tournament()
            self.tournament_controller.view.show_tournament(self.tournament_controller.tournament)
        else:
            pass
    
    def load_and_save_8_players_and_display(self):
        """Séquence menu 2.1.2
        Demande à l'utiliateur de saisir 8 nouveaux joueurs.
        Sauvegarde ces joueurs dans la BDD.
        Affiche ces joueurs.
        """
        self.players_controller.add_8_players()
        self.players_controller.players_manager.save_players_bdd()
        self.players_controller.show_players(self.players_controller.players_manager)
        if self.tournament_controller.tournament:
            self.link_players_with_tournament()
            self.tournament_controller.view.show_tournament(self.tournament_controller.tournament)
        else:
            pass

    def create_new_tournament(self):
        """Séquence menu 2.2
        Demande à l'utilisateur de saisir les données pour un nouveau tournoi.
        """
        self.tournament_controller.new_tournament()
        if len(self.players_controller.players_manager.players) == 8:
            self.link_players_with_tournament()
            self.tournament_controller.view.show_tournament(self.tournament_controller.tournament)
        else:
            pass        
        
    def display_all_tournaments_without_rounds(self):
        """Séquence menu 3.1
        Affiche tous les tournois de la BDD, sans les détails de rounds. 
        """
        all_tournaments = self.tournament_controller.tournament_manager.load_all_tournaments()
        self.tournament_controller.view.show_tournament(all_tournaments)
    
    def display_all_tournaments_with_rounds(self):
        """Séquence menu 3.2
        Affiche tous les tournois de la BDD, avec les détails de rounds et matchs.
        """
        all_tournaments = self.tournament_controller.tournament_manager.load_all_tournaments()
        self.tournament_controller.round_controller.view.show_all_rounds_all_tournaments(all_tournaments.tournaments)
        
    def display_tournaments_rounds_and_match(self):
        """Séquence menu 3.3
        Affiche les rounds et match du tournoi courant.
        """
        self.tournament_controller.round_controller.view.show_all_rounds(self.tournament_controller.tournament)
        
    def start_first_round_and_display(self):
        """Séquence menu 4.1
        Trie les joueurs par scores et classement ELO décroissant.
        Affiche la liste triée.
        Ajoute un premier round avec les matchs et l'affiche.
                        
        Returns:
            nb_rounds (int) -- Nombre de rounds ayant déjà été créé (ici nb_rounds = 1)
        """
        nb_rounds = 1
        self.players_controller.players_manager.sort_players_by_score_and_ranking(
            self.players_controller.players_manager)
        self.players_controller.show_players(self.players_controller.players_manager)
        self.start_first_round()
        self.tournament_controller.round_controller.view.show_rounds_with_matches(
            self.tournament_controller.tournament, nb_rounds)
        return nb_rounds

    def close_round_and_display(self, nb_rounds):
        """Séquence menu 4.2
        Demande à l'utilisateur de saisir les scores et met à jour les scores totaux des joueurs.
        Affiche les joueurs.
        """
        results_round = self.tournament_controller.close_last_round_with_scores()
        self.tournament_controller.round_controller.view.show_rounds_with_matches(
            self.tournament_controller.tournament, nb_rounds)
        self.players_controller.players_manager.update_scores_players(results_round)
        self.players_controller.players_manager.sort_players_by_score_and_ranking(
            self.players_controller.players_manager)
        self.players_controller.show_players(self.players_controller.players_manager)
        return nb_rounds

    def start_next_round_and_display(self, nb_rounds):
        """Séquence menu 4.3
        Vérifie qu'il reste des rounds à jouer.
        S'il en reste trie les joueurs par score et classement ELO puis crée un nouveau
        round avec les matchs.
        Affiche le round créé.
                                
        Returns:
            nb_rounds (int) -- Nombre de rounds ayant déjà été créé
        """
        print(nb_rounds)
        if nb_rounds < self.tournament_controller.tournament.number_rounds:
            self.players_controller.players_manager.sort_players_by_score_and_ranking(
                self.players_controller.players_manager)
            self.players_controller.show_players(self.players_controller.players_manager)
            nb_rounds += 1
            self.new_round_with_control(nb_rounds)
            self.tournament_controller.round_controller.view.show_rounds_with_matches(
                self.tournament_controller.tournament, nb_rounds)
        else:
            self.tournament_controller.round_controller.view.max_rounds_alert()
        return nb_rounds

    def save_tournament(self):
        """Séquence menu 4.4
        Sauvegarde le tournoi courant dans le BDD.
        """
        self.tournament_controller.tournament_manager.save_tournaments_bdd(self.tournament_controller.tournament)
        
    def update_players_ranking_and_save(self):
        """Séquence menu 5.1
        Demande à l'uitilisateur de saisir les nouveaux classements ELO.
        Met à jour les classement ELO dans la BDD.
        """
        self.players_controller.update_ranking_players()
        
    def display_all_players_by_name(self):
        """Séquence menu 5.2.1
        Affiche tous les joueurs triés par nom.
        """
        all_players = self.players_controller.players_manager.load_all_players_from_bdd()
        self.players_controller.players_manager.sort_players_by_name(all_players)
        self.players_controller.show_players(all_players)
    
    def display_all_players_by_ranking(self):
        """Séquence menu 5.2.2
        Affiche tous les joueurs triés par classement ELO décroissant.
        """
        all_players = self.players_controller.players_manager.load_all_players_from_bdd()
        self.players_controller.players_manager.sort_players_by_ranking(all_players)
        self.players_controller.show_players(all_players)

    def display_players_by_name(self):
        """Séquence menu 5.3.1
        Affiche les joueurs du tournoi courant triés par nom.
        """
        self.players_controller.players_manager.sort_players_by_name(self.players_controller.players_manager)
        self.players_controller.show_players(self.players_controller.players_manager)
    
    def display_players_by_ranking(self):
        """Séquence menu 5.3.2
        Affiche les joueurs du tournoi courant triés par classement ELO décroissant.
        """
        self.players_controller.players_manager.sort_players_by_ranking(
            self.players_controller.players_manager)
        self.players_controller.show_players(self.players_controller.players_manager)
