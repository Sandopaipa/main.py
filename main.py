from bs4 import BeautifulSoup
# словарь - как одна строка таблицы
# для хранения всей таблицы имеет смысл сделать словарь

'''Парсер для конкретной HTML страницы, в случае, если нужно парсить
    страницу другого "формата" или вида, как будет угодно - нужно будет
    данный код под конкретную страницу изменять'''

time = []
date = []
buf = []
#dict = {key: value} 19 столбцов таблицы
dict = {
    'time': None,
    'date': None,
    'wind_direction': None,
    'wind_spd': None,
    'visibility': None,
    'cloudy': None,
    't_c': None,
    'td_c': None,
    'f_percent': None,
    'te_c': None,
    'tes_c': None,
    'comfort': None,
    'p_gpa': None,
    'po_gpa': None,
    't_min_c': None,
    't_max_c': None,
    'r_mm': None,
    'r24_mm': None,
    's_cm': None,

}


'''Открываем документ для чтения'''
with open('48300_dec.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
'''Парсим название таблицы (на всякий)'''
title = soup.find("h1", class_="chronicle-title")
title = title.contents
#print(title)
'''Парсим дату и время'''
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
        buf.append(cell.text.strip())
