from for_map.initial_dataframe import InitialDataframe
import pandas as pd


#zdobyć path_name w stylu Path[i]_Data stworzony w initial_dataframe

class LastDataDataframe():
    def __init__(self, initial_dataframe=InitialDataframe):
        self.__initial_dataframe = initial_dataframe

    def __make_dataframe(self):
        last_data_df = pd.DataFrame(columns=['name', path_name, 'Last available Year'])

        for index, row in self.__initial_dataframe.iterrows():
            last_column = None

            for column in self.__initial_dataframe.columns[::-1]:
                if pd.notnull(row[column]):
                    last_column = column
                    break

            if last_column is not None:
                data = row[last_column]
                #print(f"Country: {row.name}, Data: {data}, Year: {last_column}")
                # new_row = pd.DataFrame({'name':row.name, 'Last Data': data, 'Year': last_column}, index=[0])
                last_data_df.loc[index] = [row.name, data, last_column]

