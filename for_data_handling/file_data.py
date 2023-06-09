from for_data_handling.make_file_data import MakeFileData


class FileData:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__countries_names = []  # lista nazw panstw
        self.__all_years = []  # lista lat
        self.__countries_data = []  # lista obiektow CountryData
        self.__prepare_data()

    def __prepare_data(self):
        print("preparing data...")
        maker = MakeFileData(self.__file_path)
        self.__countries_data = maker.make_data()
        self.__countries_names = maker.get_countries_names()
        self.__all_years = maker.get_all_years()
        print(f"Prepared FileData for: {self.__file_path}")
        # for elem in self.__countries_data:
        #     print(elem)

    def get_names(self):
        return self.__countries_names

    def get_years(self):
        return self.__all_years

    def get_data(self):
        return self.__countries_data

    def get_path(self):
        return self.__file_path

    def __repr__(self):
        return f"\nFile: {self.__file_path}\nCountries: {self.__countries_names}\nYears: {self.__all_years}"

    def __hash__(self):
        return self.__file_path.__hash__()

    def __eq__(self, other):
        return self.__file_path == other.get_path()
