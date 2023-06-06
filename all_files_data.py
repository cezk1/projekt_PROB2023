from file_data import FileData


class AllFilesData:
    def __init__(self):
        self.__files_data = []

    def add_file(self, file_path):
        self.__make_file_data(file_path)

    def __make_file_data(self, file_path):
        path_data = FileData(file_path)
        self.__files_data.append(path_data)


    def get_files_data(self):
        return self.__files_data

