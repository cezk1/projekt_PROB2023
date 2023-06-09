from PyQt5.QtWidgets import QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from for_data_handling.all_files_data import AllFilesData
from make_chart import MakeChart


class MainChart(FigureCanvas):
    def __init__(self, all_files_data: AllFilesData):
        width = 5
        height = 4
        dpi = 100
        self.__fig = Figure(figsize=(width, height), dpi=dpi)

        make_chart = MakeChart(all_files_data)
        self.__fig, self.__ax = make_chart.draw_chart()

        super(MainChart, self).__init__(self.__fig)


