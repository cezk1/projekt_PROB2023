class CountryData:
    def __init__(self, country_name: str, years_data: list):
        self.__country_name = country_name
        self.__years_data = years_data

    def __repr__(self):
        return f"{self.__country_name}: {self.__years_data}"

