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

""" 
module_name, package_name, ClassName, method_name, 
ExceptionName, function_name, GLOBAL_CONSTANT_NAME, 
global_var_name, instance_var_name, function_parameter_name, local_var_name.

"""


def intiliaze_driver():
    location_of_driver = os.getcwd()
    browser = webdriver.Chrome(executable_path=(location_of_driver + "/chromedriver"))
    return browser


def open_naukril_url(browser):
    browser.maximize_window()
    browser.get('https://www.naukri.com/mnjuser/homepage')
    time.sleep(2)


def login_into_naukri_url(browser):
    username = "nikkyvineeth@gmail.com"
    password = "7404325884"
    browser.find_element_by_id("usernameField").send_keys(username)
    browser.find_element_by_id("passwordField").send_keys(password)
    browser.find_element_by_xpath("//button[@data-ga-track='spa-event|login|login|Save']").click()
    time.sleep(2)
    browser.find_element_by_xpath("//a[@title='Search Jobs']").click()
    time.sleep(10)

def search_jobs_based_on_city(browser, city):
    
    try:
        WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.ID, 'block')))
    except Exception as e:
        print(e)
    browser.find_element_by_xpath("//span[contains(text(),'Later')]").click()
   # browser.find_element_by_xpath("//button[text()='GOT IT']").click()
    browser.execute_script('window.scrollBy(0, 1000)')
    browser.find_element_by_xpath("//body/div/div/div/ul/li[4]/a[1]/span[1]").click()
    time.sleep(10)
    

def set_filters_on_results(browser):
    #browser.find_element_by_id("filter-freshnessFor").click()
    #browser.find_element_by_xpath("//a[@data-id='filter-freshness_7'").click()
    pass

    


    



browser = intiliaze_driver()
open_naukril_url(browser)
login_into_naukri_url(browser)
search_jobs_based_on_city(browser, "Hyderabad")
set_filters_on_results(browser)