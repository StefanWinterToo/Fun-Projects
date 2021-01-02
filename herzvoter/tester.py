from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from urllib.request import ProxyHandler, build_opener, install_opener, Request, urlopen
from stem import Signal
from stem.control import Controller
from selenium.webdriver.chrome.options import Options

class TorHandler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

    def open_url(self, url):
        # communicate with TOR via a local proxy (privoxy)
        def _set_url_proxy():
            proxy_support = ProxyHandler({'http': '127.0.0.1:8118'})
            opener = build_opener(proxy_support)
            install_opener(opener)

        _set_url_proxy()
        request = Request(url, None, self.headers)
        return urlopen(request).read().decode('utf-8')

    @staticmethod
    def renew_connection():
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='btt')
            controller.signal(Signal.NEWNYM)
            controller.close()

def load():
    #driver = webdriver.Chrome('/Users/stefanwinter/Desktop/tmp/herzvoter/chromedriver')

    chrome_options = Options()

    tor_proxy = "127.0.0.1:9050"

    '''chrome_options.add_argument("--test-type")'''
    chrome_options.add_argument('--ignore-certificate-errors')
    '''chrome_options.add_argument('--disable-extensions')'''
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--user-data=/Users/stefanwinter/Library/Application Support/Google/Chrome/')
    chrome_options.add_argument('--proxy-server=socks5://%s' % tor_proxy)
    driver = webdriver.Chrome(executable_path='/Users/stefanwinter/Desktop/tmp_ordner/herzvoter/chromedriver', options=chrome_options)

    driver.get('https://www.shoepy.at/pages/startup-des-jahres-voting?ose=false#')

    driver.implicitly_wait(3)

    print("######")
    print("Start Clicking...")

    frame = driver.find_element_by_xpath('//*[@id="surveyhero-embed-7b323892"]/iframe')
    driver.switch_to.frame(frame)

    #privacy = driver.find_element_by_xpath('//*[@id="shopify-privacy-banner-button-div"]/button[1]')
    #accept = driver.find_element_by_xpath('//*[@id="kt-cookies-cookies_popup"]/div/div[2]/a[2]')

    try:
        driver.implicitly_wait(10)
        #print("inside iFrame")
        element = driver.find_element_by_xpath('//input[@value="9470786"]')
        driver.implicitly_wait(random.randint(1, 5))
        driver.execute_script("arguments[0].click();", element)
        print("clicked!")
        driver.implicitly_wait(1)

        #driver.switch_to_default_content()
        
        send = driver.find_element_by_xpath('//*[@id="nav-right"]')
        driver.execute_script("arguments[0].click();", send)

        #print("sent")
        #time.sleep(3)
        #driver.close()
    except:
        print("Could not click.")
        driver.quit()

def exec():
    wait_time = 1
    number_of_ip_rotations = 1
    tor_handler = TorHandler()
    
    ip = tor_handler.open_url('http://icanhazip.com/')
    print('My first IP: {}'.format(ip))
    
    # Cycle through the specified number of IP addresses via TOR
    for i in range(0, number_of_ip_rotations):
        old_ip = ip
        seconds = 0
    
        tor_handler.renew_connection()
    
        # Loop until the 'new' IP address is different than the 'old' IP address,
        # It may take the TOR network some time to effect a different IP address
        while ip == old_ip:
            time.sleep(wait_time)
            seconds += wait_time
            print('{} seconds elapsed awaiting a different IP address.'.format(seconds))
    
            ip = tor_handler.open_url('http://icanhazip.com/')
        
        print('My old IP: {}'.format(old_ip))
        print('My new IP: {}'.format(ip))
        print("")
        time.sleep(2)
        if ip != old_ip:
            try:
                load()
            except:
                break

exec()