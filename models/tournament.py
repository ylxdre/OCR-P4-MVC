from models.participant import Participant
from models.turn import Turn


class Tournament:
    """A competition with players and turns

    takes player_list
    """
    def __init__(self,
                 name,
                 participants,
                 location = "Club",
                 date_start = "today",
                 date_end = 'today',
                 current_turn = 1,
                 total_turn = 4 ):
        self.name = name
        self.participants = participants
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.total_turn = total_turn
        self.current_turn = current_turn
        self.description = "Pas encore de description"
        self.turn_list = []

    def run_turns(self):
        pass
        #if self.current_turn == "Round 1":

