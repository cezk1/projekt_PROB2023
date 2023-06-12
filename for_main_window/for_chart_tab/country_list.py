from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QFormLayout, QGroupBox

from for_main_window.for_chart_tab.country_button import CountryButton

# country_list = ['Austria', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czechia', 'Denmark',
#                       'Estonia', 'Finland', 'France', 'Germany (until 1990 former territory of the FRG)', 'Greece',
#                       'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg',
#                       'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
#                       'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Türkiye', 'United Kingdom']


# klasa odpowiadajaca za liste z przyciskami panstw
class CountryList(QScrollArea):
    def __init__(self, country_list, add_function, remove_function):  # odwolania do funkcji add i remove przekazuje
        # potem do przyciskow
        super().__init__()
        self.__country_list = country_list  # lista nazw panstw
        self.__add_function = add_function
        self.__remove_function = remove_function
        self.__button_list = []  # lista przyciskow
        self.__init_list()

        #self.__remove_all_btns()

    def __init_list(self):
        self.__btn_layout = QFormLayout()
        self.__btn_group_box = QGroupBox()

        # dla kazdego kraju tworze przycisk z jego nazwa i dodaje do listy
        for country in self.__country_list:
            button_name = f"{country}"
            btn = CountryButton(button_name, self.__add_function, self.__remove_function)  # stworzenie przycisku
            self.__button_list.append(btn)  # dodanie go do listy przyciskow
            self.__btn_layout.addWidget(btn)  # dodanie go do layoutu listy

        self.__btn_group_box.setLayout(self.__btn_layout)
        self.setWidget(self.__btn_group_box)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)


    def __remove_all_btns(self):
        btn_num = self.__btn_layout.count()
        start_index = btn_num

        for index in range(start_index-1, -1,-1):
            self.__btn_layout.removeRow(index)

    # funkcja do filtrowania przyciskow na podstawie przekazanego tekstu
    def filter_buttons(self, text):
        for button in self.__button_list:
            if text.lower() in button.text().lower():
                button.setVisible(True)
            else:
                button.setVisible(False)
