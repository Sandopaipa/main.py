import csv

from bs4 import BeautifulSoup
# словарь - как одна строка таблицы
# для хранения всей таблицы имеет смысл сделать словарь

'''Парсер для конкретной HTML страницы, в случае, если нужно парсить
    страницу другого "формата" или вида, как будет угодно - нужно будет
    данный код под конкретную страницу изменять'''
# Шапка таблицы
header = [
    'Время (UTC)',
    'Дата',
    'Ветер (напр)',
    'Видим.',
    'Явления',
    'Облачность',
    'T (C)',
    'Td (C)',
    'f (%)',
    'Te (C)',
    'Tes (C)',
    'Комфортность',
    'P (гПа)',
    'Po (гПа)',
    'Tmin (C)',
    'Tmax (C)',
    'R (мм)',
    'R24 (мм)',
    'S (см)']
table = [header, ]
row = []
# Столбцы таблицы
date = []
time = []
wind_direction = []
wind_spd = []
visivility = []
conditions = []
cloudy = []
t_c = []
td_c = []
f_per = []
te_c = []
tes_c = []
comfort = []
p_gpa = []
po_gpa = []
t_min_c = []
t_max_c = []
r_mm = []
r24_mm = []
s_cm = []

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
    if i % 2 == 1:
        time.append(table_datetime[i].text)
    else:
        date.append(table_datetime[i].text)




# Парсим целую таблицу: Таблица разбивается на строки
table_main = soup.find("div", class_="archive-table-wrap").find_all("tr")
# Парсим отдельные строки: Строки разбиваются на ячейки
# первые 0-16 ячеек - шапка таблицы
for i in range(1, len(table_main)):
    src = table_main[i].find_all("td")
#Формируем столбцы таблицы
    for j in range(len(src)):
        if j == 0:
            wind_direction.append(src[j].text)
        elif j == 1:
            wind_spd.append(src[j].text)
        elif j == 2:
            visivility.append(src[j].text)
        elif j == 3:
            conditions.append(src[j].text)
        elif j == 4:
            cloudy.append(src[j].text)
        elif j == 5:
            t_c.append(src[j].text)
        elif j == 6:
            td_c.append(src[j].text)
        elif j == 7:
            f_per.append(src[j].text)
        elif j == 8:
            te_c.append(src[j].text)
        elif j == 9:
            tes_c.append(src[j].text)
        elif j == 10:
            comfort.append(src[j].text)
        elif j == 11:
            p_gpa.append(src[j].text)
        elif j == 12:
            po_gpa.append(src[j].text)
        elif j == 13:
            t_min_c.append(src[j].text)
        elif j == 14:
            t_max_c.append(src[j].text)
        elif j == 15:
            r_mm.append(src[j].text)
        elif j == 16:
            r24_mm.append(src[j].text)
        elif j == 17:
            s_cm.append(src[j].text)
# Формируем строки таблицы и саму таблицу
# Можно в принципе уже здесь писать в файл, так как тут формируется таблица
# Это позволит не формировать её, что уменьшит затраты по памяти и времени
for i in range(len(date)):
    row.append(date[i])
    row.append(time[i])
    row.append(wind_direction[i])
    row.append(wind_spd[i])
    row.append(visivility[i])
    row.append(conditions[i])
    row.append(cloudy[i])
    row.append(t_c[i])
    row.append(td_c[i])
    row.append(f_per[i])
    row.append(te_c[i])
    row.append(tes_c[i])
    row.append(comfort[i])
    row.append(p_gpa[i])
    row.append(po_gpa[i])
    row.append(t_min_c[i])
    row.append(t_max_c[i])
    row.append(r_mm[i])
    row.append(r24_mm[i])
    row.append(s_cm[i])
    table.append(row)
    row=[]
# Пишем в файл
with open('48300_dec.csv', 'w', encoding='cp1251', newline="") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(table)



