from PyQt5.QtWidgets import QWidget, QVBoxLayout
from for_main_window.for_chart_tab.country_search import CountrySearch
from for_main_window.for_chart_tab.country_list import CountryList
from for_main_window.for_chart_tab.clear_list_button import ClearListButton
from for_main_window.for_chart_tab.save_pdf_button import SavePdfButton


# klasa odpowiadajaca za wyglad przewijanej listy z panstwami i pola do filtrowania panstw
class CountriesBox(QWidget):
    def __init__(self, country_list, add_function, remove_function, clear_function, img_getter, info_getter):
        # add_function i remove_function sluza do
        # polaczenia klikania przycisku na liscie ze zmiana tego co wyswietla sie na wykresie
        # odwolania do tych funkcji przekazuje potem do CountryList
        # clear_function czysci caly wykres
        super().__init__()
        self.__country_list = country_list
        self.__add_function = add_function
        self.__remove_function = remove_function
        self.__clear_function = clear_function
        self.__img_getter = img_getter
        self.__info_getter = info_getter

        self.__init_view()
        self.__test_list = []

    def __init_view(self):
        layout = QVBoxLayout()

        # stworzenie listy przyciskow i wyszukiwarki
        self.__scrollable_list = CountryList(self.__country_list, self.__add_function, self.__remove_function)
        self.__search_box = CountrySearch(self.__scrollable_list.filter_buttons)
        self.__clear_list_button = ClearListButton(self.__scrollable_list.clear_list, self.__clear_function)
        self.__save_pdf_button = SavePdfButton(self.__img_getter, self.__info_getter)

        layout.addWidget(self.__search_box)
        layout.addWidget(self.__scrollable_list)
        layout.addWidget(self.__clear_list_button)
        layout.addWidget(self.__save_pdf_button)

        self.setLayout(layout)

