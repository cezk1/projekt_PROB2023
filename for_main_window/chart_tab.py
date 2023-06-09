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
from for_main_window.countries_box import CountriesBox


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
            self.__add_countries_list_with_search(self.__layout)
            self.__add_slider(self.__layout)
        except FileNotFoundError:
            print("File not found")
        finally:
            pass

    # funkcje dodajace elementy do layoutu
    def __add_file_path(self, layout):
        file_path = FilesAdder(self.__load_file)

        # file_path = FilePath()
        layout.addWidget(file_path, 4, 4, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

    def __add_countries_list_with_search(self, layout):
        countries = self.__all_files_data.get_all_countries()

        countries_box = CountriesBox(countries)
        layout.addWidget(countries_box, 0, 4, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

    def __add_slider(self, layout):
        max_val = max(self.__all_files_data.get_all_years())
        min_val = min(self.__all_files_data.get_all_years())
        date_slider = DateSlider(min_val, max_val)
        layout.addWidget(date_slider, 7, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignVCenter)

    def __add_chart(self, layout):
        main_chart = MainChart(self.__all_files_data)
        layout.addWidget(main_chart, 0, 0, alignment=Qt.AlignmentFlag.AlignVCenter)

    def __set_layout_elems(self):
        layout = self.__layout
        # adding elements to layout
        self.__add_file_path(layout)
        self.__add_countries_list_with_search(layout)
        # self.__add_slider(layout)
        # self.__add_chart(layout)

        self.setLayout(layout)
