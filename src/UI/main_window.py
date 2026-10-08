
class MainWindow:
    def __init__(self):
        pass

    def display_menu(self):
        print("*" * 50)
        print("1. Харчування\n"
              "2. Введення бюджету\n"
              "0. Вийти")
        print("*" * 50)
        return input("Введіть дію: ")