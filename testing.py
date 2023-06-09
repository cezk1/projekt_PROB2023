import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

    # rail_pa_total_page_spreadsheet.xlsx
    # avia_paoc__custom_6007523_page_spreadsheet.xlsx
    # road_pa_mov_page_spreadsheet.xlsx


if __name__ == "__main__":
    main()
