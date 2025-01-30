import json
from datetime import datetime

class Player:
    """Player from the club"""
    def __init__(self, name, lastname, birthdate, gender, chess_id=None):
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate
        self.gender = gender
        self.chess_id = chess_id

    def __str__(self):
        """Used in print"""
#        return f"{self.name} {self.lastname}, né le {self.birthdate}, genre: {self.gender}"
        return self.chess_id

    def __repr__(self):
        return str(self)

