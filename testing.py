import pandas as pd
from FileData import FileData


def main(file_path):
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_colwidth", None)

    file_data = FileData(file_path)

    file_data.cos_pl()


if __name__ == "__main__":
    excel_file_rail = "rail_pa_total_page_spreadsheet.xlsx"
    excel_file_avia = "avia_paoc__custom_6007523_page_spreadsheet.xlsx"
    excel_file_road = "road_pa_mov_page_spreadsheet.xlsx"

    main(excel_file_road)
