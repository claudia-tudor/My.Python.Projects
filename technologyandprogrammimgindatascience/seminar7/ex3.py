#3

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_tci = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver_tci.get("https://www.somproduct.ro/collections/fotolii")
driver_tci.implicitly_wait(10)

product_tci = driver_tci.find_elements(By.CLASS_NAME, "product-type")
product_tci = driver_tci.find_elements(By.CLASS_NAME, "product-type")

descriptions = []
prices = []

for element in product_tci:
    desc = element.get_attribute("innerText")
    print("Description:", desc)
    descriptions.append(desc)

for p in product_tci:
    print("Price is:", p.get_attribute("innerText"))
    price = p.get_attribute("innerText")
    prices.append(price)
    
print(descriptions, prices)
