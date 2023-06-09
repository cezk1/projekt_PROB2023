from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from for_main_window.file_path import FilePath
from for_main_window.added_files_list import AddedFilesList

import os


# miejsce do wczytywania plikow
class FilesAdder(QWidget):
    def __init__(self, load_function):
        super().__init__()
        self.__load_function = load_function
        self.__showed_paths = []
        self.__init_view()

    def __init_view(self):
        layout = QVBoxLayout()

        self.__text_box = FilePath()
        self.__files_list = AddedFilesList()
        self.__add_button = QPushButton("Load")
        self.__add_button.clicked.connect(self.__button_clicked)

        layout.addWidget(self.__files_list)
        layout.addWidget(self.__text_box)
        layout.addWidget(self.__add_button)

        self.setLayout(layout)

    def __button_clicked(self):
        text = self.__text_box.text()
        if text not in self.__showed_paths and os.path.exists(text):
            self.__files_list.update_list(text)
            self.__load_function(text)
            self.__showed_paths.append(text)
            print(text)
