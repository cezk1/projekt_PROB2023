import pandas as pd

from for_data_handling.all_files_data import AllFilesData
from for_data_handling.make_file_data import MakeFileData

class InitialDataframe:
    def __init__(self, path):
        self.__df = None
        self.__path = path
        self.__create_dataframe()
        self.__prepare_dataframe()
        #self.__print_dataframe()

    def __create_dataframe(self):
        filedata = MakeFileData(self.__path)
        d1 = filedata.make_test_dataframe()
        self.__df = pd.DataFrame(d1)
        return self.__df

    def __prepare_dataframe(self):
        self.__df = self.__df.transpose()
        self.__df.index.name = 'Country'

        self.__df.rename(index={'Türkiye': 'Turkey'}, inplace=True)
        self.__df.rename(index={'Germany (until 1990 former territory of the FRG)': 'Germany'}, inplace=True)
        self.__df = self.__df.rename(columns={c: str(c) for c in self.__df.columns})
        return self.__df

    def get_dataframe(self):
        return self.__df


# P = r'C:\Users\klime\OneDrive\Pulpit\przydatne_do_projektu\projekt_PROB2023-projekt_wersja2\rail_pa_total_page_spreadsheet.xlsx'
# DF = InitialDataframe(P)
# print(type(DF))


