from datetime import datetime
import re

class View:
    """Prompt menu, get choices"""
    def __init__(self):
        pass

    def check_date(self):
        while True:
            date = input("Date de naissance (jj/mm/aaaa) ? : ")
            if datetime.strptime(date, '%d/%m/%Y'):
                break
            else:
                print("La date doit être au format jj/mm/aaaa")

    def test_ine(self):
        ine_pattern = r'[a-zA-Z]{2}\d{5}'
        while True:
            ine = input("Identifiant National d'Echecs (ine) ? : ")
            if re.match(ine_pattern, ine):
                break
            else:
                print("Mauvais format d'ine")

    def prompt_for_scores(self):
        print()
        input("Saisir les scores ?")
        return True

    def display_round_info(self, round):
        print(round)

    def display_scores(self, players_list):
        print("Les scores sont :\n")
        for i in players_list:
            print(i.ine, i.name, i.lastname, " : ", i.score)

    def prompt_for_new_player(self):
        print("Enregistrez un nouveau joueur :\n")
        self.lastname = input("Nom de famille ? : ")
        self.name = input("Prénom ? : ")
        self.birthdate = input("Date de naissance (jj/mm/aaaa) ? : ")
        #self.birthdate = self.check_date()
        self.ine = input("Identifiant National d'Echecs (ine) ? : ")
        #self.ine = self.test_ine()
        return {"Nom": self.lastname, "Prénom": self.name, "Date de naissance": self.birthdate, "INE": self.ine}

    def input_scores(self, match_list):
        for match in match_list:
            print(match)
            print("Scores pour match", match_list.index(match) + 1, " :")
            while True:
                try:
                    result = input(f"1.{match.player1}, 2.{match.player2}, 3.Nul\n")
                    if result in ("1", "2", "3"):
                        if result == "1":
                            match.player1.score += 1
                        elif result == "2":
                            match.player2.score += 1
                        elif result == "3":
                            match.player1.score += 0.5
                            match.player2.score += 0.5
                        break
                    else:
                        print("Entrez un chiffre entre 1 et 3")
                except ValueError:
                    print("Veuillez entrer un chiffre")

    def display_winner(self, player_list):
        winner = max(player_list, key=lambda t: t.score)
        print("Le gagnant est :", winner.name, winner.lastname, "avec un score de :", winner.score)










