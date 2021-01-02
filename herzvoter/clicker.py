from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
from stem import Signal
from stem.control import Controller
import requests
import tester

def load():
    driver = webdriver.Chrome('/Users/stefanwinter/Desktop/tmp/herzvoter/chromedriver')
    driver.get('https://www.shoepy.at/pages/startup-des-jahres-voting?ose=false#')

    driver.implicitly_wait(1)

    print("######")
    print("Start Clicking...")

    frame = driver.find_element_by_xpath('//*[@id="surveyhero-embed-7b323892"]/iframe')
    driver.switch_to.frame(frame)

    #privacy = driver.find_element_by_xpath('//*[@id="shopify-privacy-banner-button-div"]/button[1]')
    #accept = driver.find_element_by_xpath('//*[@id="kt-cookies-cookies_popup"]/div/div[2]/a[2]')

    #privacy.click()
    #driver.implicitly_wait(1)
    #accept.click()
    driver.implicitly_wait(10)
    print("inside iFrame")
    #print(driver.page_source)
    element = driver.find_element_by_xpath('//input[@value="9470786"]')
    #element = driver.find_element_by_xpath('//*[@id="Q3792700"]/div/div[2]/form/div/div[30]/label/div[1]/span/input')
    #element.click()
    driver.implicitly_wait(random.randint(4, 15))
    driver.execute_script("arguments[0].click();", element)
    print("clicked!")
    driver.implicitly_wait(1)

    #driver.switch_to_default_content()
    
    send = driver.find_element_by_xpath('//*[@id="nav-right"]')
    driver.execute_script("arguments[0].click();", send)
    print("sent")
    driver.implicitly_wait(1)
    
def ip():
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    with Controller.from_port(port = 9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)

    print(requests.get('https://api.ipify.org', proxies=proxies).text)


def exec():
    i = 0
    while i < 5:
        i = i+1
        ip()
        load()

exec()