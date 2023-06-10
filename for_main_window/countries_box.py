from PyQt5.QtWidgets import QWidget, QVBoxLayout
from for_main_window.country_search import CountrySearch
from for_main_window.country_list import CountryList


# klasa odpowiadajaca za wyglad przewijanej listy z panstwami i pola do filtrowania panstw
class CountriesBox(QWidget):
    def __init__(self, country_list, add_function, remove_function):  # add_function i remove_function sluza do
        # polaczenia klikania przycisku na liscie ze zmiana tego co wyswietla sie na wykresie
        # odwolania do tych funkcji przekazuje potem do CountryList
        super().__init__()
        self.__country_list = country_list
        self.__add_function = add_function
        self.__remove_function = remove_function
        self.__init_view()
        self.__test_list = []

    def __init_view(self):
        layout = QVBoxLayout()

        # stworzenie listy przyciskow i wyszukiwarki
        self.__scrollable_list = CountryList(self.__country_list, self.__add_function, self.__remove_function)
        self.__search_box = CountrySearch(self.__scrollable_list.filter_buttons)

        layout.addWidget(self.__search_box)
        layout.addWidget(self.__scrollable_list)

        self.setLayout(layout)

    # jakies testowe funkcje to byly

    # def add_name(self, name):
    #     if name not in self.__test_list:
    #         self.__test_list.append(name)
    #
    # def remove_name(self, name):
    #     if name in self.__test_list:
    #         self.__test_list.remove(name)
