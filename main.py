from bs4 import BeautifulSoup

with open('48300_dec.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
title = soup.find("h1", class_="chronicle-title")
title = title.contents
#print(title)