import datetime
from Currency_rate import reading_rate

czas=datetime.datetime.now()
actual_date=czas.strftime("%I:%M %d.%m.%Y %A")
print ("DATA: " + actual_date)
print ("Podaj nazwy walut dla ktorych chcesz sprawdzic kurs:")
kursy_walut=[]
waluty=[]
waluta1=input()
waluta2=input()
kursy_walut.append(reading_rate("kursy_walut.txt",waluta1))
kursy_walut.append(reading_rate("kursy_walut.txt",waluta2))

print("Aktualny kurs " + waluta1 + " wynosi:" + kursy_walut[0] + "(sprzedaz)")
print("Aktualny kurs " + waluta2 +  " wynosi:" + kursy_walut[1] + "(sprzedaz)")

print ("Podaj jaką walute chcesz sprzedac: " + waluta1 + " czy " + waluta2 )
waluta_na_sprzedaz=input()
if waluta_na_sprzedaz == waluta1:
    cena_waluty=kursy_walut[0]
if waluta_na_sprzedaz == waluta2:
    cena_waluty = kursy_walut[1]
print ("W jakiej ilosci chcesz sprzedać " + waluta_na_sprzedaz)
waluta_na_sprzedaz_ilosc=input()
sprzedaz_waluta1=float((cena_waluty))*float((waluta_na_sprzedaz_ilosc))
print("Za sprzedaz " + waluta_na_sprzedaz_ilosc + " " + waluta_na_sprzedaz + " dostaniesz: " + str(sprzedaz_waluta1))

