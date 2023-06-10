from PyQt5.QtWidgets import QPushButton


class CountryButton(QPushButton):
    def __init__(self, name, add_function, remove_function):
        super().__init__(name)
        self.__name = name
        self.__add_function = add_function
        self.__remove_function = remove_function
        self.__is_clicked = False

        self.clicked.connect(self.__change_color_on_click)

    def __change_color_on_click(self):
        self.__click()

        if self.__is_clicked:
            color = "grey"
            print(f"clicked: {self.__name}")
            self.__add_function(self.__name)
        else:
            color = "None"
            self.__remove_function(self.__name)

        self.setStyleSheet(f"background-color:{color}")

    def __click(self):
        self.__is_clicked = not self.__is_clicked
