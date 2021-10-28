from proxy_creds import (username , password)
PROXIES = {
    "http": f'http://{username}:{password}@{ip}:54055',
    "https": f'http://{username}:{password}@{ip}:54055',
    "socks5": f'http://{username}:{password}@{ip}:47638'
}

PROXY_ASYNC = f'http://{username}:{password}@{ip}:54055'

SELENIUM_PROXY = {
   'proxy': {
        'http': f'http://{username}:{password}@{ip}:54055',
        'https': f'http://{username}:{password}@8{ip}:54055',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

PATH = './data/'

MAX_CALLS = 5
DELAY = 0.1
