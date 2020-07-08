#%%
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import re

driver = webdriver.Chrome('/Users/stefanwinter/Documents/FindStox/Git/VIC/chromedriver')
driver.get('https://valueinvestorsclub.com/ideas')

# Extract Information
## Only extract Idea, price and market cap:
### user_id = driver.find_elements_by_xpath('//div[@class="col-xs-10 top"]')
driver.implicitly_wait(2)
html_body = driver.find_elements_by_xpath('//*[(@id = "ideas_body")]')

data = str(html_body[0].text)

#%%
data = html_body[0].text



# %%
list = data.split("\n")

# %%
def get_item_at_position(item_list, position_list):
    return([item_list[i] for i in position_list])


user_position = []
for i in range(len(list)):
    if "BY" in list[i]:
        user_position.append(i)

print(get_item_at_position(list, user_position))



# %%
