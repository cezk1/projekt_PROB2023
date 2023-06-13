from for_data_handling.read_file import ReadFile
from for_data_handling.country_data import CountryData
from for_data_handling.year_data import YearData


# klasa, ktora tworzy wszystkie dane na podstawie dataframow z pliku
class MakeFileData:
    def __init__(self, file_path):
        self.__file_path = file_path
        # ReadFile czyta plik i zwraca dataframy pandas
        self.__structure = ReadFile(file_path).get_structure()  # bierzemy arkusz "Structure" do obrobki
        self.__sheet1 = ReadFile(file_path).get_sheet1()  # bierzemy arkusz "Sheet 1" do obrobki
        self.__time_row_nr = None
        self.__countries_with_data = []  # lista panstw z jednego pliku z odpowiadajacymi danymi
        self.__countries_names = []  # lista wszystkich nazw panstw z pliku
        self.__all_years = []  # lista wszystkich lat z pliku

    # stworzenie listy krajow
    def __make_countries_list(self):
        df1 = self.__structure
        countries_df = df1.loc[(df1["Dimension"] == "Geopolitical entity (reporting)")]
        # powyzsza linijka tworzy dataframe, na ktorym bedziemy operowac tworzac liste panstw
        # stworzony dataframe posiada tylko te wiersze, ktore w kolumnie "Dimension" mialy wartosc
        # "Geopolitical entity (reporting)", w przypadku naszych plikow sa to tylko nazwy panstw i "Eurpean Union..."
        countries_list = list()
        for elem in list(countries_df.iloc[:, 2]):
            if elem[0:14] != "European Union":  # nie chcemy do nazw panstw dodawac "European Union..."
                countries_list.append(elem)

        self.__countries_names = countries_list

    # stworzenie listy lat
    def __make_year_list(self):
        df1 = self.__sheet1
        years_list = list()

        # ponizej odczytujemy wszystkie lata z danymi, w przypadku naszych plikow sa to kolumny dla wiersza "TIME" w
        # arkuszu o nazwie "Sheet 1"
        for row_index, row in df1.iterrows():  # iterujemy po wierszach arkusza
            if row[0] == "TIME":  # jesli wiersz 0 to "TIME", przechodzimy dalej i iterujemy po kolumnach z latami
                self.__time_row_nr = row_index
                for elem in row.items():
                    year_nr = str(elem[1])
                    if year_nr.lower() != "nan" and year_nr != "TIME":
                        years_list.append(year_nr)

        self.__all_years = years_list

    # make_year_data tworzy obiekty YearData
    def __make_year_data(self, year_nr: str, value):
        return YearData(year_nr, value)

    # make_country_data tworzy obiekty CountryData
    def __make_country_data(self, country_name: str, years_data: list):
        return CountryData(country_name, years_data)

    # read_data na podstawie przekazanych dataframow tworzy CountryData i dodaje je do self.__countries_with_data
    def __read_data(self):
        self.__make_countries_list()
        self.__make_year_list()
        df1 = self.__sheet1  # dataframe z danymi
        countries_list = self.__countries_names
        years_list = self.__all_years
        time_row = df1.iloc[self.__time_row_nr]  # time_row to numer wiersza, w ktorym sa wszystkie lata

        for row_index, row in df1.iterrows():
            if row[0] in countries_list:  # przechodzimy dalej jesli row[0] jest nazwa panstwa
                row_name = row[0]  # row_name to nazwa panstwa
                years_data = list()  # pusta lista na dane dla jednego kraju

                for i in range(len(row)):  # iterujemy po kolumnach wiersza dla jednego panstwa
                    if time_row[i] in years_list:  # jesli dana kolumna wiersza w ktorym sa wszystkie lata, jest
                        # w liscie wszystkich lat to przechodzi dalej
                        # (czyli sprawdzenie czy to co jest w danej kolumnie wgl jest statystyka dla danego roku

                        years_data.append(self.__make_year_data(time_row[i], row[i]))  # dodajemy do listy danych
                        # dla jednego kraju obiekt YearData dla odczytanego wlasnie roku

                self.__countries_with_data.append(self.__make_country_data(row_name, years_data)) # dodajemy do listy
                # obiekt CountryData, czyli wszystkie dane dla jednego kraju z jednego pliku

        # zwracamy utworzone dane panstw
        return self.__countries_with_data

    def make_test_dataframe(self):
        self.__read_data()
        test_dict_for_countries = {}
        for elem in self.__countries_with_data:
            country_name = elem.get_country_name()
            value_dict_for_country = {}
            for year in elem.get_years_data():
                value_dict_for_country[year.get_year()] = year.get_value()
            test_dict_for_countries[country_name] = value_dict_for_country
        return test_dict_for_countries

    # ta funkcja jest do wywolywania gdzies, jesli chcemy odczytac dane z pliku
    def make_data(self):
        return self.__read_data()

    def get_countries_names(self):
        return self.__countries_names

    def get_all_years(self):
        return self.__all_years

    def get_dataframe_ulozony(self):
        pass
