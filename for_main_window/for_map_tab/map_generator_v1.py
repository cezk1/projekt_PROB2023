import os
import sys

import pandas as pd
import geopandas as gpd
import folium
from for_data_handling.make_file_data import MakeFileData
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *


class CreateMap:
    def __init__(self, all_files_data):
        self.__all_files_data = all_files_data

    def __test1(self):
        for path in self.__all_files_data.get_all_paths():
            print(path)

    def make1(self):
        self.__test1()
