import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
import pandas as pd


def main():
    # te ustawienia sa wylacznie do tego zeby ladniej wygladaly dataframy wyswietlane w terminalu
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_colwidth", None)

    app = QApplication(sys.argv)
    # stworzenie okna glownego ze wszystkim wewnatrz
    w = MainWindow()
    w.show()
    app.exec()

    # rail_pa_total_page_spreadsheet.xlsx
    # avia_paoc__custom_6007523_page_spreadsheet.xlsx
    # road_pa_mov_page_spreadsheet.xlsx


if __name__ == "__main__":
    main()
