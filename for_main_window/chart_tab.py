from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout

from for_main_window.for_chart.date_slider import DateSlider
from for_main_window.main_chart import MainChart
from for_main_window.files_adder import FilesAdder
from for_data_handling.all_files_data import AllFilesData
from for_main_window.countries_box import CountriesBox
from for_main_window.make_chart import MakeChart
from for_main_window.chart_panel import ChartPanel


class ChartTab(QWidget):
    def __init__(self):
        super().__init__()
        self.__all_files_data = AllFilesData()
        self.__layout = QGridLayout()
        self.__date_slider = None
        self.__file_path = None
        self.__countries_box = None
        self.__chart_view = None
        self.__chart_maker = MakeChart(self.__all_files_data)
        self.__chart_panel = None

        self.__set_start_elems()

    def __load_file(self, path):
        try:
            self.__all_files_data.add_file(path)
            print("added to all_files_data")
            self.__add_chart_panel(self.__layout)
            print("created chart_panel")
            # self.__add_chart(self.__layout)
            self.__add_countries_list_with_search(self.__layout)
            # self.__add_slider(self.__layout)

        except FileNotFoundError:
            print("File not found")
        finally:
            pass

    # funkcje dodajace elementy do layoutu
    def __add_file_path(self, layout):
        file_path = FilesAdder(self.__load_file)
        layout.addWidget(file_path, 4, 4, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

    def __add_countries_list_with_search(self, layout):
        countries = self.__all_files_data.get_all_countries()
        self.__countries_box = CountriesBox(countries, self.__chart_panel.add_country,
                                            self.__chart_panel.remove_country)
        if self.__countries_box is None:
            layout.addWidget(self.__countries_box, 0, 4, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        else:
            layout.removeWidget(self.__countries_box)
            layout.addWidget(self.__countries_box, 0, 4, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

    # ------------------------------------------------------------------------------------------------------
    # tego nie uzywam na razie

    def __add_slider(self, layout):
        max_val = max(self.__all_files_data.get_all_years())
        min_val = min(self.__all_files_data.get_all_years())
        if self.__date_slider is None:
            self.__date_slider = DateSlider(min_val, max_val, self.update_test)
            layout.addWidget(self.__date_slider, 7, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignVCenter)
        else:
            layout.removeWidget(self.__date_slider)
            self.__date_slider = DateSlider(min_val, max_val, self.update_test)
            layout.addWidget(self.__date_slider, 7, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignVCenter)

    def __add_chart(self, layout):
        self.__chart_maker = MakeChart(self.__all_files_data)
        if self.__chart_view is None:
            self.__chart_view = MainChart(self.__chart_maker)
            print("stworzono chart view")
            layout.addWidget(self.__chart_view, 0, 0, 4, 4, alignment=Qt.AlignmentFlag.AlignVCenter)

    # ------------------------------------------------------------------------------------------------------


    def __add_chart_panel(self, layout):
        if self.__chart_panel is None:
            self.__chart_panel = ChartPanel(self.__all_files_data)
            layout.addWidget(self.__chart_panel, 0, 0, 8, 4, alignment=Qt.AlignmentFlag.AlignVCenter)
        else:
            layout.removeWidget(self.__chart_panel)
            self.__chart_panel = ChartPanel(self.__all_files_data)
            layout.addWidget(self.__chart_panel, 0, 0, alignment=Qt.AlignmentFlag.AlignVCenter)

    def update_test(self):
        print(self.__date_slider.get_val_from(), self.__date_slider.get_val_to())

    def __set_start_elems(self):
        layout = self.__layout
        # adding elements to layout
        self.__add_file_path(layout)
        # self.__add_countries_list_with_search(layout)

        self.setLayout(layout)
