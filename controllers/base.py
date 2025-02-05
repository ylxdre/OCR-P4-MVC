from ChessTournament.models.models import Player, Tournament, Round, Match
from ChessTournament.views.menu import Menu
from random import shuffle


class Controller:
    def __init__(self):
        # loading models
        self.players_list = []
        self.score_list = []
        self.tournament = Tournament()
        self.round = Round()
        self.match = Match()

        # loading views
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
        return sorted(self.tournament.players_list, key=lambda t: t.score)

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

        for i in range(1, self.tournament.total_round):
            self.round.name = "Round " + str(i)
            self.tournament.current_round = self.round.name

            if i == 1:
            #    self.tournament.players_list = self.shuffle_players()
                print(self.tournament.players_list)
            else:
                self.tournament.players_list = self.sort_by_score()


        #pour chaque tour :
        # set le temps de début
        # créer les matchs
        # afficher les matchs
        # attendre la saisie des scores
        # ajouter le tour à la liste des tours du tournoi
            print(self.round.name)
            self.round.start_time = self.round.turn_time()
            self.round.match_list = self.create_match()
            #self.view.print_match_list()
            print(self.round.match_list)
            #self.view.prompt_for_scores()
            print("saisir les scores :")
            input("Round suivant ?")

    def create_match(self):
        """Create match with two consecutive players. Check if match already happened in round

        returns a round.match_list
        """
        j = 0
        k = 0
        for i in range(0, len(self.tournament.players_list), 2):
            j += 1
            self.match.name = "match" + str(j)
            print(self.match.name)
            self.match.player1 = self.tournament.players_list[i]
            self.match.player2 = self.tournament.players_list[i+1]
            print(self.match)
            if self.match in self.round.match_list:
                k += 1
                print(i, k)
                print(self.tournament.players_list[i])
                print(i + k)
                #print(self.tournament.players_list[i+k].ine)
                #self.match.player2 = self.tournament.players_list[i+k].ine
                self.round.match_list.append(self.match.get_data())
            else:
                self.round.match_list.append(self.match.get_data())

        return self.round.match_list


    def record_new_player(self):
        # get_player = {}
        print("Enregistrez un nouveau joueur :\n")
        # get_player['lastname'] = input('Nom de famille :\n')
        # get_player['name'] = input('Prénom :\n')
        #get_player['birth_date'] = input('Date de naissance :\n')

        self.lastname = input("Nom de famille ? : ")
        self.name = input("Prénom ? : ")
        self.birthdate = input("Date de naissance (jj/mm/aaaa) ? : ")
        #self.birthdate = self.check_date()
        self.ine = input("Identifiant National d'Echecs (ine) ? : ")
        #self.ine = self.test_ine()


        # convert dict in json object and write it in players.json file (with "a" append to file)
        # with open("players.json", "a") as output:
        #    output.write(json.dumps(get_player, indent=3))
        return {"Nom": self.lastname, "Prénom": self.name, "Date de naissance": self.birthdate, "INE": self.ine}


    def run(self):

        menu_choice = self.menu.items(1)
        if menu_choice == "4":
            print("Bye")
        elif menu_choice == "3":
            self.menu.items(2)
        elif menu_choice == "2":
            self.record_new_player()
        elif menu_choice == "1":
            print("c'est parti")
            self.create_tournament()
            self.run_tournament()








run = Controller()
run.run()

