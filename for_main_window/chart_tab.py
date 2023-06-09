from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout

from for_main_window.file_path import FilePath
from for_main_window.country_list import CountryList
from for_main_window.country_search import CountrySearch
from for_main_window.for_chart.date_slider import DateSlider
from for_main_window.main_chart import MainChart
from for_main_window.files_adder import FilesAdder
from for_data_handling.all_files_data import AllFilesData
from make_chart import MakeChart


class ChartTab(QWidget):
    def __init__(self):
        super().__init__()
        self.__all_files_data = AllFilesData()
        self.__layout = QGridLayout()
        self.__set_layout_elems()

    def __load_file(self, path):
        try:
            self.__all_files_data.add_file(path)
            # self.__add_chart(self.__layout)
        except FileNotFoundError:
            print("File not found")
        finally:
            pass

    # funkcje dodajace elementy do layoutu
    def __add_file_path(self, layout):
        file_path = FilesAdder(self.__load_file)

        # file_path = FilePath()
        layout.addWidget(file_path, 4, 4, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

    def __add_countries_list_with_search(self, layout):
        countries = ['Austria', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czechia', 'Denmark',
                              'Estonia', 'Finland', 'France', 'Germany (until 1990 former territory of the FRG)', 'Greece',
                              'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg',
                              'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
                              'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Türkiye', 'United Kingdom']

        countries = []

        country_list = CountryList(countries)
        country_search = CountrySearch(country_list.filter_buttons)
        layout.addWidget(country_list, 1, 4, 3, 2, alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(country_search, 0, 4, 3, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

    def __add_slider(self, layout):
        date_slider = DateSlider()
        layout.addWidget(date_slider, 4, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignVCenter)

    def __add_chart(self, layout):
        main_chart = MainChart(self.__all_files_data)
        layout.addWidget(main_chart, 0, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignVCenter)

    def __set_layout_elems(self):
        layout = self.__layout
        # adding elements to layout
        self.__add_file_path(layout)
        self.__add_countries_list_with_search(layout)
        self.__add_slider(layout)
        # self.__add_chart(layout)

        self.setLayout(layout)
