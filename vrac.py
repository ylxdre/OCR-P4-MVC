from models.participant import Participant
from models.player import Player
from models.match import Match
from models.turn import Turn
from models.tournament import Tournament
from views.base import View

from random import randint
import json



# generate player list
def generate_liste():
    liste = []
    for i in range(16):
        liste.append(["Player"+str(i+1), randint(0, 8)])
    return liste

def create_player_list_file(player_list):
    """create a JSON file using a Player list

    takes a list of object Player
    returns nothing but write file"""
    player_dict = {}
    for i in player_list:
        player_dict[i.chess_id] = [i.name, i.lastname, i.birthdate, i.gender]
#    print(player_dict)
    with open("player_list.json", "a") as file:
        json.dump(player_dict, file)
    print("done.")

def get_list_from_file():
    """create a Player list from the json file

    uses file in current folder
    return a list of object Player
    """
    players = []
    data = {}
    with open("player_list.json") as file:
        data = json.load(file)
    for i in data:
        players.append(Player(name = data[i][0], lastname = data[i][1], birthdate = data[i][2], gender = data[i][3], chess_id = i))
        #print(data[i][0])
        j =+ 1
    return players
#        joueur'data.index[i]' = Player(name = i)

def chess_id_from_name(name, player_list):
    for i in player_list:
        if str(name) == str(i.name + " " + i.lastname):
            return i.chess_id
    return None

def name_from_chess_id(chess_id, player_list):
    for i in player_list:
        if str(chess_id) == str(i.chess_id):
            return str(i.name + " " + i.lastname)
    return None


joueur1 = Player("Bob", "Durand", "25/12/1995", "M", "EF34924")
joueur2 = Player("Joe", "Bidjoba", "02/01/2001", "M", "QS42622")
joueur3 = Player("Jeanine", "Mequesurton", "25/12/1995", "F", "AB20022")
joueur4 = Player("Jean-Pierre", "Quiroul", "15/09/1992", "M", "JF78739")
joueur5 = Player("René", "Nuphard", "25/12/1995", "M", "ED22230")
joueur6 = Player("Sophie", "Fonfec", "24/05/1999", "F", "EE49948")

player_list = [joueur1, joueur2, joueur3, joueur4, joueur5, joueur6]

#create_player_list_file(player_list)
#print("la player_list from file : ", get_list_from_file())
#print("La player_list crée dans le script : ", player_list)

# print(liste_from_file)
#print(chess_id_from_name("Joe Bidjoba", player_list))
#print(name_from_chess_id("JF78739", player_list))
def test2(player_list):
    # create new participants object  (dict from list)...
    participants = Participant("Tournoi de cajou", player_list)
    # display the dict
    print("print(participants) : ", participants.create_participant_from_list())
    print(participants.data)
    tour1 = Turn(participants.data)
    print(tour1.create_match())

    tour1.input_scores()

    print(participants)

def test(player_list):

    participants = Participant("Tournoi de cajou", player_list)

    print("print(participants) : ", participants.create_participant_from_list())
    print("Le score de ('Joe', 'Bidjoba') : ", participants.get((chess_id_from_name("Joe Bidjoba", player_list))))

    match = Match(joueur1, joueur3)
    print("print(match): ", match)


    match.score2=1
    print("print(match), après match.score2=1: ", match)


    turn1 = Turn(participants, "Round 1")
    turn1.create_player_list()
    print("turn1.player_list : ",turn1.player_list)
    turn1.ramble_player_list()
    turn1.create_matches()
    print("turn1.match_list : ", turn1.match_list )

    turn1.input_scores()

    print("print(participants) : ", participants)

def test3():
    # initialization
    participants = Participant()
    participants.get_players_from_file() #load dict from file
    view = View()
    tour = Turn(participants)
    tournoi1 = Tournament("Tournoi de Cajou", participants)
    

    def run_turn(turn_nb):
        tour = Turn(participants.data, name = "Round"+str(turn_nb))
        tour.create_match()
        print(f"La liste des matchs pour le {tour.name} est :\n {tour.match_list}")
        view.prompt_for_scores()
        tour.input_scores()
        print("Save \n", tour.name, tour.match_result)
        tournoi1.turn_list.append([tour.name, tour.match_result])

    while i < tournoi1.total_turn:
        if tounoi1.current_turn == 1:


    run_turn(turn_nb)

    #for i in range(1, tournoi1.total_turn+1):
        #tour = Turn(participants, name = "Round"+str(i))
        #tour.





test3()