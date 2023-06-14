from for_main_window.for_map_tab.initial_dataframe import InitialDataframe
import pandas as pd

class LastDataDataframe:
    def __init__(self, initial_dataframe=InitialDataframe):
        self.__initial_dataframe = initial_dataframe
        self.__last_data_df = None
        self.__create_lastdata()

    def __create_lastdata(self):
        dataframe = self.__initial_dataframe.get_dataframe()
        self.__last_data_df = pd.DataFrame(columns=['name', 'Data:', 'Last available Year'])

        for index, row in dataframe.iterrows():
            last_column = None

            for column in dataframe.columns[::-1]:
                if pd.notnull(row[column]):
                    last_column = column
                    # print(last_column)
                    break

            if last_column is not None:
                data = row[last_column]
                #print(f"Country: {row.name}, {path_name} {data}, Year: {last_column}")
                # new_row = pd.DataFrame({'name':row.name, 'Last Data': data, 'Year': last_column}, index=[0])

                self.__last_data_df.loc[index] = [row.name, data, last_column]

        return self.__last_data_df

    def get_last_data(self):
        return self.__last_data_df


# P = r'C:\Users\klime\OneDrive\Pulpit\przydatne_do_projektu\projekt_PROB2023-projekt_wersja2\rail_pa_total_page_spreadsheet.xlsx'
# DF = InitialDataframe(P)
#
# LDF = LastDataDataframe(DF)
# LDF.print()