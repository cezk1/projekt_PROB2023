from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider
from PyQt5.QtCore import Qt
import sys

class DateSlider(QWidget):
    def __init__(self, parent=None):
        super(DateSlider, self).__init__(parent)

        # Vertical layout
        layout = QVBoxLayout()

        # First slider
        self.slider1 = QSlider(Qt.Horizontal)
        layout.addWidget(self.slider1)

        # Set spacing
        layout.addSpacing(1)

        # Second slider
        self.slider2 = QSlider(Qt.Horizontal)
        layout.addWidget(self.slider2)

        # Set layout
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a DateSlider instance
    date_slider = DateSlider()

    # Show the DateSlider
    date_slider.show()

    # Execute the application
    sys.exit(app.exec_())
