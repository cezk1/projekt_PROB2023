from PyQt5.QtWidgets import QPushButton


class ClearListButton(QPushButton):
    def __init__(self, clear_list, clear_chart):
        super().__init__()

        self.setText("Uncheck all")
        self.clicked.connect(clear_list)
        self.clicked.connect(clear_chart)
