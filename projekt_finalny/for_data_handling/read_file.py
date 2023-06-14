import pandas as pd
import numpy as np


class ReadFile:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__structure_df = None
        self.__sheet1_df = None

    def __read_file(self):
        path = self.__file_path

        # arkusz "Structure"
        structure_df = pd.read_excel(path, sheet_name="Structure", skiprows=1)

        # arkusz "Sheet 1"
        sheet1_df = pd.read_excel(path, sheet_name="Sheet 1", skiprows=1).replace\
            (to_replace=[None, ":", "c"], value=np.nan)

        self.__set_structure_df(structure_df)
        self.__set_sheet1_df(sheet1_df)

    def __set_structure_df(self, dataframe):
        self.__structure_df = dataframe

    def __set_sheet1_df(self, dataframe):
        df_columns = dataframe.columns

        # tutaj zmieniam nazwy kolumn
        for i in range(len(df_columns)):
            column_name = df_columns[i]
            dataframe.rename(columns={f"{column_name}": f"Column {i}"}, inplace=True)

        self.__sheet1_df = dataframe

    def get_sheet1(self):
        self.__read_file()
        dataframe2 = self.__sheet1_df

        return dataframe2

    def get_structure(self):
        self.__read_file()
        dataframe1 = self.__structure_df

        return dataframe1
