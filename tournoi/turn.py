from random import choice


class Turn():
    def __init__(self, name, matchs):
        self.name = name
        self.matchs = matchs
        self.match_history = []

    def rambling(self, player_list):
        """jumble (random order) players in list and return list"""
        self.tmp_list = []
        self.picked_player = []
        for i in range(2^len(player_list)):
            self.picked_player = choice(player_list)
            self.tmp_list.append(self.picked_player)
        return self.tmp_list


    def sorting(self, player_list):
        """order players on score : use second index (for every item in the list) as key (given by function score)"""
        def score(couple):
            return couple[1]
        return sorted(player_list, key=score)


    def associate(self, player_list):
        """create a match list"""
        self.match_list = []
        self.couple = ()
        for i in range(len(player_list)):
            if i % 2 == 0 :
                self.couple = (player_list[i][0], player_list[i+1][0])
                if self.couple in self.match_history:
                    self.couple = (player_list[i][0], player_list[i + 2][0])
                    self.match_list.append(self.couple)
                else:
                    self.match_list.append(self.couple)

        self.match_history.append(self.name)
        self.match_history.append(self.match_list)
        return self.match_list


    def matchmarking(self, player_list):
        pass

list = [['Player1', 8],
 ['Player2', 2],
 ['Player3', 0],
 ['Player4', 5],
 ['Player5', 8],
 ['Player6', 3],
 ['Player7', 1],
 ['Player8', 6],
 ['Player9', 3],
 ['Player10', 4],
 ['Player11', 3],
 ['Player12', 2],
 ['Player13', 8],
 ['Player14', 4],
 ['Player15', 2],
 ['Player16', 7]]

tour = Turn("tour1", 1)

print(tour.sorting(list))
print(tour.rambling(list))

print(tour.associate(tour.sorting(list)))

print(f"Voici l'historique des matchs : {tour.match_history}")

tour2 = Turn()