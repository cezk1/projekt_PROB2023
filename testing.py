import pandas as pd
from make_file_data import MakeFileData
from file_data import FileData
from read_file import ReadFile
from make_chart import MakeChart
from all_files_data import AllFilesData


def main(*file_paths):
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_colwidth", None)

    # mfd1 = MakeFileData(file_path)
    # mfd1.test()
    # lista1 = mfd1.make_data()

    # chart1 = MakeChart(lista1)
    # chart1.draw_chart()

    test_afd = AllFilesData()
    test_chart = MakeChart()

    for path in file_paths:
        # test_afd.add_file(path)
        test_chart.add_file_to_show(path)


    test_chart.create_line_chart()


if __name__ == "__main__":
    excel_file_rail = "rail_pa_total_page_spreadsheet.xlsx"
    excel_file_avia = "avia_paoc__custom_6007523_page_spreadsheet.xlsx"
    excel_file_road = "road_pa_mov_page_spreadsheet.xlsx"

    main(excel_file_rail, excel_file_road)

