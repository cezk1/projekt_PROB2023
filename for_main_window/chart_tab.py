from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class ChartTab(QWidget):
    def __init__(self):
        super().__init__()

        self.__init_view()

    def __init_view(self):
        layout = QVBoxLayout()
        label = QLabel("Chart content goes here", self)

        layout.addWidget(label)

        self.setLayout(layout)
