from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np

url = 'https://whoscored.com/Matches/1651577/Live/Italy-Serie-A-2022-2023-Napoli-Juventus'
match = 'Napoli 5-1 Juventus'

driver = webdriver.Chrome(r'C:\Users\Admin\chromedriver.exe')
driver.get(url)

t = driver.page_source

start = t.find("matchCentreData")+len('matchCentreData')+2
end = t[t.find("matchCentreData"):].find('matchCentreEventTypeJson') + start - 30

output = t[start:end]
print(output)