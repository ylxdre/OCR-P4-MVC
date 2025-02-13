from models.models import (Player, Round, Match,
                                           MatchHistory)
from models.models import DATAPATH, PLAYERFILE, TOURNAMENTFILE


from random import shuffle
import os
import json


class Save:
    def __init__(self):
        pass

    def load_file(self, file):
        try:
            os.mkdir(DATAPATH)
        except FileExistsError:
            pass
            # test if file exists... could be done more gracefully
        try:
            with open(file, "r") as json_file:
                data_tmp = json.load(json_file)
            return data_tmp

        except json.decoder.JSONDecodeError:
            print("Erreur de format sur le fichier")
        except FileNotFoundError:
            return False

    def write_file(self, data_tmp, file):
        with open(file, "w") as json_file:
            json_file.write(json.dumps(data_tmp))
        return "Done."

    def player_write(self, player) -> bool:
        data_tmp = []
        if self.load_file(PLAYERFILE):
            data_tmp = (self.load_file(PLAYERFILE))
        data_tmp.append(player)
        self.write_file(data_tmp, PLAYERFILE)
        print("Joueur créé !")
        return True

    def player_load(self) -> list:
        """Load and create player from JSON file
        returns:
        list of Player"""
        if self.load_file(PLAYERFILE):
            data_tmp = self.load_file(PLAYERFILE)
            data_list = []
            for player in data_tmp:
                data_list.append(Player(name=player['name'],
                                        lastname=player['lastname'],
                                        birthdate=player['birthdate'],
                                        ine=player['ine']))

            return data_list
        else:
            print("\n**** Pas de fichier joueur trouvé :/\n")

    def tournament_write(self, tournament):
        data = {
            tournament.name: tournament.data()
        }
        print(data)

        if self.load_file(TOURNAMENTFILE):
            data_tmp = self.load_file(TOURNAMENTFILE)
            data_tmp[tournament.name] = tournament.data()
            self.write_file(data_tmp, TOURNAMENTFILE)
        else:
            self.write_file(data, TOURNAMENTFILE)
        return True

    def tournament_load(self):
        if self.load_file(TOURNAMENTFILE):
            data_tmp = self.load_file(TOURNAMENTFILE)
            return data_tmp
        else:
            print("\n**** Pas de fichier tournoi trouvé :/ \n")


class Application:
    def __init__(self, tournament, save, view, menu):
        self.tournament = tournament
        self.save = save
        self.match = Match()
        self.match_history = MatchHistory()
        self.view = view
        self.menu = menu

    def sort_by_score(self):
        self.tournament.players_list.sort(key=lambda t: t.score, reverse=True)

    def shuffle_players(self):
        return shuffle(self.tournament.players_list)

    def create_tournament(self):
        print("Nouveau tournoi ! \n")
        tournament_details = self.view.prompt_for_tournament()
        self.tournament.name = tournament_details['name']
        self.tournament.location = tournament_details['location']
        self.tournament.date_start = tournament_details['date_start']
        self.tournament.date_end = tournament_details['date_end']
        self.tournament.description = tournament_details['description']
        self.tournament.total_round = tournament_details['total_round']
        if self.save.player_load():
            self.tournament.players_list = self.save.player_load()
            self.save.tournament_write(self.tournament)
        else:
            self.view.display_player_instructions()
            self.menu_manager()

    def run_tournament(self):
        shuffle(self.tournament.players_list)
        for each_round in range(1, self.tournament.total_round + 1):
            self.tournament.current_round += 1
            self.round = Round()
            self.round.name = "Round " + str(each_round)
            self.view.prompt_for_round(self.round)
            # set round start time
            self.round.start_time = self.round.get_time()
            # create matches TODO : check from history
            self.round.match_list = self.create_match()
            # display matches
            self.view.display_matches(self.round.match_list)
            self.view.prompt_for_scores()
            self.round.end_time = self.round.get_time()
            self.scores(self.round.match_list)
            self.sort_by_score()
            self.tournament.round_list.append(self.round.save())
            print("après maj", self.tournament.round_list)
            self.save.tournament_write(self.tournament)
            self.view.display_round_info(self.round)
            self.view.display_scores(self.tournament.players_list)

        print("\nLe tournoi", self.tournament.name, "est terminé !\n")

    def get_match_info(self, match_list):
        matches = []
        for i in match_list:
            matches.append(i.get_data())
        return matches

    def check_match(self, match, match_history):
        for item in match_history:
            if match in item:
                return True
            else:
                return False

    def create_match(self) -> list:
        """Create match with two consecutive players

        returns :
        list of Match
        """
        match_list = []
        j = 0
        for i in range(0, len(self.tournament.players_list), 2):
            j += 1
            match = Match()
            match.player1 = self.tournament.players_list[i]
            match.player2 = self.tournament.players_list[i+1]
            match_list.append(match)
        return match_list

    def scores(self, match_list) -> list:
        """user asked to enter scores, update Player
        returns:
        list of tuples
        """
        matches = []
        for match in match_list:
            count = match_list.index(match) + 1
            result = self.view.input_scores(match, count)
            if result in ("1", "2", "3"):
                if result == "1":
                    match.player1.score += 1
                    match.score1 = 1
                elif result == "2":
                    match.player2.score += 1
                    match.score2 = 1
                elif result == "3":
                    match.player1.score += 0.5
                    match.player2.score += 0.5
                    match.score1 = match.score2 = 0.5
            matches.append(match.get_data())
        return matches

    def menu_manager(self):
        menu_choice = self.menu.items(1)
        while True:
            # Quit
            if menu_choice == "4":
                print("Bye")
                break
            # Rapports
            elif menu_choice == "3":
                rapport_choice = self.menu.items(2)

                # Go back
                if rapport_choice == "4":
                    self.menu_manager()

                # Display players from file
                elif rapport_choice == "1":
                    if self.save.player_load():
                        self.view.display_players(self.save.player_load())
                    input("?")

                # Display list of tournaments
                elif rapport_choice == "2":
                    if self.save.tournament_load():
                        self.view.display_tournaments(
                            self.save.tournament_load())
                    input("?")

                # display tournament's details
                elif rapport_choice == "3":
                    temp = {}
                    if self.save.tournament_load():
                        temp = self.save.tournament_load()
                        name = self.view.prompt_tournament_to_display(temp)
                        if name in temp:
                            self.view.display_tournament_detail(
                                temp[name])
                        else:
                            self.view.display_error()

            # create new player and save it in file
            elif menu_choice == "2":
                joueur = self.view.prompt_for_new_player()
                self.save.player_write(joueur)
                input("Retour ?")
                self.menu_manager()

            # create new tournament
            elif menu_choice == "1":
                print("c'est parti")
                self.create_tournament()
                self.run_tournament()
                self.view.display_winner(self.tournament.players_list)
                self.view.display_scores(self.tournament.players_list)
                self.menu_manager()
