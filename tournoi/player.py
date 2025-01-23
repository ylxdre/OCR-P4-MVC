import json

class Player:
    """Define player, should store only data for now ? Don't see further"""

    def get_new_player(self):
        get_player = {}
        print("Enregistrez un nouveau joueur :\n")
        get_player['lastname'] = input('Nom de famille :\n')
        get_player['name'] = input('Prénom :\n')
        get_player['birth_date'] = input('Date de naissance :\n')

    #convert dict in json object and write it in players.json file (with "a" append to file)
        with open("players.json", "a") as output:
            output.write(json.dumps(get_player, indent=3))


new = Player()
new.get_new_player()
