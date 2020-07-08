from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

driver = webdriver.Chrome('/Users/stefanwinter/Documents/FindStox/Git/VIC/chromedriver')
driver.get('https://valueinvestorsclub.com/ideas')

def click_on_button():
    driver.implicitly_wait(2)

    i = 0

    while i < 10:
        i = i + 1
        driver.implicitly_wait(2)
        button = driver.find_elements_by_xpath('//*[@id="top"]/div[3]/div[2]/div[1]/a')[0]
        if len(button.text) < 1:
            print("No more pages left")
            break
        else:
            ActionChains(driver).move_to_element(button).click(button).perform()
