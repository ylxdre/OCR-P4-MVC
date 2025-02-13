from datetime import datetime
from collections import UserList

DATAPATH = ("data/")
PLAYERFILE = DATAPATH + "liste_joueurs.json"
TOURNAMENTFILE = DATAPATH + "liste_tournois.json"


class Tournament:
    """Chess tournament with player_list, keeps a list with all rounds"""
    def __init__(self,
                 name="None",
                 players_list=None,
                 location="club",
                 total_round=4
                 ):
        self.name = name
        self.location = location
        self.start = datetime.now().strftime("%d-%m-%Y")
        self.end = self.start
        self.total_round = total_round
        self.round_list = []
        self.current_round = 0
        self.players_list = players_list
        self.scores = []
        self.description = "Pas de description"

    def __str__(self):
        return "Tournoi " + self.name + " à " + self.location

    def data(self):
        """Save tournament in file"""
        players = []
        for i in self.players_list:
            # players.append(i.name + " " + i.lastname)
            players.append(i.data())
        tournament_dict = {
            "name": self.name,
            "location": self.location,
            "description": self.location,
            "start": self.start,
            "end": self.end,
            "total_rounds": self.total_round,
            "current": self.current_round,
            "players": players,
            "rounds": self.round_list}
        return tournament_dict


class Player:
    """A Chess player"""
    def __init__(self, name, lastname, birthdate, ine):
        self.lastname = lastname
        self.name = name
        self.birthdate = birthdate
        self.ine = ine
        self.score = 0

    def __str__(self):
        """Used in print"""
        return self.ine

    def __repr__(self):
        return str(self)

    def data(self):
        player_dict = {
            'prénom': self.name,
            'nom': self.lastname,
            'date de naissance': self.birthdate,
            'ine': self.ine,
            'score': self.score
        }
        return player_dict


class Match:
    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def __str__(self):
        return self.player1.ine + " / " + self.player2.ine

    def get_data(self):
        return ([self.player1.ine, self.score1],
                [self.player2.ine, self.score2])

    def get_scores(self) -> list:
        return (self.player1.ine
                + " : " + str(self.score1)
                + " - " + self.player2.ine
                + " : " + str(self.score2))


class Round:

    def __init__(self, name="Round 1"):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.match_list = []

    def __str__(self):
        return (self.name
                + ": début le "
                + self.start_time
                + " et terminé le "
                + self.end_time)

    def get_time(self) -> str:
        return datetime.now().strftime("%d-%m-%Y à %Hh%M,%Ss")

    def save(self) -> dict:
        matches = []
        for match in self.match_list:
            matches.append(match.get_data())
        dico = {
            "Nom": self.name,
            "Debut": self.start_time,
            "Fin": self.end_time,
            "Matches": matches
        }
        return dico


class MatchHistory(UserList):
    """Keep a history of matches to avoid same match occur

    returns a list of matches
    """
    def __init__(self):
        self.matches = []

    def add(self, match_list):
        for match in match_list:
            self.matches.append(match)

    def __str__(self):
        return self.matches

    def check(self, given_match):
        for match in self.matches:
            if (given_match.player1 == match.player1
                    or given_match.player1 == match.player2):
                if (given_match.player2 == match.player2
                        or given_match.player2 == match.player2):
                    return True
            return False
