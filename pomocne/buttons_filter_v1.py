import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QScrollArea, QPushButton
from PyQt5.QtGui import QColor


class ScrollableButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Scrollable Button Window")
        layout = QVBoxLayout()

        filter_label = QLabel("Filter:")
        self.filter_textbox = QLineEdit()
        self.filter_textbox.textChanged.connect(self.filter_buttons)
        layout.addWidget(filter_label)
        layout.addWidget(self.filter_textbox)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        layout.addWidget(self.scroll_area)
        self.setLayout(layout)

        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        country_list = ["Polska", "Holandia", "Niemcy", "Białoruś", "Czechy", "Łotwa", "Hiszpania",
                        "Grecja", "Portugalia", "Albania", "Chorwacja", "Wielka Brytania", "Rosja",
                        "Ukraina", "Słowacja", "Francja", "Słowenia", "Węgry", "Serbia", "Rumunia"]
        button_names = country_list
        for name in button_names:
            button = QPushButton(name)
            button.clicked.connect(self.button_clicked)
            self.buttons.append(button)
            self.scroll_layout.addWidget(button)

    def filter_buttons(self, text):
        for button in self.buttons:
            if text.lower() in button.text().lower():
                button.setVisible(True)
            else:
                button.setVisible(False)

    def button_clicked(self):
        button = self.sender()
        button.setStyleSheet("background-color: blue")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollableButtonWindow()
    window.show()
    sys.exit(app.exec())
