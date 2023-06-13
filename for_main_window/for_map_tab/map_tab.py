from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from for_main_window.for_map_tab.map_generator_v1 import CreateMap


class MapTab(QWidget):
    def __init__(self):
        super().__init__()

        self.__init_view()

    def __init_view(self):
        layout = QVBoxLayout()
        label = QLabel("TODO: mapa z geopandas z klikaniem")

        layout.addWidget(label)

        self.setLayout(layout)

    def dodaj_mape_do_layoutu(self, path):
        # zrobic instancje make_file_data
        # przekazac do tej instancji "path"
        # wywolac funkcje do robienia dataframu z make_file_data
        # na postawie dataframu stworzyc widget mapy z kilkaniem i wszystkim innym
        # dodac mape do layoutu MapTab
        pass

    def make_map(self, all_files_data):
        # stworzenie dataframu, dodanie do world -> Widget
        # dodawanie widgetu do layoutu zakladki
        # layaout.addWidget
        # self.__creator = CreateMap(all_files_data)
        pass

