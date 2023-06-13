from PyQt5.QtWidgets import QPushButton


class SavePdfButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Save PDF")
