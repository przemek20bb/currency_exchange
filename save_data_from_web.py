#!/usr/bin/env python

from lxml import html
from datetime import date
import requests

# pobieram dzisiejszą datę
today = date.today()
# format wyświetlanej daty
data = today.strftime('%Y-%9-%d')
print ("DATA: " + data)
# adres strony z horoskopem
urlwyborcza = 'https://horoskopy.gazeta.pl/horoskop/byk/dzienny/'
# składam adres strony i daty w celu pobierania aktualnego horoskopu
urlwyborcza += data
print ("urlwyborcza: " + urlwyborcza)
# ścieżka do elementu XPATH
xpathwyborcza = '//*[@id="holder_217"]/section/p/text()'
# pobiera stronę z horoskopem
pagewyborcza = requests.get(urlwyborcza)
# parsuje stronę
tree = html.fromstring(pagewyborcza.text)
# wyszukuje interesujący nas element
textwyborcza = tree.xpath(xpathwyborcza)
# wyświetla w yniki działania
print(data)
print(textwyborcza)