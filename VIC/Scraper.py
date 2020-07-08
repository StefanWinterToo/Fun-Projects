from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

driver = webdriver.Chrome('/Users/stefanwinter/Downloads/chromedriver')
driver.get('https://valueinvestorsclub.com/ideas')

# Extract Information
#user_id = driver.find_elements_by_xpath('//*[@id="ideas_body"]/div[2]/div[3]/p[1]/span[1]')
#print(user_id.text)
#user_list = []
#for i in user_id:
#    user_list.append(i.get_attribute('id'))


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

