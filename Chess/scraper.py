from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
import requests
import random

driver = webdriver.Firefox()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
headers = {'User-Agent': user_agent}
driver.get('https://www.chess.com/games')
r = requests.get('https://www.chess.com/games', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
people = driver.find_elements_by_class_name("post-preview-image")
d1 = webdriver.Firefox()
for i in people:
    d1.get(i.get_attribute("href"))
    #time.sleep(random.randint(0, 10))
    verify = d1.find_elements_by_class_name("no-js")
    if not (verify == []):
        time.sleep(12)
        d1.get(i.get_attribute("href"))
        time.sleep(2)