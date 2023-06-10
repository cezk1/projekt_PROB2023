from PyQt5.QtWidgets import QWidget, QVBoxLayout
from for_main_window.country_search import CountrySearch
from for_main_window.country_list import CountryList


class CountriesBox(QWidget):
    def __init__(self, country_list, add_function, remove_function):
        super().__init__()
        self.__country_list = country_list
        self.__add_funtion = add_function
        self.__remove_function = remove_function
        self.__init_view()
        self.__test_list = []

    def __init_view(self):
        layout = QVBoxLayout()

        self.__scrollable_list = CountryList(self.__country_list, self.__add_funtion, self.__remove_function)
        self.__search_box = CountrySearch(self.__scrollable_list.filter_buttons)

        layout.addWidget(self.__search_box)
        layout.addWidget(self.__scrollable_list)

        self.setLayout(layout)

    def add_name(self, name):
        if name not in self.__test_list:
            self.__test_list.append(name)
        print(f"current names: {self.__test_list}")

    def remove_name(self, name):
        if name in self.__test_list:
            self.__test_list.remove(name)
        print(f"current names: {self.__test_list}")