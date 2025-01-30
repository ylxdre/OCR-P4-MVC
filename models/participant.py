from collections import UserDict
import json
from models.player import Player


class Participant(UserDict):
    """Dict of players and score attending a tournament

    takes tournament's name and list of object Player
    returns dict with player: score"""
    def __init__(self, player_list = None):
        #self.tournament
        self.player_list = player_list
        self.identifiant = ()
        self.data = {}
        self.PLAYERS_FILE = "./data/players/player_list.json"
        # initiate list


    def create_participant_from_list(self, players):
        for item in players:
            self.data[item.chess_id] = 0
        return self.data

    def get_list_from_file(self):
        with open(self.PLAYERS_FILE) as file:
            self.data = json.load(file)


    def get_players_from_file(self):
        """create a Player list from the json file

        uses file in current folder
        return a list of object Player
        """
        players = []
        data = {}
        with open(self.PLAYERS_FILE) as file:
            data = json.load(file)
        for i in data:
            players.append(
                Player(name=data[i][0], lastname=data[i][1], birthdate=data[i][2], gender=data[i][3], chess_id=i))
            # print(data[i][0])
            j = + 1
        return self.create_participant_from_list(players)

    def ask_for_new_participant(self):
        pass

