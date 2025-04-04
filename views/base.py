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
        input("Saisir les scores ? (y)")
        return True

    def prompt_next(self):
        print()
        input("?")
        return True

    def prompt_for_round(self, round):
        print()
        input(f"Prêt à lancer le {round.name} ? (y)")
        return True

    def prompt_for_new_player(self) -> dict:
        print("Enregistrez un nouveau joueur :\n")
        lastname = input("Nom de famille ? : ")
        name = input("Prénom ? : ")
        birthdate = input("Date de naissance (jj/mm/aaaa) ? : ")
        ine = input("Identifiant National d'Echecs (ine) ? : ")
        return {'name': name,
                'lastname': lastname,
                'birthdate':  birthdate,
                'ine':  ine}

    def prompt_for_tournament(self) -> dict:
        tournament_details = {}
        tournament_details['name'] = str.lower(input("Nom du tournoi ? : "))
        tournament_details['location'] = str.lower(input("Lieu du tournoi : "))
        tournament_details['date_start'] = (
            input("date de début (jj/mm/aaaa) : [today] "
                  or datetime.now().strftime("%d/%m/%Y")))
        tournament_details['date_end'] = (
            input("date de fin (jj/mm/aaaa) : [today] "
                  or datetime.now().strftime("%d/%m/%Y")))
        tournament_details['description'] = input("Description ? : ")
        total_round = input("Nombre de tours ? (4 par défaut) : ") or 4
        tournament_details['total_round'] = int(total_round)
        return tournament_details

    def prompt_tournament_to_display(self, tournament_list_to_display):
        i = 0
        temp_list = []
        for tournament in tournament_list_to_display:
            i += 1
            print(i, ".", tournament)
            temp_list.append(tournament)
        num = int(input("Numéro du tournoi à afficher ? "))
        return temp_list[num - 1]

    def input_scores(self, match, count):
        print("Scores pour le match", count, " :")
        while True:
            try:
                result = input(f"1.{match.player1}, "
                               f"2.{match.player2}, "
                               f"3.Nul\n")
                if result in ("1", "2", "3"):
                    return result
                else:
                    print("Entrez un chiffre entre 1 et 3")
            except ValueError:
                print("Veuillez entrer un chiffre")

    def display_matches(self, match_list):
        print("Liste des matchs : ")
        for match in match_list:
            print(match.player1.name, match.player1.lastname.upper(),
                  "contre", match.player2.name, match.player2.lastname.upper(),
                  "(", match, ")"
                  )

    def display_round_info(self, round):
        print("\n  -> ", round)

    def display_scores(self, players_list):
        print("\nLes scores sont :")
        print("-----------------")
        for i in players_list:
            print(i.ine, ':', i.name, i.lastname, i.score)

    def display_players(self, player_list_to_display):
        print("\nListe des joueurs :")
        for player in player_list_to_display:
            print(f"{player.name} {str.upper(player.lastname)} ({player.ine})")

    def display_tournaments(self, tournament_list_to_display):
        print("\nListe des tournois : ")
        for tournament in tournament_list_to_display:
            print("-", tournament,
                  "le",
                  tournament_list_to_display[tournament]['start'])

    def display_tournament_detail(self, tournament_to_display):
        i = tournament_to_display
        print("\n***************************************************")
        print("\nNom du tournoi : ", i['name'])
        print("Lieu : ", i['location'])
        print("Description : ", i['description'])
        print("Le tournoi a débuté le : ", i['start'])
        print("Et s'est terminé le : ", i['end'])
        print("\nLes participants étaient : ")
        for j in i['players']:
            print(j['ine'], "-", j['prénom'], str.upper(j['nom']))
        print("\nLes matches et leurs résultats étaient :")
        for j in i['rounds']:
            print(j['Nom'])
            print("Commencé à ", j['Debut'])
            print("Terminé à ", j['Fin'])
            print("Liste des matchs :")
            for k in j['Matches']:
                print(k)
            print()
        print("Les scores finaux :")
        for j in i['players']:
            print(j['prénom'], str.upper(j['nom']), ":", j['score'])
        print("\n***************************************************")

    def display_error(self):
        print("Erreur de saisie, recommencez;")

    def display_format_error(self):
        print("\n**** Erreur de format de fichier")

    def display_file_error(self, file):
        print(f"\n**** Pas de fichier {file} trouvé :/")

    def display_player_instructions(self):
        print("Placez un fichier joueur dans le répertoire data "
              "ou créez des nouveaux joueurs depuis le menu")
        print()

    def display_quit(self):
        print("Bye !")

    def display_error_already(self):
        print("Déjà joué")

    def ok_player(self):
        print("\nJoueur créé.")

    def ok_go(self):
        print("\n!!! C'est parti !!!\n")

    def ok_done(self, name):
        print(f"\nLe tournoi {name} est terminé !\n")
