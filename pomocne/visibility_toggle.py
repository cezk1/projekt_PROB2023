import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Chart(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

        self.axes.plot([1, 2, 3, 4, 5], [1, 2, 3, 2, 1])

class Window(QMainWindow):
    def __init__(self, chart):
        super().__init__()

        self.setWindowTitle("PyQt and Matplotlib")

        self.chart = chart

        self.btn = QPushButton("Toggle Line Visibility", self)
        self.btn.clicked.connect(self.toggle_visibility)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)
        layout.addWidget(self.btn)
        layout.addWidget(self.chart)

    def toggle_visibility(self):
        line = self.chart.axes.lines[0]
        line.set_visible(not line.get_visible())
        self.chart.draw()

app = QApplication(sys.argv)
chart = Chart()
window = Window(chart)
window.show()
sys.exit(app.exec_())
