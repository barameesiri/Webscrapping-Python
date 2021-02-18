from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import re
import json

sportcheck_url = "https://www.sportchek.ca/categories/men/footwear/sneakers-lifestyle-boots/sneakers/product/nike-mens-air-vapormax-flyknit-3-shoes-white-332723629.html?_br_psugg_q=vapormax#332723629%5Bcolor%5D=332723629_10"
nordstrom_url = "https://www.nordstrom.ca/s/nike-air-vapormax-flyknit-3-sneaker-women/5636211?origin=keywordsearch-personalizedsort&breadcrumb=Home%2FAll%20Results&color=100"

#class SportCheckNike:
agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
r1 = requests.get(sportcheck_url,headers=agent)
soup = BeautifulSoup(r1.text, 'html.parser')
#print(soup.prettify())
container = soup.find('div',attrs={'class','product-detail__price-container'})
price_container = container['data-prices']
parse = price_container.split(":",1)
json_data = parse[1]
#Remove { at the end of the JSON format
json_data = json_data[:-1]
data = json.loads(json_data)
print("Price from Sportcheck: ",data['price'])    

#class Nordstrom: Use Selenium

driver = webdriver.Chrome()
#driver = webdriver.Firefox(executable_path='/home/pi/Documents/GitRepo/webscrapping-repo/geckodriver')
driver.get(nordstrom_url)