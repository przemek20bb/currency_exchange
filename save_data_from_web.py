
from lxml import html
from datetime import date
import requests

# pobieram dzisiejszą datę
today = date.today()
# format wyświetlanej daty
data = today.strftime('%d-%m-%Y')
# adres strony z horoskopem
urlwyborcza = 'https://www.nbp.pl/home.aspx?f=/kursy/kursyc.html'
# składam adres strony i daty w celu pobierania aktualnego horoskopu
urlwyborcza += data

# ścieżka do elementu XPATH
xpathwyborcza = '//*[@id="holder_230"]/div/p[1]/text()'
# pobiera stronę z horoskopem
pagewyborcza = requests.get(urlwyborcza)
# parsuje stronę
tree = html.fromstring(pagewyborcza.text)
# wyszukuje interesujący nas element
textwyborcza = tree.xpath(xpathwyborcza)
# wyświetla w yniki działania
print(data)
print(textwyborcza)
# zapis do pliku kursy_walut.txt