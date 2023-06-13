import folium
from for_main_window.for_map_tab.initial_dataframe import InitialDataframe
from for_main_window.for_map_tab.create_json import CreateJSON
from for_main_window.for_map_tab.last_data_dataframe import LastDataDataframe
import os

class HtmlMap:

    def __init__(self, JSON = CreateJSON):
        self.__json = JSON.get_geoJSON()
        self.__last_data = JSON.get_last_data()
        self.__create_html()

    def __create_html(self):
        map_obj = folium.Map(location=[48, 10], zoom_start=4)
        json_layer = folium.GeoJson(self.__json, name="Countries").add_to(map_obj)

        # w razie dodatkowych danych pojawi się dodatkowy merged_df.columns[] w fields=
        json_layer.add_child(folium.features.GeoJsonPopup(fields=['name', (self.__last_data.columns[-1]), (self.__last_data.columns[-2])], labels=True, localize=True))

        self.__html_path = 'map.html'
        map_obj.save(self.__html_path)

    def get_html_path(self):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, self.__html_path)
        return file_path



# P = r'C:\Users\klime\OneDrive\Pulpit\przydatne_do_projektu\projekt_PROB2023-projekt_wersja2\rail_pa_total_page_spreadsheet.xlsx'
# DF = InitialDataframe(P)
# LDF = LastDataDataframe(DF)
# JSON = CreateJSON(LDF)
# HTML = Html_Map(JSON)
# print(HTML.get_html_path())
