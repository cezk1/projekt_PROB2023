from matplotlib import pyplot as plt
from for_data_handling.all_files_data import AllFilesData
from for_data_handling.country_data import CountryData


class MakeChart:
    def __init__(self, all_files_data: AllFilesData):
        self.__files_to_show = all_files_data.get_files_data()  # lista obiektow FileData
        self.__all_years = all_files_data.get_all_years()
        self.__all_countries = all_files_data.get_all_countries()

        self.__max_year = max(self.__all_years)
        self.__min_year = min(self.__all_years)

    def set_max_year(self, year: [int, str]):
        self.__max_year = str(year)

    def set_min_year(self, year: [int, str]):
        self.__min_year = str(year)

    def set_countries(self, countries: list):
        self.__all_countries = countries

    def __update_years(self):
        pass

    def __prepare_data_to_show(self):  # to wsm nic nie robi
        print(type(self.__all_years[0]))
        print(f"Max year in data: {self.__max_year}")
        print(f"Min year in data: {self.__min_year}")
        print(self.__all_countries)

    def __make_data_to_show(self, country_data: CountryData):
        all_years = []
        all_values = []
        for i, year_data in enumerate(country_data.get_years_data()):
            if self.__min_year <= year_data.get_year() <= self.__max_year:
                all_years.append(year_data.get_year())
                all_values.append(year_data.get_value())

        return all_years, all_values

    def __create_line_chart(self):
        # TODO: to trzeba poprawic chyba + dodac updatowanie wykresu

        bar_width = 0.15
        fig, ax = plt.subplots()

        for i, file_data in enumerate(self.__files_to_show, 1):
            # path = file_data.get_path()
            for country_data in file_data.get_data()[0:]:
                if country_data.get_country_name() in self.__all_countries:
                    # get all years and values for this country
                    # all_years = [year_data.get_year() for year_data in country_data.get_years_data()]
                    # all_values = [year_data.get_value() for year_data in country_data.get_years_data()]
                    all_years = self.__make_data_to_show(country_data)[0]
                    all_values = self.__make_data_to_show(country_data)[1]

                    # plot line for this country
                    ax.plot(all_years, all_values, "o--",
                            label=f"{country_data.get_country_name()} (Path nr. {i})")

        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

        # Adding the legend and showing the plot
        plt.xlabel("Years")
        plt.ylabel("Number of passengers")
        plt.title("Values by Year and Country")
        # plt.legend()
        plt.grid()
        plt.show()

    def draw_chart(self):
        self.__prepare_data_to_show()
        self.__create_line_chart()
