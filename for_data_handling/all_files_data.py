from for_data_handling.file_data import FileData
import bisect


# klasa sluzaca do przechowywania danych z plikow i obslugi tych danych
class AllFilesData:
    def __init__(self):
        self.__files_data = []  # lista obiektow FilesData
        self.__all_paths = []  # lista wszystkich sciezek
        self.__all_years = []  # lista wszystkich lat ze wszystkich plikow
        self.__all_countries = []  # lista wszystkich panstw ze wszystkich plikow

    # add_file sluzy do dodania pliku do przechowywanych danych
    def add_file(self, file_path):
        self.__make_file_data(file_path)

    def get_files_data(self):
        return self.__files_data

    def get_all_years(self):
        return self.__all_years

    def get_all_countries(self):
        return self.__all_countries

    # make_file_data tworzy dane na podstawie przekazanej sciezki
    def __make_file_data(self, file_path):
        if file_path not in self.__all_paths:
            path_data = FileData(file_path)  # stworzenie obiektu FileData dla konkretnej sciezki
            self.__files_data.append(path_data)  # dodanie stworzonego obiektu do listy
            self.__update_all_years(path_data)
            self.__update_all_countries(path_data)
        else:
            print("Path already loaded")

    # zaaktualizowanie listy lat
    def __update_all_years(self, file_data: FileData):
        for year in file_data.get_years():
            if year not in self.__all_years:
                bisect.insort(self.__all_years, year)  # bisect.insort wstawia w odpowiedniej kolejnosci elementy

    # zaaktualizowanie listy panstw
    def __update_all_countries(self, file_data: FileData):
        for country in file_data.get_names():
            if country not in self.__all_countries:
                bisect.insort(self.__all_countries, country)
