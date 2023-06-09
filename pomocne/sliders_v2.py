from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QGridLayout
from PyQt5.QtCore import Qt
import sys


class DateSlider(QWidget):
    def __init__(self, min_val, max_val, step, tick_interval, parent=None):
        super(DateSlider, self).__init__(parent)

        # Set class variables
        self.__min_val = min_val
        self.__max_val = max_val
        self.__step = step
        self.__tick_interval = tick_interval

        # Vertical layout
        layout = QVBoxLayout()

        # First slider
        self.slider1 = self.__create_slider_with_labels()
        layout.addWidget(self.slider1)

        # Set spacing
        layout.addSpacing(50)

        # Second slider
        self.slider2 = self.__create_slider_with_labels()
        layout.addWidget(self.slider2)

        # Set layout
        self.setLayout(layout)

    def __create_slider_from(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val)
        slider.setSingleStep(self.__step)
        slider.setTickInterval(self.__tick_interval)
        slider.setTickPosition(QSlider.TicksAbove)
        slider.setPageStep(self.__step)

        slider.setValue(self.__min_val)
        slider.valueChanged.connect(self.__handle_from_change)

        return slider

    def __create_slider_with_labels(self):
        slider = self.__create_slider_from()

        layout = QGridLayout()
        layout.addWidget(slider, 0, 0, 1, self.__max_val + 1)

        for i in range(self.__min_val, self.__max_val + 1, self.__tick_interval):
            label = QLabel(str(i))
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label, 1, i)

        slider_widget = QWidget()
        slider_widget.setLayout(layout)

        return slider_widget

    def __handle_from_change(self, value):
        print("Slider value changed to: ", value)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a DateSlider instance
    date_slider = DateSlider(0, 100, 1, 10)

    # Show the DateSlider
    date_slider.show()

    # Execute the application
    sys.exit(app.exec_())
