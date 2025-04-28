#1

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.cel.ro/calculatoare-desktop/')
driver.implicity_wait(10)

description_tci=driver.find_elements("class name" , "productTitle")
price_tci=driver.find_elements("class name" , "price")

descriptions=[]
prices=[]

for element in description_tci :
    print("Description" , element.get_attribute("innerText"))
    desc=element.get_attribute("innerText")
    descriptions.append(desc)
    
for p in price_tci :
    print("Price is:", p.get_attribute("innerText"))
    price= p.get_attribute("innerText")
    prices.append(price)
print(descriptions, prices)
