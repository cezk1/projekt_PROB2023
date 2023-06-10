from PyQt5.QtWidgets import QWidget, QVBoxLayout
from for_main_window.for_chart.date_slider import DateSlider
from for_main_window.make_chart import MakeChartV2
import bisect


class ChartPanel(QWidget):
    def __init__(self, all_files_data):
        super().__init__()
        self.__all_files_data = all_files_data
        self.__country_list = []
        self.__min_year = min(self.__all_files_data.get_all_years())
        self.__max_year = max(self.__all_files_data.get_all_years())
        self.__create_view()
        self.setFixedSize(1000, 800)

    def add_country(self, country):
        if country not in self.__country_list:
            bisect.insort(self.__country_list, country)
        self.__update_chart()
        print(self.__country_list)

    def remove_country(self, country):
        if country in self.__country_list:
            self.__country_list.remove(country)
        self.__update_chart()
        print(self.__country_list)

    def __create_view(self):
        self.__date_slider = DateSlider(self.__min_year, self.__max_year, self.__update_chart)

        layout = QVBoxLayout()
        if len(self.__all_files_data.get_files_data()) >= 0:
            self.__chart = MakeChartV2(self.__all_files_data, self.__country_list, self.__min_year, self.__max_year)
            layout.addWidget(self.__chart)

        layout.addWidget(self.__date_slider)
        print("added slider to layout")
        self.setLayout(layout)

    def __update_chart2(self):
        print(self.__date_slider.get_val_from(), self.__date_slider.get_val_to())

    def __update_chart(self):
        print("in update_chart")
        min_year = self.__date_slider.get_val_from()
        max_year = self.__date_slider.get_val_to()
        country_list = self.__country_list

        self.__chart.update_plot(country_list, min_year, max_year)

