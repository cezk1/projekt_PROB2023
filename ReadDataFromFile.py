import pandas as pd
import numpy as np


class ReadDataFromFile:
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
            (to_replace=[None, ":"], value=np.nan)

        self.__set_structure_df(structure_df)
        self.__set_sheet1_df(sheet1_df)

    def __set_structure_df(self, dataframe):
        self.__structure_df = dataframe

    def __set_sheet1_df(self, dataframe):
        self.__sheet1_df = dataframe

    def get_dataframes(self):
        self.__read_file()
        df1 = self.__structure_df
        df2 = self.__sheet1_df

        return df1, df2
