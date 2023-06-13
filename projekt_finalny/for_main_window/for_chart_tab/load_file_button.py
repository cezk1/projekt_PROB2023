from PyQt5.QtWidgets import QPushButton


class LoadFileButton(QPushButton):
    def __init__(self, func_to_connect):
        super().__init__()

        self.setText("Load inserted path")
        self.clicked.connect(func_to_connect)
