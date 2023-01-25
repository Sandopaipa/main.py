from bs4 import BeautifulSoup


'''Парсер для конкретной HTML страницы, в случае, если нужно парсить
    страницу другого "формата" или вида, как будет угодно - нужно будет
    данный код под конкретную страницу изменять'''

time = []
date = []

with open('48300_dec.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
title = soup.find("h1", class_="chronicle-title")
title = title.contents
print(title)
table_datetime = soup.find("div", class_="archive-table-left-column").find_all("td")
for i in range(1, len(table_datetime)):
    if "." in str(table_datetime[i].contents):
        time.append(table_datetime[i].contents)
    else:
        date.append(table_datetime[i].contents)
# Парсим целую таблицу: Таблица разбивается на строки
table_main = soup.find("div", class_="archive-table-wrap").find_all("tr")
# Парсим отдельные строки: Строки разбиваются на ячейки
# первые 0-16 ячеек - шапка таблицы
for str in table_main:
    src = str.find_all("td")
    for cell in src:
        print(cell.text.strip())
