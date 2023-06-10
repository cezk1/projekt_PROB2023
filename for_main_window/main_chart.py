from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from for_data_handling.all_files_data import AllFilesData
from for_main_window.make_chart import MakeChart


# tego w koncu tez nie uzywam
class MainChart(FigureCanvas):
    def __init__(self, make_chart: MakeChart):
        width = 10
        height = 10
        dpi = 100
        self.__fig = Figure(figsize=(width, height), dpi=dpi)

        self.__fig, self.__ax = make_chart.draw_chart()

        super(MainChart, self).__init__(self.__fig)
        self.__make_chart = make_chart

    def update_years(self, val_from, val_to):
        print(val_from, val_to)

