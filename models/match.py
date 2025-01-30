from models.player import Player

class Match:
    """Get two players

    print a string with both ids
    return a tuple of list player, score
    """
    def __init__(self, player1, player2):
        self.name = None
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.data = ([self.player1, self.score1], [self.player2, self.score2])

    def __str__(self):
        return f"[{self.player1}, {self.player2}]" #pretty print for prompt

    def __repr__(self):
        #return ([self.player1, self.score1], [self.player2, self.score2])
        return str(self)

    def update(self):
        """Update tuple when attributs have change"""
        self.data = ([self.player1, self.score1], [self.player2, self.score2])
        return self.data
