from PyQt5.QtWidgets import QWidget, QVBoxLayout
from for_main_window.for_chart_tab.date_slider import DateSlider
from for_main_window.for_chart_tab.make_chart import MakeChart
import bisect


# klasa odpowiada za wyswietlany wykres w zakladce ChartTab oraz za suwaki zintegrowane z wykresem
class ChartPanel(QWidget):
    def __init__(self, all_files_data):
        super().__init__()
        self.__all_files_data = all_files_data
        self.__country_list = []
        self.__min_year = min(self.__all_files_data.get_all_years())
        self.__max_year = max(self.__all_files_data.get_all_years())
        self.__create_view()
        self.setFixedSize(1000, 800)

    # add_country i remove_country sa przekazywane do listy przyciskow panstw, tak aby po kliknieciu na nazwe
    # danego kraju wyswietlily sie dla niego wykresy
    def add_country(self, country):
        if country not in self.__country_list:
            bisect.insort(self.__country_list, country)
        self.__update_chart()

    def remove_country(self, country):
        if country in self.__country_list:
            self.__country_list.remove(country)
        self.__update_chart()

    # stworzenie widgetu z suwakiem i wykresem
    def __create_view(self):
        self.__date_slider = DateSlider(self.__min_year, self.__max_year, self.__update_chart)  # suwak dat
        # z przekazanym odwolaniem do funkcji aktualizujacej wyglad wykresu

        layout = QVBoxLayout()
        if len(self.__all_files_data.get_files_data()) >= 0:  # tworzy wykres tylko gdy sa jakies dane w all_files_data

            self.__chart = MakeChart(self.__all_files_data, self.__country_list, self.__min_year, self.__max_year)
            layout.addWidget(self.__chart)  # stworzenie wykresu dla przekazanej listy wszystkich danych, listy
            # panstw do wyswietlenia oraz maksymalnego i minimalnego roku

        layout.addWidget(self.__date_slider)

        layout.setStretch(0, 10)
        layout.setStretch(1, 1)
        self.setLayout(layout)

    # jakies testowe chyba
    def __update_chart2(self):
        print(self.__date_slider.get_val_from(), self.__date_slider.get_val_to())

    # aktualizowanie wyswietlanego wykresu na podstawie wartosci suwakow
    def __update_chart(self):
        min_year = self.__date_slider.get_val_from()
        max_year = self.__date_slider.get_val_to()
        country_list = self.__country_list

        self.__chart.update_plot(country_list, min_year, max_year)

