from bs4 import BeautifulSoup

with open('48300_dec.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
title = soup.find("h1", class_="chronicle-title")
title = title.contents
#print(title)
table_datetime = soup.find("div", class_="archive-table-left-column").find_all("td")
'''for i in table_datetime:
    if "." in str(i.contents):
        print(i.contents)
    else:
        print("time is" + str(i.contents))'''
# Парсим целую таблицу: Таблица разбивается на строки
table_main = soup.find("div", class_="archive-table-wrap").find_all("tr")
# Парсим отдельные строки: Строки разбиваются на ячейки
for str in table_main:
    src = str.find_all("td")
    for cell in src:
        print(cell.text.strip())
