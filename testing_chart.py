import pandas as pd
from for_main_window.for_chart_tab.make_chart import MakeChart
from for_data_handling.all_files_data import AllFilesData


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
    for path in file_paths:
        test_afd.add_file(path)
        # test_chart.add_file_to_show(path)

    test_chart = MakeChart(test_afd)

    countries_list = ['Austria', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czechia', 'Denmark',
                      'Estonia', 'Finland', 'France', 'Germany (until 1990 former territory of the FRG)', 'Greece',
                      'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg',
                      'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
                      'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Türkiye', 'United Kingdom']

    test_chart.set_countries(countries_list[0:8])
    test_chart.set_max_year(2015)
    test_chart.set_min_year(2000)
    test_chart.draw_chart()


if __name__ == "__main__":
    excel_file_rail = "rail_pa_total_page_spreadsheet.xlsx"
    excel_file_avia = "avia_paoc__custom_6007523_page_spreadsheet.xlsx"
    excel_file_road = "road_pa_mov_page_spreadsheet.xlsx"

    main(excel_file_avia, excel_file_road, excel_file_rail)

