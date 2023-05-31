#TODO: robienie wykresu na podstawie przekazanych danych
from matplotlib import pyplot as plt


class MakeChart:
    def __init__(self, countries_list):
        self.__countries_list = countries_list

    def draw_chart(self):
        lista1 = self.__countries_list[6:10]

        for elem in lista1:
            print(elem)

        print("".center(50, "="))

        for elem in lista1:
            country_name = elem.get_country_name()
            years_data = elem.get_years_data()
            x = []
            y = []
            for year in years_data:
                x.append(year.get_year())
                y.append(year.get_value())

            plt.plot(x, y, "o--", label=country_name)

        plt.xlabel("Years")
        plt.ylabel("Number of passengers")
        plt.legend()
        plt.show()


