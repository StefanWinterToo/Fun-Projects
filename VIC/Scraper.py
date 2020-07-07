from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('/Users/stefanwinter/Downloads/chromedriver')
driver.get('https://valueinvestorsclub.com/ideas')

# Extract Information
user_id = driver.find_elements_by_xpath('//*[@id="ideas_body"]/div[2]/div[3]/p[1]/span[1]')
print(user_id.text)
user_list = []
for i in user_id:
    user_list.append(i.get_attribute('id'))

print(user_list)
