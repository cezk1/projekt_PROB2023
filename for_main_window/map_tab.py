from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class MapTab(QWidget):
    def __init__(self):
        super().__init__()

        self.__init_view()

    def __init_view(self):
        layout = QVBoxLayout()
        label = QLabel("TODO: mapa z geopandas z klikaniem")

        layout.addWidget(label)

        self.setLayout(layout)
