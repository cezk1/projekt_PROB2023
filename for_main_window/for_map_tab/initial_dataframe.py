import pandas as pd

from for_data_handling.all_files_data import AllFilesData
from for_data_handling.make_file_data import MakeFileData

class InitialDataframe:
    def __init__(self, path, all_files_data=AllFilesData):
        self.__df = None
        self.__path = path
       # self.__all_files_data = all_files_data.get_files_data()
        self.__create_dataframe()
        self.__prepare_dataframe()
        self.__print_dataframe()

    def __create_dataframe(self):
        filedata = MakeFileData(self.__path)
        d1 = filedata.make_test_dataframe()
        self.__df = pd.DataFrame(d1)
        return self.__df

    def __prepare_dataframe(self):
        self.__df = self.__df.transpose()
        self.__df.index.name = 'Country'

        self.__df.rename(index={'Türkiye': 'Turkey'}, inplace=True)
        self.__df.rename(index={'Germany (until...': 'Germany'}, inplace=True)
        self.__df = self.__df.rename(columns={c: str(c) for c in self.__df.columns})
        return self.__df

    def __name_path(self):
        all_files_data = self.__all_files_data
        self.__files_to_show = all_files_data.get_files_data()


    def __print_dataframe(self):
        print(self.__df)


P = 'rail_pa_total_page_spreadsheet.xlsx'
P2 = 'avia_paoc__custom_6007523_page_spreadsheet.xlsx'
DF = InitialDataframe(P)
DF2 = InitialDataframe(P2)


