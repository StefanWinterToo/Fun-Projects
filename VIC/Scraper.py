from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import re



def extract_user(l):
    user_position = []
    for i in range(len(l)):
        if "BY" in l[i]:
            user_position.append(i)
    print([l[i] for i in user_position])
    print(l)
    print("success")

l = []
l = scrape_site()
print(l)
#extract_user(list)