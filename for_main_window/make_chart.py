import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt
from for_data_handling.all_files_data import AllFilesData
from for_data_handling.country_data import CountryData
import bisect


class MakeChart:
    def __init__(self, all_files_data: AllFilesData):
        self.__all_files_data = all_files_data
        if len(self.__all_files_data.get_files_data()) >= 1:
            self.__init_maker()
        else:
            pass

    def __init_maker(self):
        all_files_data = self.__all_files_data
        self.__files_to_show = all_files_data.get_files_data()  # lista obiektow FileData
        self.__all_years = all_files_data.get_all_years()
        self.__all_countries = []

        self.__max_year = max(self.__all_years)
        self.__min_year = min(self.__all_years)

        self.__fig = None
        self.__ax = None

    def set_max_year(self, year: [int, str]):
        self.__max_year = str(year)

    def set_min_year(self, year: [int, str]):
        self.__min_year = str(year)

    def add_country(self, country):
        if country not in self.__all_countries:
            bisect.insort(self.__all_countries, country)
        print(self.__all_countries)

    def remove_country(self, country):
        if country in self.__all_countries:
            self.__all_countries.remove(country)
        print(self.__all_countries)

    def __prepare_data_to_show(self):  # to wsm nic nie robi
        # print(type(self.__all_years[0]))
        print(f"Max year in data: {self.__max_year}")
        print(f"Min year in data: {self.__min_year}")
        # print(self.__all_countries)

    def __make_data_to_show(self, country_data: CountryData):
        all_years = []
        all_values = []
        for i, year_data in enumerate(country_data.get_years_data()):
            if self.__min_year <= year_data.get_year() <= self.__max_year:
                all_years.append(year_data.get_year())
                all_values.append(year_data.get_value())

        return all_years, all_values

    def __create_line_chart(self):
        self.__fig = Figure()
        self.__ax = Figure().add_subplot(111)
        # fig, ax = plt.subplots()
        fig = self.__fig
        ax = self.__ax

        for i, file_data in enumerate(self.__files_to_show, 1):
            for country_data in file_data.get_data():
                if country_data.get_country_name() in self.__all_countries:
                    # get all years and values for this country
                    all_years = self.__make_data_to_show(country_data)[0]
                    all_values = self.__make_data_to_show(country_data)[1]

                    # plot line for this country
                    ax.plot(all_years, all_values, "o--",
                            label=f"{country_data.get_country_name()} (Path nr. {i})")

        # box = ax.get_position()
        # ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

        # Adding the legend and showing the plot
        ax.set_xlabel("Years")
        ax.set_ylabel("Number of passengers")
        ax.set_title("Values by Year and Country")
        ax.grid()
        # plt.show()

    def draw_chart(self):
        self.__prepare_data_to_show()
        self.__create_line_chart()
        print(self.__all_countries)
        return self.__fig, self.__ax


class MakeChartV2(FigureCanvas):
    def __init__(self, all_files_data, country_list, min_year, max_year, width=10, height=10, dpi=100):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)
        self.__all_files_data = all_files_data
        self.__country_list = country_list
        self.__min_year = min_year
        self.__max_year = max_year

        self.__init_view()

    def __init_view(self):
        self.__ax = self.__fig.add_subplot(111)
        # self.__plot_line()
        self.__plot_data()

    def __make_data_to_show(self, country_data: CountryData):
        all_years = []
        all_values = []
        for i, year_data in enumerate(country_data.get_years_data()):
            print(year_data.get_year())
            print(type(self.__min_year), self.__max_year)
            if int(year_data.get_year()) >= self.__min_year and int(year_data.get_year()) <= self.__max_year:
                all_years.append(year_data.get_year())
                all_values.append(year_data.get_value())

        return all_years, all_values

    def __plot_data(self):
        self.__ax.clear()
        ax = self.__ax
        self.__files_to_show = self.__all_files_data.get_files_data()

        for i, file_data in enumerate(self.__files_to_show, 1):
            for country_data in file_data.get_data():
                if country_data.get_country_name() in self.__country_list:
                    # get all years and values for this country
                    all_years = self.__make_data_to_show(country_data)[0]
                    all_values = self.__make_data_to_show(country_data)[1]

                    # plot line for this country
                    ax.plot(all_years, all_values, "o--",
                            label=f"{country_data.get_country_name()} (Path nr. {i})")

        # box = ax.get_position()
        # ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
        ax.legend()
        # Adding the legend and showing the plot
        ax.set_xlabel("Years")
        ax.set_ylabel("Number of passengers")
        ax.set_title("Values by Year and Country")
        ax.grid()

        self.__fig.canvas.draw()

    def __plot_line(self):
        self.__ax.plot([1, 2, 3, 4, 5], [1, 2, 3, 2, 1])
        self.__fig.canvas.draw()

    def update_plot(self, country_list, min_year, max_year):
        self.__country_list = country_list
        self.__min_year = min_year
        self.__max_year = max_year
        # self.__plot_line()
        self.__plot_data()


