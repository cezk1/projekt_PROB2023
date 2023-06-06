#TODO: robienie wykresu na podstawie przekazanych danych
from matplotlib import pyplot as plt
from file_data import FileData
from this_project_exceptions import FileAlreadyLoaded


class MakeChart:
    def __init__(self):
        self.__files_to_show = []  # lista obiektow FileData
        self.__file_paths = []

    def add_file_to_show(self, file_path: str):
        if file_path not in self.__file_paths:
            self.__files_to_show.append(FileData(file_path))
        else:
            print("File already loaded!")
            # raise FileAlreadyLoaded(file_path)

    def set_max_year(self, year: [int, str]):
        pass

    def set_min_year(self, year: [int, str]):
        pass

    def __update_countries(self):
        pass

    def __update_years(self):
        pass

    def __prepare_data_to_show(self):
        pass

    def create_line_chart(self):
        bar_width = 0.15
        fig, ax = plt.subplots()

        for i, file_data in enumerate(self.__files_to_show):
            for country_data in file_data.get_data()[0:5]:
                # get all years and values for this country
                all_years = [year_data.get_year() for year_data in country_data.get_years_data()]
                all_values = [year_data.get_value() for year_data in country_data.get_years_data()]

                # plot line for this country
                ax.plot(all_years, all_values, marker='o', label=f'{country_data.get_country_name()} (FileData {i + 1})')

        # Adding the legend and showing the plot
        plt.xlabel('Years')
        plt.ylabel('Values')
        plt.title('Values by Year and Country')
        plt.legend()
        plt.grid(True)
        plt.show()
