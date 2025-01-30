from controllers.base import Controller
from views.base import View


def main():
    view = View()
    menu = Controller(view)
    menu.run()


if __name__ == "__main__" :
    main()





