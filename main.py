from models.models import Tournament
from controllers.base import Application, Save
from views.base import View
from views.menu import Menu


def main():
    tournament = Tournament()
    save = Save()
    view = View()
    menu = Menu()
    application = Application(tournament=tournament,
                              save=save,
                              view=view,
                              menu=menu)
    # launch application
    application.menu_manager()


if __name__ == "__main__":
    main()
