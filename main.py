import time
import asyncio #для ассинхронных запросов
import aiohttp #для ассинхронных запросов
import json
from hooks import (
                    write2TxtFile,#params = text, file_name ; save text to 'data' folder
                    getDataSync,#params = url ; return soup
                    # try:
                    #     getDataSync(link)
                    # except Exception as ex:
                    #     continue
                    getDataSelenium,#params = (url , parser) ;
                    getDataAsync, #params = (url , session, parser) ;
                    downloadImg,#params = image_url ; save img to 'data' folder
                    write2csv,#params = data ; add new row to csv file
                    rename,# params=(src_dir, trgt_dir)
                    checkIP # check own IP (for proxy debuging)
                   )

start_time = time.time()

    #PARSER EXAMPLES

#1. For async requests

# def parser(soup , item):
#     name = str(item["ID"]) + '. ' + item["Title"]
#     name = name.replace('/' , '|')[:100] #заменяем символы, чтобы не ломался путь при записи файла и обрезаем длину
#     try:
#         text = soup.find(id="begin").get_text()
#         write2TxtFile(text , name)
#     except Exception:
#         write2TxtFile('text' , f'{item["ID"]}. Пустой')
#
#     try:
#         image = soup.find("img", {"class": "figure_img"})
#         image_url = image.get('src')
#         downloadImg( image_url)
#     except Exception:
#         print('Фото отсутствует')

#2. For selenium

# def selenium_parser(url , driver):
#
#     driver.get(url)
#     time.sleep(5)
#     search_input = driver.find_element_by_id('search')
#     search_input.clear()
#     search_input.send_keys('5YJ3E1EA0JF042788')
#     submit_btn = driver.find_element_by_id('submit')
#     submit_btn.click()
#
#     time.sleep(5)


async def parseAsyncFromJSON():# 1. Берем данные с json и пробегаемся по ним
     with open('./data/list.json') as data_file:
        data = json.load(data_file)
        async with aiohttp.ClientSession() as session: #создаем контекст, позволяющий работь через одну сессию
            tasks = [] #создаем массив для хранения заданий

            event = asyncio.Event()
            event.set()

            for item in data:
                if item["ID"] < 20:#ограничение колличества запросов для дебага

                    task = asyncio.create_task(getDataAsync(item["Link"] , session, event , parser , item)) #создаем корутин
                    tasks.append(task) #добавляем корутин в стек
            await asyncio.gather(*tasks)


def main():
    #asyncio.run(parseAsyncFromJSON())
    #checkIP()

    #getDataSelenium('https://bidfax.info', selenium_parser)

    finish_time = round(time.time() - start_time , 1)
    print(f"Execution time: {finish_time} s")



if __name__ == "__main__":
    main()
