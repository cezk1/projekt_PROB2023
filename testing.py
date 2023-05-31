import pandas as pd
from make_file_data import MakeFileData
from file_data import FileData
from read_file import ReadFile
from make_chart import MakeChart


def main(file_path):
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_colwidth", None)

    mfd1 = MakeFileData(file_path)
    # mfd1.test()
    lista1 = mfd1.make_data()

    chart1 = MakeChart(lista1)
    chart1.draw_chart()


if __name__ == "__main__":
    excel_file_rail = "rail_pa_total_page_spreadsheet.xlsx"
    excel_file_avia = "avia_paoc__custom_6007523_page_spreadsheet.xlsx"
    excel_file_road = "road_pa_mov_page_spreadsheet.xlsx"

    main(excel_file_rail)
