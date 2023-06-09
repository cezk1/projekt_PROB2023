from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
from for_main_window.for_chart.date_slider import DateSlider


class ChartTab(QWidget):
    def __init__(self):
        super().__init__()

        self.__set_layout_elems()

    def __set_layout_elems(self):
        layout = QGridLayout()

        # elements to add to layout
        date_slider = DateSlider()

        # adding elements to layout
        layout.addWidget(date_slider, 4, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.setLayout(layout)
