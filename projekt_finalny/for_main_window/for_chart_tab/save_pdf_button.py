from PyQt5.QtWidgets import QPushButton, QFileDialog
from reportlab.lib.utils import ImageReader
from for_main_window.for_chart_tab.pdf_maker import PdfMaker
import os


# przycisk odpowiadajacy za zapisanie wykresu do pliku pdf
class SavePdfButton(QPushButton):
    def __init__(self, img_getter, info_getter):
        super().__init__()

        self.__img_getter = img_getter
        self.__info_getter = info_getter
        self.__pdf_maker = PdfMaker()
        self.setText("Save PDF")
        self.clicked.connect(self.__save_function)

    def __save_function(self):
        img_data = self.__img_getter()
        img = ImageReader(img_data)

        filename = self.__file_chooser()
        min_year = self.__info_getter()[0]
        max_year = self.__info_getter()[1]
        countries = self.__info_getter()[2]

        if len(os.path.basename(filename)) > 0:
            self.__pdf_maker.generate_pdf(filename, img, min_year, max_year, countries)
        else:
            print("File not chosen")

    def __file_chooser(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save chart as PDF", filter="PDF (*.pdf);;All files (*)")
        return filename



