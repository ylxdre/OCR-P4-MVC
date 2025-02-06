from ChessTournament.models.models import Player, Tournament, Round, Match
from ChessTournament.views.menu import Menu
from ChessTournament.views.base import View

from random import shuffle


class Controller:
    def __init__(self):
        # loading models
        self.players_list = []
        self.score_list = []
        self.match = Match()
        self.tournament = Tournament()

        # loading views
        self.view = View()
        self.menu = Menu()

        # for test
        joueur1 = Player("Bob", "Durand", "25/12/1995", "EF34924")
        joueur2 = Player("Joe", "Bidjoba", "02/01/2001", "QS42622")
        joueur3 = Player("Jeanine", "Mequesurton", "25/12/1995", "AB20022")
        joueur4 = Player("Jean-Pierre", "Quiroul", "15/09/1992", "JF78739")
        joueur5 = Player("René", "Nuphard", "25/12/1995", "ED22230")
        joueur6 = Player("Sophie", "Fonfec", "24/05/1999", "EE49948")

        self.liste = [joueur1, joueur2, joueur3, joueur4, joueur5, joueur6]

    def sort_by_score(self):
        self.tournament.players_list.sort(key=lambda t: t.score, reverse = True)

    def shuffle_players(self):
        return shuffle(self.tournament.players_list)

    def create_tournament(self):
        print("Nouveau tournoi ! \n")
        self.tournament.name = input("Nom du tournoi ? : ")
        self.tournament.location = input("Lieu du tournoi : ")
        self.tournament.date_start = input("date de début (jj/mm/aaaa) : ")
        self.tournament.date_end = input("date de fin (jj/mm/aaaa) : ")
        self.tournament.description = input("Description ? : ")
        #self.tournament.players_list = input("Liste des joueurs : ")
        self.tournament.players_list = self.liste

        total_round = input("Nombre de tours ? (4 par défaut) : ") or 4
        if total_round != 4:
            self.tournament.total_round = int(total_round)


    def run_tournament(self):
        input("Prêt à lancer le premier round ?\n")
        #print("tour", self.tournament.current_round, round1.start_time)
        print("Liste des joueurs : ", self.tournament.players_list)
        shuffle(self.tournament.players_list)

        for i in range(1, self.tournament.total_round):
            self.round = Round()
            self.round.name = "Round " + str(i)
            self.tournament.current_round = self.round.name
        #pour chaque tour :
        # set le temps de début
        # créer les matchs
        # afficher les matchs
        # attendre la saisie des scores
        # ajouter le tour à la liste des tours du tournoi

            self.round.start_time = self.round.get_time()
            self.round.match_list = self.create_match()
            self.view.prompt_for_scores()
            self.round.end_time = self.round.get_time()
            self.view.input_scores(self.round.match_list)
            self.sort_by_score()
            self.view.display_round_info(self.round)
            self.view.display_scores(self.tournament.players_list)

        print("Le tournoi", self.tournament.name, "est terminé !")






    def create_match(self):
        """Create match with two consecutive players. Check if match already happened in round

        returns a round.match_list
        """
        j = 0
        k = 0
        print(self.tournament.players_list)
        for i in range(0, len(self.tournament.players_list), 2):
            j += 1
            match_name = "match" + str(j)
            match = Match()
            match.player1 = self.tournament.players_list[i]
            match.player2 = self.tournament.players_list[i+1]
            self.round.match_list.append(match)

        return self.round.match_list



    def run(self):
        menu_choice = self.menu.items(1)
        if menu_choice == "4":
            print("Bye")
        elif menu_choice == "3":
            self.menu.items(2)
        elif menu_choice == "2":
            self.view.prompt_for_new_player()
        elif menu_choice == "1":
            print("c'est parti")
            self.create_tournament()
            self.run_tournament()
            self.view.display_winner(self.tournament.players_list)
            self.view.display_scores(self.tournament.players_list)


run = Controller()
run.run()

