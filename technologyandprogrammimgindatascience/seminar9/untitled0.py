from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import tkinter as fd
from tkinter import Button
from selenium.webdriver.common.by import By

driver_tci = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver_tci.get('https://www.cel.ro/calculatoare-desktop/')
driver_tci.implicitly_wait(10)

description_tci = []
costs_tci = []

def get_prices_tci():
    description_tci.clear()
    costs_tci.clear()

description_elements = driver_tci.find_elements(By.CLASS_NAME, "productTitle")
price_elements = driver_tci.find_elements(By.CLASS_NAME, "price")

for element in description_elements:
    desc = element.get_attribute ("innerText")
    description_tci.append(desc)
    
for p in price_elements :
    price = p.get_attribute ("innerText")
    costs_tci.apped ("price")
    
product_name_series_tci = pd.Series(description_tci)
price_series_tci = pd.Series(costs_tci)

product_dict_tci = {"Name:" , product_name_series_tci, 
                    "Price:" , price_series_tci}

df_products_tci = pd.DataFrame(product_dict_tci)

filename = fd.askopenfilename()

df_products_tci.to_excel () (f"{filename}.xlsx")

button_get_tci = Button(text="Get data" , command = get_prices_tci)
button_get_tci.pack()

    