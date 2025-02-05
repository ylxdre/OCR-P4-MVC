from datetime import datetime
import re

class View:
    """Prompt menu, get choices"""
    def __init__(self):
        pass

    def prompt_for_scores(self):
        print()
        input("Saisir les scores ?")
        return True

    def display_winner(self, participants):
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

