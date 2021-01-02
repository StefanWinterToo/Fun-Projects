from stem import Signal
from stem.control import Controller
import requests

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

print(requests.get('https://ident.me', proxies=proxies).text)

with Controller.from_port(port = 9051) as c:
    c.authenticate()
    c.signal(Signal.NEWNYM)

print(requests.get('https://api.ipify.org', proxies=proxies).text)