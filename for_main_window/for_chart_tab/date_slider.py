from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QHBoxLayout, QVBoxLayout, QStyleOptionSlider, QGridLayout


class DateSlider(QWidget):

    # DoubleSlider
    def __init__(self, min_val, max_val, update_min_max):  # update_min_max to przekazana funkcja, ktora wplywa na
        # wyswietlany wykres
        super().__init__()
        self.__validate_args(int(min_val), int(max_val))

        self.__min_val = int(min_val)
        self.__max_val = int(max_val)
        self.__step = 1
        self.__tick_interval = self.__step

        self.__update_min_max = update_min_max

        self.__create_view()

    def __validate_args(self, min_val, max_val):
        if min_val >= max_val:
            raise Exception("Wrong values! max_val cannot be lower than min_val.")

    # stworzenie suwaka dat polega na dodaniu dwoch suwakow, gdzie jeden jest ograniczony drugim
    def __create_view(self):
        self.__slider_from = self.__create_slider_from()
        self.__slider_to = self.__create_slider_to()

        self.__chosen_from_label = QLabel(f"Year from: {self.__min_val}")
        self.__chosen_to_label = QLabel(f"Year to: {self.__max_val}")

        labels = QHBoxLayout()
        labels.addWidget(self.__chosen_from_label)
        labels.addStretch(1)
        labels.addWidget(self.__chosen_to_label)

        layout = QVBoxLayout()

        layout.addWidget(self.__slider_to)
        layout.addWidget(self.__slider_from)
        layout.addLayout(labels)

        self.setLayout(layout)

    def __create_slider_from(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val)
        slider.setSingleStep(self.__step)
        slider.setTickInterval(self.__tick_interval)
        slider.setTickPosition(QSlider.TicksAbove)
        slider.setPageStep(self.__step)

        slider.setValue(self.__min_val)
        slider.valueChanged.connect(self.__handle_from_change)
        slider.valueChanged.connect(self.__update_min_max)  # polaczenie zmiany wartosci suwaka ze zmiana na wykresie

        return slider

    def __create_slider_to(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val)
        slider.setSingleStep(self.__step)
        slider.setTickInterval(self.__tick_interval)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setPageStep(self.__step)

        slider.setValue(self.__max_val)
        slider.valueChanged.connect(self.__handle_to_change)
        slider.valueChanged.connect(self.__update_min_max)  # polaczenie zmiany wartosci suwaka ze zmiana na wykresie

        return slider

    def __handle_from_change(self):
        # print(f"Value from: {self.__slider_from.value()}")
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()

        # ograniczenie przesuwania suwaka tak aby slider_from nie mogl byc wiekszy niz slider_to
        if value_from >= value_to - self.__step:
            self.__slider_to.setValue(value_from + self.__step)
        if value_from > self.__max_val - self.__tick_interval:
            self.__slider_from.setValue(self.__max_val - self.__tick_interval)

        self.__update_chosen_val_from()

    def __handle_to_change(self):
        # print(f"Value to: {self.__slider_to.value()}")
        value_from = self.__slider_from.value()
        value_to = self.__slider_to.value()

        # ograniczenie przesuwania suwaka tak aby slider_to nie mogl byc mniejszy niz slider_from
        if value_to <= value_from + self.__step:
            self.__slider_from.setValue(value_to - self.__step)
        if value_to < self.__min_val + self.__tick_interval:
            self.__slider_to.setValue(self.__min_val + self.__tick_interval)

        self.__update_chosen_val_to()

    # tutaj sie zmienia wyswietlana wybrana data od
    def __update_chosen_val_from(self):
        value = self.__slider_from.value()
        # print(f"Updated value from: {value}")
        self.__chosen_from_label.setText(f"Year from: {value}")

    # tutaj sie zmienia wyswietlana wybrana data do
    def __update_chosen_val_to(self):
        value = self.__slider_to.value()
        # print(f"Updated value to: {value}")
        self.__chosen_to_label.setText(f"Year to: {value}")

    def get_val_to(self):
        return self.__slider_to.value()

    def get_val_from(self):
        return self.__slider_from.value()

