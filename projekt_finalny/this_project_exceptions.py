class FileAlreadyLoaded(Exception):
    def __init__(self, file_path):
        self.__message = f"File with path: {file_path} has already been loaded!"
