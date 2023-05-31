from read_file import ReadFile
from file_data import FileData
from country_data import CountryData
from year_data import YearData

import numpy as np


# MakeFileData tworzy obiekty FileData ze wszystkimi danymi z jednego pliku
class MakeFileData:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__structure = ReadFile(file_path).get_structure()  # arkusz "Structure"
        self.__sheet1 = ReadFile(file_path).get_sheet1()  # arkusz "Sheet 1"
        self.__time_row_nr = None
        self.__countries_with_data = []

    # stworzenie listy krajow
    def __make_countries_list(self):
        df1 = self.__structure
        countries_df = df1.loc[(df1["Dimension"] == "Geopolitical entity (reporting)")]
        countries_list = list()
        for elem in list(countries_df.iloc[:, 2]):
            if elem[0:14] != "European Union":
                countries_list.append(elem)

        return countries_list

    # stworzenie listy lat
    def __make_year_list(self):
        df1 = self.__sheet1
        years_list = list()

        for row_index, row in df1.iterrows():
            if row[0] == "TIME":
                self.__time_row_nr = row_index
                for elem in row.items():
                    year_nr = str(elem[1])
                    if year_nr.lower() != "nan" and year_nr != "TIME":
                        years_list.append(year_nr)

        return years_list

    def __make_year_data(self, year_nr: str, value):
        return YearData(year_nr, value)

    def __make_country_data(self, country_name: str, years_data: list):
        return CountryData(country_name, years_data)

    def __read_data(self):
        df1 = self.__sheet1  # dataframe z danymi
        countries_list = self.__make_countries_list()
        years_list = self.__make_year_list()
        time_row = df1.iloc[self.__time_row_nr]



        for row_index, row in df1.iterrows():
            if row[0] in countries_list:
                row_name = row[0]
                years_data = list()  # pusta lista na dane dla jednego kraju

                for i in range(len(row)):
                    if time_row[i] in years_list:
                        years_data.append(self.__make_year_data(time_row[i], row[i]))

                self.__countries_with_data.append(self.__make_country_data(row_name, years_data))

        # TODO: czy takie rozwiazenie jest git?
        # for elem in countries_with_data:
        #     print(elem)
        print(type(self.__countries_with_data))

        return self.__countries_with_data

    def make_data(self):
        return self.__read_data()

    def test(self):
        print(self.__sheet1, "".center(60, "="), sep="\n")
        # print(self.__make_year_list())
        print(self.__make_countries_list())
        self.make_data()
