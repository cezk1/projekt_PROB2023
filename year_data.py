class YearData:
    def __init__(self, year, value):
        self.__year = year
        self.__value = value

    def __repr__(self):
        return f"{self.__year}: {self.__value}"
