import json
from datetime import datetime

class Player:
    """A chess player"""
    def __init__(self, name, lastname, birthdate, ine=None, score = 0):
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate
        self.ine = ine
        self.score = score

    def __str__(self):
        """Used in print"""
        return self.ine

    def __repr__(self):
        return str(self)


joueur1 = Player("Bob", "Durand", "25/12/1995", "EF34924")
joueur2 = Player("Joe", "Bidjoba", "02/01/2001", "QS42622")
joueur3 = Player("Jeanine", "Mequesurton", "25/12/1995", "AB20022")
joueur4 = Player("Jean-Pierre", "Quiroul", "15/09/1992", "JF78739")
joueur5 = Player("René", "Nuphard", "25/12/1995", "ED22230")
joueur6 = Player("Sophie", "Fonfec", "24/05/1999", "EE49948")


liste = [joueur1, joueur2, joueur3, joueur4, joueur5, joueur6]
print(joueur1)