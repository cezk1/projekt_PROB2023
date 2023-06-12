from PyQt5.QtWidgets import QLineEdit


# pole tekstowe do filtrowania przyciskow panstw
class CountrySearch(QLineEdit):
    def __init__(self, update_filter):
        super().__init__()
        self.__update_filter = update_filter
        self.setPlaceholderText("Search country")
        self.setFixedSize(300, 50)

        self.textChanged.connect(self.__update_filter)

    # def update_on_change(self, text):
    #     print(text)

