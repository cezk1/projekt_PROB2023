from PyQt5.QtWidgets import QPushButton


class CountryButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)
        self.__is_clicked = False
        self.clicked.connect(self.__change_color_on_click)

    def __change_color_on_click(self):
        self.__click()

        if self.__is_clicked:
            color = "grey"
        else:
            color = "None"

        self.setStyleSheet(f"background-color:{color}")

    def __click(self):
        self.__is_clicked = not self.__is_clicked
