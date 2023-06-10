from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QTabWidget
from for_main_window.chart_tab import ChartTab
from for_main_window.map_tab import MapTab


# klasa MainWindow wywolywana przy otwieraniu aplikacji tworzy dwie zakladki (na wykres i mape) i dodaje je do
# glownego okna aplikacji
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__init_default_values()
        self.__init_view()

        self.show()

    # ustawienia poczatkowego wygladu okna
    def __init_default_values(self):
        self.__padding_x = 50
        self.__padding_y = 50
        self.__width = 800
        self.__height = 600

    # wdrozenie poczatkowych ustawien okna
    def __init_view(self):
        self.setWindowTitle("Main Window for Project 2023")
        self.setGeometry(self.__padding_x, self.__padding_y, self.__width, self.__height)

        main_layout = self.__config_main_layout()
        self.__add_widgets_to_layout(main_layout)

    # dodanie glownego widgetu, jakim jest QTabWidget pozwalajacy na dodawanie zakladek
    def __config_main_layout(self):
        tab_widget = QTabWidget(self)
        main_layout = tab_widget

        self.setCentralWidget(main_layout)  # CentralWidget musi być w QMainWindow

        return main_layout

    # stworzenie i dodanie do QTabWidget zakladek dla wykresu (ChartTab) i mapy (MapTab)
    def __add_widgets_to_layout(self, main_layout):

        self.__map_tab = MapTab()
        self.__chart_tab = ChartTab(self.__map_tab)

        main_layout.addTab(self.__chart_tab, "Chart")
        main_layout.addTab(self.__map_tab, "Map")
