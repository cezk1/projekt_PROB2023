from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import ticker
from for_data_handling.country_data import CountryData
from io import BytesIO


# klasa odpowiadajaca za zrobienie wykresu
class MakeChart(FigureCanvas):
    __IMG_FORMAT = "png"

    def __init__(self, all_files_data, country_list, min_year, max_year, width=10, height=10, dpi=100):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)
        self.__all_files_data = all_files_data
        self.__country_list = country_list
        self.__min_year = int(min_year)
        self.__max_year = int(max_year)

        self.__init_view()

    def get_img_data(self):
        img_data = BytesIO()
        self.__img_fig.savefig(img_data, format=self.__IMG_FORMAT)

        seek_offset = 0
        img_data.seek(seek_offset)

        return img_data

    def __init_view(self):
        self.__ax = self.__fig.add_subplot(111)
        self.__plot_data()

    # make_data_to_show tworzy liste potrzebna do wykresu na podstawie danych jednego panstwa z jednego pliku
    def __make_data_to_show(self, country_data: CountryData):
        all_years = []
        all_values = []
        for i, year_data in enumerate(country_data.get_years_data()):
            if int(year_data.get_year()) >= self.__min_year and int(year_data.get_year()) <= self.__max_year:
                all_years.append(year_data.get_year())
                all_values.append(year_data.get_value())

        return all_years, all_values

    # plot_data robi wykresy dla przekazanej listy krajow i ich wartosci
    def __plot_data(self):
        self.__ax.clear()
        ax = self.__ax
        self.__files_to_show = self.__all_files_data.get_files_data()

        for i, file_data in enumerate(self.__files_to_show, 1):
            for country_data in file_data.get_data():
                if country_data.get_country_name() in self.__country_list:
                    # zbierz wszystkie dane dla lat dla panstwa
                    all_years = self.__make_data_to_show(country_data)[0]
                    all_values = self.__make_data_to_show(country_data)[1]

                    path_for_legend = file_data.get_path()[0:4].strip() + "..."

                    if len(country_data.get_country_name()) > 15:
                        name_for_legend = country_data.get_country_name()[0:15].strip() + "..."
                    else:
                        name_for_legend = country_data.get_country_name()
                    # dodaj wykres panstwa
                    ax.plot(all_years, all_values, "o--",
                            label=f"{name_for_legend} [{path_for_legend}]")

        self.__chart_appearance(ax)

        self.__img_fig = self.__fig

        self.__fig.canvas.draw()

    def update_plot(self, country_list, min_year, max_year):
        self.__country_list = country_list
        self.__min_year = min_year
        self.__max_year = max_year
        self.__plot_data()

    def __chart_appearance(self, ax):
        ax.set_position([0.125, 0.110, 0.6, 0.8])
        ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

        # dodanie legendy i podpisow
        ax.set_xlabel("Years")
        ax.set_ylabel("Number of passengers")
        ax.set_title("Values by Year and Country")

        ax.xaxis.grid(True, which="major", linestyle="-", linewidth=1)

        ax.yaxis.grid(True, which="major", linestyle="-", linewidth=1)
        ax.yaxis.grid(True, which="minor", linestyle="--", linewidth=0.5)

        ax.set_xlim(self.__min_year-0.5, self.__max_year+0.5)

        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))  # ustawienie siatki w osi X co 1 rok
        formatter_for_x = ticker.StrMethodFormatter("{x:.0f}")
        ax.xaxis.set_major_formatter(formatter_for_x)

        self.__years_label_display(ax)
        self.__value_label_display(ax)

    @staticmethod
    def __years_label_display(ax):
        num_xlim = ax.get_xlim()[1] - ax.get_xlim()[0]
        if num_xlim >= 15:
            every_nth = 2
            for n, label in enumerate(ax.xaxis.get_ticklabels(), 1):
                if n % every_nth != 0:
                    label.set_visible(False)
        else:
            pass

    @staticmethod
    def __value_label_display(ax):
        all_ticks = ax.get_yticks()
        val_btt = all_ticks[2] - all_ticks[1]  # value between two ticks
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(val_btt / 5))

