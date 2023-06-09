class CountryData:
    def __init__(self, country_name: str, years_data: list):
        self.__country_name = country_name
        self.__years_data = sorted(years_data, key=lambda x: x.get_year())  # lista obiektow YearData

    def __repr__(self):
        return f"{self.__country_name}: {self.__years_data}"

    def get_country_name(self):
        if len(self.__country_name) > 15:
            name = self.__country_name[0:15].strip() + "..."
        else:
            name = self.__country_name

        return name

    def get_years_data(self):
        return self.__years_data

