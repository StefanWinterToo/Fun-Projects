from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from ButtonClicker import click_on_button

def load():
    driver = webdriver.Chrome('/Users/stefanwinter/Documents/FindStox/Git/VIC/chromedriver')
    driver.get('https://valueinvestorsclub.com/ideas')

    driver.implicitly_wait(2)

    html_body = driver.find_elements_by_xpath('//*[(@id = "ideas_body")]')

    data = html_body[0].text
    data = data.split("\n")

    driver.implicitly_wait(2)
    print("loaded data", html_body[0])

    click_on_button(driver)

    print("###########")
    print(html_body[0].text)
    with open("data/vic.txt", "w") as file:
        file.write(html_body[0].text)
    print("Saved Text")
    

load()