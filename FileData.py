from ReadDataFromFile import ReadDataFromFile
from CountryData import CountryData
from YearData import YearData


class FileData:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__structure = ReadDataFromFile(file_path).get_dataframes()[0]  # arkusz "Structure"
        self.__sheet1 = ReadDataFromFile(file_path).get_dataframes()[1]  # arkusz "Sheet 1"

    def make_countries_list(self):
        df1 = self.__structure
        countries_df = df1.loc[(df1["Dimension"] == "Geopolitical entity (reporting)")]
        countries_list = list()
        for elem in list(countries_df.iloc[:, 2]):
            if elem[0:14] != "European Union":
                countries_list.append(elem)

        return countries_list

    def make_year_list(self):
        # TODO: trzeba to zmienic, tak aby lista lat nie zalezala od wygladu excela
        #  czyli zamiast skiprows=7 zrobic zeby szukalo tam gdzie zaczyna sie wiersz "TIME"
        df1 = self.__sheet1
        years_list = list(df1)[1::2]

        return years_list

    def __make_year_data(self, year_nr, value):
        return YearData(year_nr, value)

    def __make_country_data(self, country_name, yd_list):
        return CountryData(country_name, yd_list)

    def cos_pl(self):
        df1 = self.__sheet1
        # print("\n", df1)

        columns_names_list = list(df1)
        countries_list = self.make_countries_list()
        years_list = self.make_year_list()

        country_with_data_list = []

        # iteracja po wierszach dataframe'u z danymi
        for row_index, row in df1.iterrows():
            yd_obj_list = []  # lista na obiekty YearData, lista ta przechowuje elementy typu YearData\
            # dla pojedynczego panstwa

            # sprawdzenie czy pierwszy element wiersza jest nazwa panstwa
            if row[0] in countries_list:
                # iteracja po kolumnach w wierszu z danym panstwem
                for i in range(len(row)):
                    # sprawdzenie czy nazwa kolumny (nazwa w dataframie) jest "nazwa" roku\
                    # jesli jest tworzymy obiekt YearData(year_nr, value)
                    if df1.columns[i] in years_list:
                        year_nr = df1.columns[i]  # year_nr jest numerem roku
                        value = row[i]  # value jest liczba przypisana danemu roku
                        obj = self.__make_year_data(year_nr, value)
                        # nastepnie rozszerzam liste z danymi rocznymi dla konkretnego panstwa
                        yd_obj_list.append(obj)
                # teraz tworze obiekt typu CountryData, ktory przechowuje wszystkie dane roczne\
                # dla danego panstwa
                obj2 = self.__make_country_data(row[0], yd_obj_list)
                # rozszerzam liste panstw z danymi
                country_with_data_list.append(obj2)

        for i in country_with_data_list:
            print(i)

        # print(columns_names_list, countries_list, years_list, sep="\n")
