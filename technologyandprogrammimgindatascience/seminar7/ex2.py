#2

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_tci = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver_tci.get('https://www.emag.ro/laptopuri/filter/tip-laptop-f7882,home-v-3292210/c?ref=subcat_0_fashion-grid_1')
driver_tci.implicitly_wait(10)

description_tci = driver_tci.find_elements(By.CLASS_NAME, "px-2")
product_tci = driver_tci.find_elements(By.CLASS_NAME, "product-new-price")

descriptions = []
prices = []

for element in description_tci:
    print("Description" , element.get_attribute("innerText"))
    desc = element.get_attribute("innerText")
    descriptions.append(desc)

for p in product_tci:
    print("Price is:", p.get_attribute("innerText"))
    price = p.get_attribute("innerText")
    prices.append(price)
    
print(descriptions, prices)
