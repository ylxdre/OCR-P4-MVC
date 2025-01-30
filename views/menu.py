
class Menu:
    def __init__(self):
        self.ITEMS = [
            "[1] Créer un nouveau tournoi",
            "[2] Enregistrer un nouveau joueur",
            "[3] Rapports",
            "[4] Quitter"
        ]
        self.RAPPORTS = [
            "[1] Afficher la liste des joueurs",
            "[2] Afficher l'historique des tournois",
            "[3] Afficher le détail d'un tournoi",
            "[4] Quitter"
        ]

    def items(self, value):
        menu_type = []
        if value == 1:
            menu_type = self.ITEMS
        if value == 2:
            menu_type = self.RAPPORTS

        for i in menu_type:
            print(i)
        try:
            demande = input("Choix ? : ")
            if demande not in range(1, len(menu_type)):
                demande = input("Choix ? : ")
        except ValueError:
            print("Veuillez saisir un chiffre")
            demande = input("Choix ? : ")
        return demande
