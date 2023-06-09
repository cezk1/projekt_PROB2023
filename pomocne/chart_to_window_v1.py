import sys
import matplotlib

matplotlib.use('QT5Agg')
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)

        self.ax = self.figure.add_subplot(111)
        self.ax.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 10])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Matplotlib in PyQt5")

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        canvas = PlotCanvas()
        layout.addWidget(canvas)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
