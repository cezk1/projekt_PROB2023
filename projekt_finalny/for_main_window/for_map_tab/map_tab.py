from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from for_main_window.for_map_tab.initial_dataframe import InitialDataframe
from for_main_window.for_map_tab.last_data_dataframe import LastDataDataframe
from for_main_window.for_map_tab.create_json import CreateJSON
from for_main_window.for_map_tab.html_map import HtmlMap
from for_main_window.for_map_tab.make_map import MapWidget

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
        DF = InitialDataframe(path)
        LD = LastDataDataframe(DF)
        JS = CreateJSON(LD)
        HL = HtmlMap(JS)
        self.__Map = MapWidget(HL)
        layout = QVBoxLayout()
        layout.addWidget(self.__Map)
        self.setLayout(layout)
        #return self.__Map

        # zrobic instancje make_file_data
        # przekazac do tej instancji "path"
        # wywolac funkcje do robienia dataframu z make_file_data
        # na postawie dataframu stworzyc widget mapy z kilkaniem i wszystkim innym
        # dodac mape do layoutu MapTab


    def make_map(self, path):
        # stworzenie dataframu, dodanie do world -> Widget
        # dodawanie widgetu do layoutu zakladki
        # layaout.addWidget
        pass


