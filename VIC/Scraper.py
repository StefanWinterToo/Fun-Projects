from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

driver = webdriver.Chrome('/Users/stefanwinter/Documents/FindStox/Git/VIC/chromedriver')
driver.get('https://valueinvestorsclub.com/ideas')

# Extract Information
## Only extract Idea, price and market cap:
### user_id = driver.find_elements_by_xpath('//div[@class="col-xs-10 top"]')
driver.implicitly_wait(2)
html_body = driver.find_elements_by_xpath('//*[(@id = "ideas_body")]')

data = str(html_body[0].text)
