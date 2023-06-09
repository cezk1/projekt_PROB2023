from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QScrollArea
import sys

class TextBoxButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Text Box and Button Widget")

        layout = QVBoxLayout()

        # Create Scroll Area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        layout.addWidget(self.scroll_area)

        # Create QLineEdit
        self.textbox = QLineEdit()
        layout.addWidget(self.textbox)

        # Create QPushButton
        button = QPushButton("Print Text")
        button.clicked.connect(self.button_clicked)
        layout.addWidget(button)

        self.setLayout(layout)

    def button_clicked(self):
        # Print the text from QLineEdit when the button is clicked
        text = self.textbox.text()
        print(text)

        # Add the text to scroll area
        self.add_text_to_history(text)

    def add_text_to_history(self, text):
        # Create a QLabel with the text and add it to the scroll layout
        label = QLabel(text)
        self.scroll_layout.addWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextBoxButtonWidget()
    window.show()
    sys.exit(app.exec())
