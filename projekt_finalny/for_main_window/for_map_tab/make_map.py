from for_main_window.for_map_tab.html_map import HtmlMap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *


class MapWidget(QWebEngineView):
    def __init__(self,html_map=HtmlMap):
        super().__init__()
        self.__html = html_map.get_html_path()
        self.load(QUrl.fromLocalFile((self.__html)))
    #     self.__create_widget()
    # def __create_widget(self):
    #     web_view = QWebEngineView()
    #     web_view.load(QUrl.fromLocalFile(self.__html))


