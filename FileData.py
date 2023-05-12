from ReadDataFromFile import ReadDataFromFile
from CountryData import CountryData


class FileData:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__structure = ReadDataFromFile(file_path).get_dataframes()[0]
        self.__sheet1 = ReadDataFromFile(file_path).get_dataframes()[1]

    def make_countries(self):
        df1 = self.__structure

        countries_df = df1.loc[(df1["Dimension"] == "Geopolitical entity (reporting)")]
        countries_list = list()

        for elem in list(countries_df.iloc[:, 2]):
            if elem[0:14] != "European Union":
                countries_list.append(elem)

        print(countries_list)

        years_df = df1.loc[(df1["Dimension"] == "Time")]
        years_list = list(years_df.iloc[:, 2])
        print(years_list)

        df2 = self.__sheet1
        # print("\n", df2)

        data_dict = {}

        for index, row in df2.iterrows():
            country_name = row[0]
            values = list(row)[1::2]
            if row[0] in countries_list:
                print(f"Country: {country_name}\nValues: {values}\n")
                for i in range(len(values)):
                    data_dict[years_list[i]] = values[i]

        print(data_dict)

