from for_data_handling.file_data import FileData
import bisect


class AllFilesData:
    def __init__(self):
        self.__files_data = []
        self.__all_paths = []
        self.__all_years = []
        self.__all_countries = []

    def add_file(self, file_path):
        self.__make_file_data(file_path)

    def get_files_data(self):
        return self.__files_data

    def get_all_years(self):
        return self.__all_years

    def get_all_countries(self):
        return self.__all_countries

    def __make_file_data(self, file_path):
        if file_path not in self.__all_paths:
            path_data = FileData(file_path)
            self.__files_data.append(path_data)
            self.__update_all_years(path_data)
            self.__update_all_countries(path_data)
        else:
            print("Path already loaded")

    def __update_all_years(self, file_data: FileData):
        for year in file_data.get_years():
            if year not in self.__all_years:
                bisect.insort(self.__all_years, year)

    def __update_all_countries(self, file_data: FileData):
        for country in file_data.get_names():
            if country not in self.__all_countries:
                bisect.insort(self.__all_countries, country)



