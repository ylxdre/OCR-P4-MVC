from models.tournament import Tournament
from models.player import Player
from models.turn import Turn
from models.match import Match
from views.menu import Menu

class Controller:
    def __init__(self):
        # loading models
        self.players_list: List[Player] = []
        self.score_list = []



        # loading views
        self.view = Menu()

        #self.tournament = Tournament(name = "Tournoi de Cajou", )
        #self.turn = Turn()
    def prompt_menu(self):
        pass

    def record_new_player(self):
        # get_player = {}
        print("Enregistrez un nouveau joueur :\n")
        # get_player['lastname'] = input('Nom de famille :\n')
        # get_player['name'] = input('Prénom :\n')
        #get_player['birth_date'] = input('Date de naissance :\n')

        self.lastname = input("Nom de famille ? :\n")
        self.name = input("Prénom ? :\n")

        def input_date(date):
            """Keep asking until date format is valid"""
            try:
                datetime.strptime(date, '%d/%m/%Y')
                return date
            except ValueError:
                print("La date doit être au format jj/mm/aaaa")
            new_date = input()
            input_date(new_date)
            return new_date

        self.birthdate = input_date(input("Date de naissance (jj/mm/aaaa) ?:\n"))

        while self.gender not in ("M", "F", "N"):
            self.gender = input("Sexe (M/F/N) ?:\n")

        # convert dict in json object and write it in players.json file (with "a" append to file)
        # with open("players.json", "a") as output:
        #    output.write(json.dumps(get_player, indent=3))

        return {"Nom": self.lastname, "Prénom": self.name, "Date de naissance": self.birthdate, "Genre": self.gender}

    def run(self):

        menu_choice = self.view.items(1)
        if menu_choice == 3:
            self.view.items(2)


