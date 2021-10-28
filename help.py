



                            #Beautiful soup#





# title = soup.title.text.strip()

# page_h1 = soup.find("div").find_all('a')[0]

# user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text

# item_url = item.get("href")
#link_href_attr1 = link["href"]

# link_data_attr = link.get("data-attr")
# link_data_attr1 = link["data-attr"]

# .find_parent() -находит родительский элемент
#.find_parents() -находит коренного родителя вместе со всеми вложенностями

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")

# next_el = soup.find(class_="post__title").find_next().text - возвращает следующий элемент(вложенный)


# .find_next_sibling() .find_previous_sibling() - возвращает следующий элемент
# next_sib = soup.find(class_="post__title").find_next_sibling()

# find_a_by_text = soup.find("a", text="Одежда") - должен содержать полный текст ссылки

# find_a_by_text = soup.find("a", text="Одежда для взрослых")

# find_a_by_text = soup.find("a", text=re.compile("Одежда")) - часть текста
# find_a_by_text = soup.find_all(text=re.compile("[Оо]дежда")) - часть текста c разным регистром





                        #Snippets#





#with open('file.html' , 'w') as file:
#    file.write(text)


#with open('file.html' , 'r') as file:
#    f = file.readlines()
#    for line in f:
#        pass



#with open('file.json' , 'a') as file: -открытие на дозапись
#     json.dump(obj, file, ensure_ascii=False, indent=4)
#    file.write(text)

# folder_name = f'data/data_{item}'
# if os.path.exists(folder_name):
#     print('Папка существует')
# else:
#     os.mkdir(folder_name)
