from datetime import datetime

class Tournament:
    """Chess tournament with player_list, keeps a list with all rounds"""
    def __init__(self, name = None, players_list = None, location = "club", total_round = 4):
        self.name = name
        self.location = location
        self.start = "start"
        self.end = "end"
        self.total_round = total_round
        self.round_list = []
        self.current_round = 1
        self.players_list = players_list
        self.description = "Pas de description"


class Player:
    """A Chess player"""
    def __init__(self, name, lastname, birth_date, ine):
        self.lastname = lastname
        self.name = name
        self.birth_date = birth_date
        self.ine = ine
        self.score = 0

    def __str__(self):
        """Used in print"""
        return self.ine

    def __repr__(self):
        return str(self)


class Match:
    def __init__(self, player1 = None, player2 = None):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def __str__(self):
        return self.player1.name + " " + self.player1.lastname + " / " + self.player2.name + " " + self.player2.lastname

    def __repr__(self):
        return str(self)


    def create(self):
        pass

    def get_data(self):
        return ([self.player1.ine, self.player1.score], [self.player2.ine, self.player2.score])


class Round:
    def __init__(self, name = "Round 1"):
        self.name = name
        self.match_list = []
        self.start_time = None
        self.end_time = None

    def turn_time(self):
        return datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    def create_match2(self):
        pass

    def start(self):
        self.start_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    def stop(self):
        self.end_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

