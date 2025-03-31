#1

import pandas as pd_tci
import os

current_directory = os.getcwd()

fruit_tci=["clementine", "apple", "lemon", "blueberry"]
color_tci=["orange", "red", "yellow", "blue"]
print("Lists are:")
print(fruit_tci)
print(color_tci)

fruit_series_tci = pd_tci.Series(fruit_tci)
color_series_tci = pd_tci.Series(color_tci) 
print("Series are:")
print(fruit_series_tci)
print(color_series_tci)

dictionary_tci={"Preffered fruits:" , fruit_series_tci, "The colors:" ,color_series_tci}
print("Dictionary is:" , dictionary_tci)
df = pd_tci.DataFrame(dictionary_tci)
print("DataFrame is:" ,df)

df.to_excel(current_directory+"\\fruits.xlsx", sheet_name="My prefered fruits", engine= "xlsxwriter")

dp_selection=pd_tci.read_excel(current_directory+"\\fruits.xlsx", sheet_name= "Selection of fruits" ,
                           engine="xlsxwriter")
