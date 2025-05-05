from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver_tci = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver_tci.get("https://www.e2esoft.com/shop/")

time.sleep(5)

esoft_tci = []
price_tci = []

products = driver_tci.find_elements("class name", "woocommerce-loop-product__title")
prices = driver_tci.find_elements("class name", ".price")


for product in products:
    esoft_tci.append(product.get_attribute("innerText"))


for price in prices:
    raw_price = price.get_attribute("innerText").replace('$', '').strip()
    if '-' in raw_price:
        raw_price = raw_price.split('-')[0].strip()
    try:
        price_tci.append(float(raw_price))
    except ValueError:
        continue  


print("Products:", esoft_tci)
print("Prices:", price_tci)


driver_tci.quit()