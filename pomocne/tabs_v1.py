from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QApplication
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(100, 100, 600, 400)

        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Map Tab
        self.map_tab = QWidget(self)
        self.map_layout = QVBoxLayout(self.map_tab)
        self.map_label = QLabel("Map content goes here", self)
        self.map_layout.addWidget(self.map_label)
        self.tab_widget.addTab(self.map_tab, "Map")

        # Chart Tab
        self.chart_tab = QWidget(self)
        self.chart_layout = QVBoxLayout(self.chart_tab)
        self.chart_label = QLabel("Chart content goes here", self)
        self.chart_layout.addWidget(self.chart_label)
        self.tab_widget.addTab(self.chart_tab, "Chart")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())