from PyQt5.QtWidgets import QWidget, QVBoxLayout
from for_main_window.country_search import CountrySearch
from for_main_window.country_list import CountryList


class CountriesBox(QWidget):
    def __init__(self, country_list):
        super().__init__()
        self.__country_list = country_list
        self.__init_view()

    def __init_view(self):
        layout = QVBoxLayout()

        self.__scrollable_list = CountryList(self.__country_list)
        self.__search_box = CountrySearch(self.__scrollable_list.filter_buttons)

        layout.addWidget(self.__search_box)
        layout.addWidget(self.__scrollable_list)

        self.setLayout(layout)
