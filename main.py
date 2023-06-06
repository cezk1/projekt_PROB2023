import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QGridLayout, QWidget,
    QPushButton, QGraphicsPixmapItem,QVBoxLayout, QGroupBox, QHBoxLayout, QScrollArea, QFormLayout
)
from PyQt5.QtCore import Qt


country_list = ["Polska","Holandia","Niemcy","Białoruś","Czechy","Łotwa","Hiszpania",
                "Grecja","Portugalia","Albania","Chorwacja","Wielka Brytania","Rosja",
                "Ukraina","Słowacja","Francja","Słowenia","Węgry","Serbia","Rumunia"]


class FilePath(QLineEdit):

    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Ścieżka do pliku")
        self.setFixedSize(300,50)

class CountrySearch(QLineEdit):

    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Wyszukaj Państwo")
        self.setFixedSize(300,50)

        self.textChanged.connect(self.__update_on_change)

    def __update_on_change(self):
        text = self.text()



class DateSlider(QWidget):

    def __init__(self,slider_min,slider_max):
        super().__init__()
        self.__slider_min = slider_min
        self.__slider_max = slider_max

        self.__setup_slider()
    def __setup_slider(self):
        slider = QSlider()
        slider.setMinimum(self.__slider_min)
        slider.setMaximum(self.__slider_max)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setSingleStep(1)
        slider.setPageStep(1)
        slider.setTickInterval(1)
        slider.setOrientation(Qt.Horizontal)

        result_label = QLabel(f'Wybrana data: {slider.value()}')
        slider.valueChanged.connect(lambda value: result_label.setText(f'Wybrana data: {slider.value()}'))

        min_label = QLabel(f'{self.__slider_min}')
        max_label = QLabel(f'{self.__slider_max}')
        labels = QHBoxLayout()
        labels.addWidget(min_label)
        labels.addStretch(1)
        labels.addWidget(max_label)

        layout = QVBoxLayout()
        layout.addWidget(slider)
        layout.addLayout(labels)
        layout.addWidget(result_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)


class CountryButton(QPushButton):
    def __init__(self,name):
        super().__init__(name)
        self.__is_clicked = False
        self.clicked.connect(self.__change_color_on_click)

    def __change_color_on_click(self):
        self.__click()

        if self.__is_clicked:
            color = "blue"
        else:
            color = "None"

        self.setStyleSheet(f"background-color:{color}")

    def __click(self):
        self.__is_clicked = not self.__is_clicked


class CountryList(QScrollArea):

    def __init__(self):
        super().__init__()
        self.__init_list()
        #self.__remove_all_btns()

    def __init_list(self, search_phrase=None):
        self.__btn_layout = QFormLayout()
        self.__btn_group_box = QGroupBox()
        print(search_phrase)

        for country in country_list:
            button_name = f'{country}'
            btn = CountryButton(button_name)
            self.__btn_layout.addWidget(btn)

            is_phrase_in_name = search_phrase is not None \
                                and \
                                (search_phrase in button_name)

            if search_phrase is None or is_phrase_in_name:
                self.__btn_layout.addRow(btn)

        self.__btn_group_box.setLayout(self.__btn_layout)
        self.setWidget(self.__btn_group_box)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)

    def __remove_all_btns(self):
        btn_num = self.__btn_layout.count()
        start_index = btn_num

        for index in range(start_index-1, -1,-1):
            self.__btn_layout.removeRow(index)

    def update_btns(self,search_phrase):
        self.__remove_all_btns()
        self.__init_list(search_phrase)




class MainChart(QLabel):

    def __init__(self):
        super().__init__()
        self.setFixedSize(200,200)
        #self.setPixmap(QGraphicsPixmapItem('1.png'))



class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.__prepare_window()

    def __prepare_window(self):
        self.__set_basic()

        self.__set_layout_elems()
        self.show()

    def __set_basic(self):
        self.setWindowTitle("Okno aplikacji")
        width, height = 1200,900
        self.setFixedSize(width, height)


    def __set_layout_elems(self):
        #w layout_elems powinno być ustawianie zakładek: "Wykres" oraz "Mapa"
        country_search = CountrySearch()
        country_list = CountryList()
        file_path = FilePath()
        date_slider = DateSlider(1990,2000)  #slider przyjmuje dane = min data, max data
        main_chart = MainChart()


        layout = QGridLayout()
        layout.addWidget(file_path,4,4,1,2,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(country_list,1,4,3,2,alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(country_search,0,4,1,2,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(date_slider,4,0,1,4,alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(main_chart,0,0,alignment=Qt.AlignmentFlag.AlignVCenter)


        self.setLayout(layout)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
