from random import choice, shuffle
from models.participant import Participants
from models.match import Match

class Turn:
    """Round for tournament

    has name, dict of participant (object)
    """
    def __init__(self, participants, name="Round 1"):
        self.name = name
        self.participants = participants
        self.match_history = []
        self.match_list = []
        self.match_result = []
        self.player_list = []

    def ramble_player_list(self):
        """shuffle player's list"""
        return shuffle(self.player_list)

    def sort_players_by_score(self):
        """orders dict on value and returns sorted list"""
        return sorted(self.participants.items(), key=lambda t: t[1])

    def create_match(self):
        print("Liste des joueurs: ", self.player_list)
        j = 0
        k = 0
        for i in range(0, len(self.player_list), 2):
                j += 1
                match = Match(self.player_list[i][0], self.player_list[i+1][0])
                match.name = "match" + str(j)
                while match in self.match_history:
                    k += 1# If match has already been made, choose the next player
                    match = Match(self.player_list[i][0], self.player_list[i+k][0])
                    self.match_list.append(match)
                else:
                    self.match_list.append(match)
                #print(match)

        self.match_history.append([self.name, self.match_list])
        return self.match_list
        #   if i.index

    def input_scores(self):
        for match in self.match_list:
                print(match.name)
                self.result = input(f"Vainqueur du {match.name} : 1.{match.player1}, 2.{match.player2}, 3.nul\n ? ")
                if self.result == "1":
                    self.participants[match.player1] += 1
                    match.score1 += 1
                if self.result == "2":
                    self.participants[match.player2] += 1
                    match.score2 += 1
                if self.result == "3":
                    self.participants[match.player1] += 0.5
                    match.score1 += 0.5
                    self.participants[match.player2] += 0.5
                    match.score2 += 0.5
                match.update() # update match then save it at the end of the turn
                self.match_result.append(match.data)
        return self.match_result

