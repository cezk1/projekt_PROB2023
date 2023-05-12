import pandas as pd
import numpy as np
import os


pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


class ReadData:
    def __init__(self, file_path):
        self.__file_path = file_path

    def read_file(self):
        file_path = self.__file_path
        all_data = pd.read_excel(file_path, sheet_name="Sheet 1", skiprows=1).replace(to_replace=[None, ":"],
                                                                                      value=np.nan)
        structure_sheet = pd.read_excel(file_path, sheet_name="Structure", skiprows=1)
        countries_df = structure_sheet.loc[(structure_sheet["Dimension"] == "Geopolitical entity (reporting)")]
        countries_list = list(countries_df.iloc[3:, 2])

        # caly arkusz danych
        print(all_data)

        # panstwa
        # print(countries_df)
        # print(countries_list)

        # nazwa arkusza z danymi
        df_name = all_data.columns[1]
        # print(df_name)

        # jednostka danych
        df_unit = all_data.iloc[4, 2]
        print(df_unit)

        # df = all_data.replace(to_replace=[None, ":"], value=np.nan).iloc[]


def main(file_path):
    test_read1 = ReadData(file_path)
    test_read1.read_file()


if __name__ == "__main__":
    rail_passengers = "rail_pa_total_page_spreadsheet.xlsx"
    main(rail_passengers)
