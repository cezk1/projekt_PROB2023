
from for_main_window.for_map_tab.last_data_dataframe import LastDataDataframe
import geopandas as gpd
import pandas as pd


class CreateJSON:

    def __init__(self, last_data_dataframe=LastDataDataframe):
        self.__last_data_dataframe = last_data_dataframe
        self.__last_data = self.__last_data_dataframe.get_last_data()
        self.__merged_df = None
        # self.__merge_world_data()
        self.__create_geoJSON()

    def __merge_world_data(self):
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        world = world.rename(columns={c: str(c) for c in world.columns})
        self.__merged_df = pd.merge(world, self.__last_data, left_on='name', right_on='name')

        return self.__merged_df
    def __create_geoJSON(self):
        self.__merge_world_data()
        self.__jsonfile = 'output.geojson'
        self.__merged_df.to_file(self.__jsonfile, driver='GeoJSON')

    def get_geoJSON(self):
        return self.__jsonfile

    def get_last_data(self):
        return self.__last_data



# P = r'C:\Users\klime\OneDrive\Pulpit\przydatne_do_projektu\projekt_PROB2023-projekt_wersja2\rail_pa_total_page_spreadsheet.xlsx'
# DF = InitialDataframe(P)
# LDF = LastDataDataframe(DF)
# JSON = CreateJSON(LDF)
