from ..views.tournamentview import TournamentView
from ..models.tournament import Tournament
from ..models.tournamentmanager import TournamentManager
from ..controllers.roundcontroller import RoundController


class TournamentController:
    """
    Modélise le controller du tournoi.
    Assure le lien entre utilisateur et modèles en appelant la vue du tournoi
    pour la saisie d'un nouveau tournoi.
    Sert à créer une liste d'instances de tournois, afin de sauvegarder les tournois passés.

    Attributs:

        self.view (objet TournamentView)  -- instance de TournamentView destinée à la saisie
                                             et l'affichage des données propres aux tournois
        self.round_controller (objet RoundController) -- instance de RoundController.  Permet d'accéder aux données
                                                         de rounds depuis une instance de TournamentController
        self.tournaments  (list) -- liste d'instances de Tournament. Le tournoi courant est dans self.tournament[0].
                                    Peut acceuillir tous les tournois de la BDD dans une instance indépendante de
                                    TournamentController
        self.bdd_id  (list)  --  liste de id des tournois dans la BDD
        self.tournament_manager (objet TournamentManager)  -- Pour sauvegarde ou chargement d'un tournoi dans la BDD
    """

    def __init__(self):
        self.view = TournamentView()
        self.round_controller = RoundController()
        self.tournaments = []
        self.bdd_id = []
        self.tournament_manager = TournamentManager()

    def __str__(self):
        """Permet d'afficher la liste des tournois:

        Returns:
            string -- chaine de caractère contenant la liste de tous les tournois
        """
        liste_tournaments = ""
        for index in range(len(self.tournaments)):
            liste_tournaments += "tournoi " + str(index + 1) + ":\n" + str(self.tournaments[index]) + "\n"
        return liste_tournaments

    def add_tournament(self, tournament):
        """Ajoute le tournoi en argument au Tournament manager.
        Permet de préparer la sauvegarde du tournois en cours.

        Arguments:
            tournament {objet Tournament} -- Instance de Tournament contenant un tournoi en cours.
        """
        self.tournaments.append(tournament)

    def new_tournament(self):
        """Crée instance de Tournament avec saisie utilisateur des caractéristiques du tournois,
        sauf attribut players
        L'attribut round se renseigne à l'instanciation à partir du nombre de rounds donné par l'utilisateur
        On instancie les rounds vides.
        """
        self.tournaments = []
        self.tournaments.append(Tournament(self.view.prompt_name_tournament(),
                                           self.view.prompt_site_tournament(),
                                           self.view.prompt_date_begin_tournament(),
                                           self.view.prompt_date_end_tournament(),
                                           self.view.prompt_description_tournament(),
                                           self.view.prompt_time_control(),
                                           self.view.prompt_number_rounds()))

    def close_last_round_with_scores(self, players_controller):
        """Ferme le dernier round créé avec saisie des scores des matchs et met à jour les scores dans Match.
        Mémorise les scores de chaque joueur pour pouvoir mettre à jour ces scores dans Player.

        Returns:
            dict -- dictionnaire des scores de chaque joueur sous la forme {id_bdd: score}
        """

        index_last_round = len(self.tournaments[0].rounds) - 1
        last_round_matches = self.tournaments[0].rounds[index_last_round].matches
        score_round = {}
        for match in last_round_matches:
            name_player1 = players_controller[match.pairs[0][0]].full_name
            name_player2 = players_controller[match.pairs[1][0]].full_name
            winner = self.round_controller.view.prompt_score_match(match, name_player1, name_player2)
            if winner == "j" + str(match.pairs[0][0]):
                match.update_score(1, 0)
                score_round[match.pairs[0][0]] = 1
                score_round[match.pairs[1][0]] = 0
            if winner == 'j' + str(match.pairs[1][0]):
                match.update_score(0, 1)
                score_round[match.pairs[0][0]] = 0
                score_round[match.pairs[1][0]] = 1
            if winner == "=":
                match.update_score(0.5, 0.5)
                score_round[match.pairs[0][0]] = 0.5
                score_round[match.pairs[1][0]] = 0.5
        self.tournaments[0].rounds[index_last_round].close_round()
        return score_round

    def recover_couples_players_for_memorize(self):
        """Récupération des couples de joueurs ayant déjà joué ensemble, aprés chargement d'un tournoi depuis la BDD
        """
        for index in range(len(self.tournaments[0].rounds)):
            for match in self.tournaments[0].rounds[index].matches:
                self.round_controller.add_players_to_memo_match(match.pairs[0][0], match.pairs[1][0])
                self.round_controller.add_players_to_memo_match(match.pairs[1][0], match.pairs[0][0])
