from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_tci = webdriver.Chrome()  

driver_tci.get("https://www.thesill.com/collections/ready-to-ship")

time.sleep(5)

product_tci = []
price_tci = []

try:
    product_section = driver_tci.find_element(By.CLASS_NAME, "collection_products")
    product_elements = product_section.find_elements(By.CLASS_NAME, "text-sm")
    product_tci = [el.text for el in product_elements if el.text.strip() != '']
except Exception as e:
    print("Error extracting products:", e)

try:
    price_elements = product_section.find_elements(By.CLASS_NAME, "text-xs")
    for el in price_elements:
        price_text = el.text.replace('$', '').strip()
        if '–' in price_text:  
            dash_index = price_text.find('–')
            price = price_text[:dash_index].strip()
        else:
            price = price_text.strip()
        try:
            price_tci.append(float(price))
        except ValueError:
            continue  
except Exception as e:
    print("Error extracting prices:", e)

print("product_tci:")
print(product_tci)

print("\nprice_tci:")
print(price_tci)

driver_tci.quit()