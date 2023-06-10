# klasa przechowujaca dane dla jednego roku
class YearData:
    def __init__(self, year, value):
        self.__year = year  # rok
        self.__value = value  # wartosc dla tego roku (u nas liczba pasazerow)

    def __repr__(self):
        return f"{self.__year}: {self.__value}"

    def get_year(self):
        return int(self.__year)  # tutaj trzeba zwracac int chyba

    def get_value(self):
        return self.__value
