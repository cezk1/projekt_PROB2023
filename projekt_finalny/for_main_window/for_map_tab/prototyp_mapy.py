import sys

import pandas as pd
import geopandas as gpd
import folium
from for_data_handling.make_file_data import MakeFileData
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *

app = QApplication(sys.argv)
########

path = r"C:\Users\klime\OneDrive\Pulpit\projekt_python\projekt_finalny\rail_pa_total_page_spreadsheet.xlsx"

#jakaś metoda, która będzie automatycznie ustawiała nazwy ścieżek - te nazwy dodaje sie potem do wyświetlania statystyk
path_name = 'path1 Data:'

#robi filedata z ścieżki
test1 = MakeFileData(path)
print(test1)
#robi dataframe z ścieżki
d1 = test1.make_test_dataframe()
print(d1)

DF = pd.DataFrame(d1)
print(DF)
#transpozycja potrzebna aby kraje były w wierszach a nie kolumnach
DF_T= DF.transpose()
DF_T.index.name='Country'

#zamiana nazw Turcji i Niemiec aby pasowały do datasetu naturalearth_lowres
DF_T.rename(index={'Türkiye': 'Turkey'}, inplace=True)
DF_T.rename(index={'Germany (until 1990 former territory of the FRG)':'Germany'},inplace=True)
DF_T = DF_T.rename(columns={c:str(c) for c in DF_T.columns})

print(DF_T)

#zrobienie dataframeu:
# PAŃSTWO - OSTATNIE_DANE - OSTATNI_ROK
# Poland - 2506256 - 2021

last_data_df = pd.DataFrame(columns=['name', path_name, 'Last available Year'])

for index, row in DF_T.iterrows():
    last_column = None

    for column in DF_T.columns[::-1]:
        if pd.notnull(row[column]):
            last_column = column
            #print(last_column)
            break

    if last_column is not None:
        data = row[last_column]
        print(f"Country: {row.name}, {path_name} {data}, Year: {last_column}")
        #new_row = pd.DataFrame({'name':row.name, 'Last Data': data, 'Year': last_column}, index=[0])

        last_data_df.loc[index] = [row.name, data, last_column]
print(last_data_df)
print(type(last_data_df))
######

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world.rename(columns={c:str(c) for c in world.columns})

merged_df = pd.merge(world, last_data_df, left_on='name', right_on='name')
print(merged_df)


jsonfile = 'output.geojson'
merged_df.to_file(jsonfile,driver='GeoJSON')
print(jsonfile)
print(type(jsonfile))

map_obj = folium.Map(location=[48, 10], zoom_start=4)
json_layer = folium.GeoJson("output.geojson",name="Countries").add_to(map_obj)

#w razie dodatkowych danych pojawi się dodatkowy merged_df.columns[] w fields=
json_layer.add_child(folium.features.GeoJsonPopup(fields=['name',(last_data_df.columns[-1]),(last_data_df.columns[-2])], labels=True, localize=True))

map_obj.save('map.html')

web_view = QWebEngineView()

web_view.load(QUrl.fromLocalFile(r'C:\Users\klime\OneDrive\Pulpit\projekt_python\projekt_finalny\for_main_window\for_map_tab\map.html'))


main_window = QMainWindow()
layout = QVBoxLayout(main_window)

layout.addWidget(web_view)

central_widget = QWidget(main_window)
central_widget.setLayout(layout)

main_window.setCentralWidget(central_widget)

main_window.show()

app.exec()
