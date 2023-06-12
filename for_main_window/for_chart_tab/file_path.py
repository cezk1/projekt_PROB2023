from PyQt5.QtWidgets import QLineEdit


# do pole tekstowe do wprowadzania sciezek do plikow
class FilePath(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Insert file path")
        self.setFixedSize(300, 50)

