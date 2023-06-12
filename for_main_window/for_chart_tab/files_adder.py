from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from for_main_window.for_chart_tab.file_path import FilePath
from for_main_window.for_chart_tab.added_files_list import AddedFilesList
from for_main_window.for_chart_tab.choose_button import ChooseButton

import os


# miejsce do wczytywania plikow razem z lista wczytanych plikow
class FilesAdder(QWidget):
    def __init__(self, load_function):
        super().__init__()
        self.__load_function = load_function
        self.__showed_paths = []  # lista wyswietlanych w liscie sciezek do plikow
        self.__nr_of_paths = 0  # liczba wczytanych sciezek

        self.__init_view()

    def __init_view(self):
        layout = QVBoxLayout()

        self.__text_box = FilePath()  # stworzenie pola tekstowego, do ktorego mozna wpisac sciezke
        self.__files_list = AddedFilesList()  # stworzenie listy wszytanych sciezek
        self.__choose_button = ChooseButton(self.__chosen_from_explorer)  # stworzenie przycisku do otwierania
        # eksploratora plikow na komputerze
        self.__text_button = QPushButton("Load inserted path")  # przycisk do wczytania sciezki
        # wpisanej w polu tekstowym
        self.__text_button.clicked.connect(self.__button_clicked)

        # dodanie przycikow i listy do layoutu
        layout.addWidget(self.__files_list)
        layout.addWidget(self.__text_box)
        layout.addWidget(self.__choose_button)

        layout.addWidget(self.__text_button)

        self.setLayout(layout)

    # obsluga przerwan otwarcia eksploratora plikow
    def __chosen_from_explorer(self, path):
        text = os.path.basename(path)  # bierzemy tylko nazwe pliku (bez calej sciezki)
        if text not in self.__showed_paths and os.path.exists(text):  # wczytujemy plik tylko gdy nie ma go w liscie
            # (nie zostal juz wczesniej wczytany) i kiedy plik istnieje
            self.__nr_of_paths += 1
            self.__files_list.update_list(text, self.__nr_of_paths)  # zaaktualizowanie wyswietlanej listy plikow
            self.__load_function(text)  # wywolanie funkcji load_file z ChartTab
            self.__showed_paths.append(text)
            self.__text_box.clear()

    # obsluga przerwania przy klikaniu przycisku "Load inserted path"
    def __button_clicked(self):
        text = self.__text_box.text()
        if text not in self.__showed_paths and os.path.exists(text):  # wczytujemy plik tylko gdy nie ma go w liscie
            # (nie zostal juz wczesniej wczytany) i kiedy plik istnieje
            self.__nr_of_paths += 1
            self.__files_list.update_list(text, self.__nr_of_paths)  # zaaktualizowanie wyswietlanej listy plikow
            self.__load_function(text)  # wywolanie funkcji load_file z ChartTab
            self.__showed_paths.append(text)
            self.__text_box.clear()
