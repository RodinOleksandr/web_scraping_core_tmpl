import settings #содержит исходные данные для парсинга
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
from seleniumwire import webdriver
import time #для создания задержки в синхронных запросах
import urllib #скачиваем изображения
import csv
import asyncio #для планирования ассинхронных запросов
import aiohttp #для ассинхронных запросов
import os
import pickle #для сохранения cookies

next_delay = 0.3
active_calls = 0

def getDataSelenium(url,parser):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('user-agent = Chrome')
    chrome_options.add_argument('--headless')#включение headless режима
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')#отключение определения вебдрайвера
    driver = webdriver.Chrome(
        executable_path='./browsers/chromedriver/chromedriver',
        seleniumwire_options=settings.SELENIUM_PROXY,
        options=chrome_options
    )

    try:
        cookie_name = f"{url.split('//')[-1]}_cookies"

        if os.path.exists(cookie_name):
            print('Загружаем куки с файла')
            for cookie in pickle.load(open(cookie_name , 'rb')):
                driver.add_cookie(cookie)

        checkIP()
        parser(url , driver)


    except Exception as ex:
        print(ex)
    finally:
        print('Сохраняем куки')
        pickle.dump(driver.get_cookies() , open( cookie_name , 'wb'))
        driver.close()
        driver.quit()

def rename (src_dir, trgt_dir):

    for item in os.listdir(source_dir):  # loop through items in dir
    	print("Converted item: " , item)
    	old = source_dir + item
    	new =  target_dir + item + '.pdf'
    	os.rename(old,new)

def write2TxtFile(text, file_name):
    f = open(   f'{settings.PATH}{file_name}.txt'  , 'w')
    f.write(text)
    f.close()

async def getDataAsync(url , session, event , parser , item):

    global active_calls, next_delay

    while active_calls >= settings.MAX_CALLS:
        await event.wait()

    if active_calls >= settings.MAX_CALLS - 1:
        event.clear()

    active_calls += 1
    next_delay += settings.DELAY
    # print('next_delay' , next_delay)
    await asyncio.sleep(next_delay)

    try:
        async with session.get(url=url , headers=settings.HEADERS , proxy=settings.PROXY_ASYNC) as response:

            soup = BeautifulSoup(await response.text(), 'html.parser')
            parser(soup, item);

    finally:
        active_calls -= 1

    if active_calls == 0:
        next_delay = 0.1
        event.set()

def getDataSync(link, retry=5):

    # time.sleep(3)
    try:
        r = requests.get(link, headers=settings.HEADERS , proxies=settings.PROXIES)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup
        print(r.status_code)
    except Exception as ex:
        if retry:
            print(f'[ERROR] Неудачная попытка запроса. Осталось попыток{retry}')
            time.sleep(150/retry)

            return getDataSync(link, retry=(retry - 1))
        else:
            print('Попытки закончились')

def downloadImg(image_url):

    file_name = image_url.split('/')[-1];
    full_path = f'{settings.PATH}/{file_name}'
    try:
        urllib.request.urlretrieve(image_url, full_path)
    except(urllib.error.HTTPError):
        print('I can`t download: ' , image_url)

def write2csv(data):
    with open(f'{PATH}list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def checkIP():
    r = requests.get('https://httpbin.org/ip', proxies=settings.PROXIES)
    print('IP: ', r.json())
