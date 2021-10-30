# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 23:14:06 2021

@author: ADMIN
"""

import requests
import re
from selenium import webdriver
import os
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url = 'https://moneycontrol.com'

os.chdir('C:\\Users\\ADMIN\\moneycontrol')

service = webdriver.chrome.service.Service('./chromedriver')
service.start()
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options = options.to_capabilities()
driver = webdriver.Remote(service.service_url, options)
driver.get(url)

wait = WebDriverWait(driver, 20)

string1 = "HDFCBANK"
#wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div[2]/div[5]/span"))).click()

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[1]/div/div/div[2]/div/div/form/input[5]"))).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[1]/div/div/div[2]/div/div/form/input[5]"))).send_keys(string1)

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[1]/div/div/div[2]/div/div/form/input[5]"))).send_keys(Keys.ENTER)
#wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[2]/div[6]/div/a"))).click()
i = 1
list1 = []
is_found = False
while 1:
    try:
        
        tex = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[3]/div[2]/div/table/tbody/tr["+str(i)+"]/td[2]"))).text
        num = tex.find("NSE Id :")
        num2 = tex.find("ISIN Id :")
        if tex[num+len("nse id :"):num2-1] == string1:
            is_found = True
            break
        
        i = i + 1
    except:
        break

if not is_found:
    exit(0)
    
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[3]/div[2]/div/table/tbody/tr["+str(i)+"]/td[1]"))).click()


