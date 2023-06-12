from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5 import sip

from for_main_window.for_chart.date_slider import DateSlider
from for_main_window.main_chart import MainChart
from for_main_window.files_adder import FilesAdder
from for_data_handling.all_files_data import AllFilesData
from for_main_window.countries_box import CountriesBox
from for_main_window.make_chart import MakeChart
from for_main_window.chart_panel import ChartPanel
from for_main_window.map_tab import MapTab


# widget odpowiadajacy za wyglad calej zakladki zwiazanej z wykresem
class ChartTab(QWidget):
    def __init__(self, map_tab: MapTab):
        super().__init__()
        self.__all_files_data = AllFilesData()  # stworzenie obiektu AllFilesData do przetwarzania danych wejsciowych
        self.__layout = QGridLayout()  # ustawienie layoutu zakladki z wykresem na siatke
        # ponizej tworze zmienne do ktorych beda przypisywane konkretne elementy layoutu
        self.__date_slider = None
        self.__file_path = None
        self.__countries_box = None
        self.__chart_view = None
        # self.__chart_maker = MakeChart(self.__all_files_data)
        self.__chart_panel = None

        self.__set_start_elems()  # ustawienie startowego wygladu zakladki, tylko do wczytania pliku
        # (nie wyswietla sie wykres)

    # load_file jest wywolywana za kazdym razem gdy uzytkownik doda sciezke do pliku
    def __load_file(self, path):
        try:
            self.__all_files_data.add_file(path)  # dodanie sciezki do obiektu AllFilesData
            # obslugujacego wszystkie pliki

            # self.__map_tab.dodaj_mape_do_layoutu(path)
            print("added to all_files_data")

            self.__add_chart_panel(self.__layout)  # dodanie do layoutu zakladki (wyswietlenie) wykresu z suwakami
            print("created chart_panel")

            # self.__map_tab.make_map(path)

            # self.__add_chart(self.__layout)
            self.__add_countries_list_with_search(self.__layout)  # dodanie do layoutu (wyswietlenie)
            # wyszukiwarki panstw

            # self.__add_slider(self.__layout)
            # funkcja ktora uruchamia maptab
            # tutaj zrobic jakies odwolanie do map

        except FileNotFoundError:
            print("File not found")
        finally:
            pass

    # funkcje dodajace elementy do layoutu

    # add_file_path dodaje do layoutu miejsce, w ktorym uzytkownik moze wprowadzic sciezke i dodac pliki
    def __add_file_path(self, layout):
        files_adder = FilesAdder(self.__load_file)  # do FilesAdder trzeba przekazac funkcje load_file, zeby polaczyc
        # klikanie przycisku w FilesAdder ze stworzeniem wykresu
        layout.addWidget(files_adder, 4, 4, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

    # add_countries_list_with_search dodaje do layoutu przewijana liste panstw i filtrowanie listy
    def __add_countries_list_with_search(self, layout):
        countries = self.__all_files_data.get_all_countries()  # bierzemy nazwy wszystkich panstw

        if self.__countries_box is None:
            self.__countries_box = CountriesBox(countries, self.__chart_panel.add_country,
                                                self.__chart_panel.remove_country)
            # odwolania do funkcji chart_panel.add_country i chart_panel.add_country pozwalaja na polaczenie
            # listy i przyciskow na liscie krajow z wykresem
            layout.addWidget(self.__countries_box, 0, 4, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        else:
            # jesli countries_box byl juz wczesniej zrobiony to usuwamy istniejacy i dodajemy do layoutu nowy
            # z aktualnymi informacjami
            layout.removeWidget(self.__countries_box)
            sip.delete(self.__countries_box)
            self.__countries_box = None
            self.__countries_box = CountriesBox(countries, self.__chart_panel.add_country,
                                                self.__chart_panel.remove_country)
            layout.addWidget(self.__countries_box, 0, 4, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)




    # ------------------------------------------------------------------------------------------------------
    # tego ponizej nie uzywam na razie ale nie usuwam bo moze sie przyda
    # jak sie okaze ze wszystko dziala to mozna usunac od tego momentu...

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

    # ...do tego momentu
    # ------------------------------------------------------------------------------------------------------




    # add_chart_panel dodaje do layoutu wykres z suwakami
    def __add_chart_panel(self, layout):
        if self.__chart_panel is None:
            self.__chart_panel = ChartPanel(self.__all_files_data)  # stworzenie obiektu ChartPanel
            layout.addWidget(self.__chart_panel, 0, 0, 8, 4, alignment=Qt.AlignmentFlag.AlignVCenter)
        else:
            # tak samo jak z lista panstw, najpierw trzeba usunac istniejacy juz chart_panel
            layout.removeWidget(self.__chart_panel)
            sip.delete(self.__chart_panel)
            self.__chart_panel = None
            self.__chart_panel = ChartPanel(self.__all_files_data)
            layout.addWidget(self.__chart_panel, 0, 0, alignment=Qt.AlignmentFlag.AlignVCenter)

    # ta funkcja chyba tylko do jakiegos testu przewijania byla potrzebna
    def update_test(self):
        print(self.__date_slider.get_val_from(), self.__date_slider.get_val_to())

    # set_start_elems ustawia startowe elementy layoutu, czyli mozliwosc dodania pliku
    def __set_start_elems(self):
        layout = self.__layout
        # adding elements to layout
        self.__add_file_path(layout)
        # self.__add_countries_list_with_search(layout)

        self.setLayout(layout)
