from ..views.tournamentview import TournamentView
from ..models.tournament import Tournament
from ..controllers.roundcontroller import RoundController


class TournamentController:
    """
    Modélise le controller du tournoi.
    Assure le lien entre utilisateur et modèles en appelant la vue du tournoi
        pour la saisie d'un nouveau tournoi
    """

    def __init__(self):
        """
        """
        # self.players = PlayerManager()
        self.view = TournamentView()
        self.round_controller = RoundController()
        self.tournament = None

    def new_tournament(self):
        """Crée instance de Tournament avec saisie utilisateur des caractéristique du tournois,
        sauf attribut players
        L'attribut round se renseigne à l'instanciation à partir du nombre de rounds donné par l'utilisateur
        On instancie les rounds vides.
        """
        self.tournament = Tournament(self.view.prompt_name_tournament(),
                                     self.view.prompt_site_tournament(),
                                     self.view.prompt_date_begin_tournament(),
                                     self.view.prompt_date_end_tournament(),
                                     self.view.prompt_description_tournament(),
                                     self.view.prompt_time_control(),
                                     self.view.prompt_number_rounds())

    def close_last_round_with_scores(self):
        """Ferme le dernier round créé avec saisie des scores des matchs
        """
        index_last_round = len(self.tournament.rounds) - 1
        last_round_matches = self.tournament.rounds[index_last_round].matches
        score_round = {}
        for match in last_round_matches:
            winner = self.round_controller.view.prompt_score_match(match)
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
        self.tournament.rounds[index_last_round].close_round()
        return score_round
