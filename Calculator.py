import datetime
from Currency_rate import reading_rate_sale
from Currency_rate import reading_rate_buy
from parsowanie_walut import parsowanie_listy_walut

czas = datetime.datetime.now()
actual_date = czas.strftime("%I:%M %d.%m.%Y %A")
lista_walut = ["euro", "dolar amerykañski", "frank szwajcarski", "funt szterling", "korona czeska", "korona szwedzka",
               "korona duñska", "korona norweska"]

print("DATA: " + actual_date)
print("Aktualna tabela kursów walut:")
print("Nazwa waluty          |" + " Sprzedaz |" + " Kupno|")
print("----------------------|----------|------|")
for i in range(len(lista_walut)):
    print(str(i + 1) + "." + parsowanie_listy_walut(lista_walut[i]) + "| " + (
        reading_rate_sale(lista_walut[i])) + "     | " + (reading_rate_buy(lista_walut[i])) + " |")
print("----------------------|----------|------|")
print("Wybierz rodaj waluty dla ktorej chcesz dokonac przeliczenia 1-" + str(len(lista_walut)))
# cześć kodu odpowiedzialna za wybor waluty
rodzaj_waluty = 0
while rodzaj_waluty <= 0 or rodzaj_waluty > len(lista_walut):
    try:
        rodzaj_waluty = int(input())
        if int(rodzaj_waluty) <= 0:
            print("wprowadziles wartosc liczby <=0,spróbuj jeszcze raz")
        else:
            if int(rodzaj_waluty) > len(lista_walut):
                print("wprowadziles wartosc liczby >" + str(len(lista_walut)) + " spróbuj jeszcze raz")
    except ValueError:
        print("Nie wprowadziłes/as liczby, spróbuj jeszcze raz")


# test sprawdzający czy poadana przez nas liczba jest w zakresie listy wyswietlonych walut
def test_is_currency():
    assert int(rodzaj_waluty) <= len(lista_walut)


waluta = lista_walut[int(rodzaj_waluty) - 1]
print("Wybrana waluta to: " + waluta)
print("Chcesz sprzedać czy kupic walute? \n 1.Sprzedaz \n 2.Kupno")
# cześć kodu odpowiedzialna za wybor transakcji
wybor_transakcji = 0
while wybor_transakcji <= 0 or wybor_transakcji > 2:
    try:
        wybor_transakcji = int(input())
        if str(wybor_transakcji) == "1":
            operacja = "sprzedaż"
            print("Aktualny kurs " + waluta + " wynosi:" + reading_rate_buy(
                waluta) + " (Po takim kursie nastąpi " + operacja + ")")
            x = reading_rate_buy(waluta)
        elif str(wybor_transakcji) == "2":
            operacja = "kupno"
            print("Aktualny kurs " + waluta + " wynosi:" + reading_rate_sale(
                waluta) + " (Po takim kursie nastąpi " + operacja + ")")
            x = reading_rate_sale(waluta)
        else:
            print("wprowadziles wartosc liczby spoza zakresu,spróbuj jeszcze raz")
    except ValueError:
        print("Nie wprowadziłes/as liczby, spróbuj jeszcze raz")

print("W jakiej ilosci ma nastapic " + operacja + " " + waluta)
# cześć kodu odpowiedzialna za podanie ilosci waluty
waluta_na_sprzedaz_kupno_ilosc = 0
while waluta_na_sprzedaz_kupno_ilosc <= 0:
    try:
        waluta_na_sprzedaz_kupno_ilosc = int(input())
        if int(waluta_na_sprzedaz_kupno_ilosc) <= 0:
            print("wprowadziles wartosc liczby <=0,spróbuj jeszcze raz")
    except ValueError:
        print("Nie wprowadziłes/as liczby, spróbuj jeszcze raz")
waluta_wartosc_sprzedazy_kupna = float(x) * float((waluta_na_sprzedaz_kupno_ilosc))
print("Wartosc transakcji " + operacja + " " + str(waluta_na_sprzedaz_kupno_ilosc) + " " + waluta + " wynosi: " + str(
    round(waluta_wartosc_sprzedazy_kupna, 2)))
