from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QLabel


# lista wczytanych plikow
class AddedFilesList(QScrollArea):
    def __init__(self):
        super().__init__()
        self.__init_view()

    def __init_view(self):
        self.setWidgetResizable(True)
        # self.setFixedSize(300, 100)
        self.__scroll_content = QWidget(self)
        self.__scroll_layout = QVBoxLayout(self.__scroll_content)
        self.setWidget(self.__scroll_content)

    # dodanie sciezki do listy
    def update_list(self, text, nr):
        name = f"({nr}) {text}"
        label = QLabel(name)
        self.__scroll_layout.addWidget(label)
