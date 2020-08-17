import urllib
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time

def ty():
    location_of_driver = os.getcwd()
    browser = webdriver.Chrome(executable_path=(location_of_driver + "/chromedriver"))
    browser.get("https://www.youtube.com")
    
    browser.maximize_window()
    browser.execute_script('window.scrollBy(0,500)')
    time.sleep(10)


ty()

