from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common import exceptions
import csv
import pandas as pd

product_name = []
product_description = []
disponibility = []

try:
    for i in range(1, 16):
        url = "https://www.mytek.tn/13-pc-portable#/page-" + str(i)
        driver = webdriver.Firefox(executable_path=r'/home/hosni/Downloads/geckodriver/geckodriver')
        driver.get(url)
        products = driver.find_elements_by_class_name("product-name")
        description = driver.find_elements_by_class_name("product-desc-grid")
        disponibilite = driver.find_elements_by_class_name("custAvailableClass")
        for i in products:
            product_name.append(i.text)
        for j in description:
            product_description.append(j.text)

except exceptions.StaleElementReferenceException:
    pass

print("Description", len(product_description))
print("Name Products", len(product_name))

s1 = pd.Series(product_name, name='Name_Product')
s2 = pd.Series(product_description, name='Product_Desciption')
df = pd.concat([s1, s2], axis=1)
df.to_csv("MyTek_PC_Portable.csv")
