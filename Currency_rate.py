import requests

#funkcja przyjmująca  nazwe waluty, a zwracająca kurs sprzedaży tej waluty
def reading_rate_sale(waluta):

    res = requests.get('https://www.nbp.pl/kursy/xml/LastC.xml')
    res.raise_for_status() # check if is positive response
    hej = res.text
    lista_nbp=[]
    lista_nbp=hej.splitlines()
    #mozna zrobic w petli druga liste z usunieciem spacji - lstrip()
    #print(lista_nbp)
    m = "      <nazwa_waluty>"+(waluta)+"</nazwa_waluty>"
    k=lista_nbp.index(m)
    #print("miejsce tej waluty na liscie nbp to: " + str(k))
    w=lista_nbp[k+3]
    t=lista_nbp[k+4]

    r= t[22:26].replace(",",".")
    #print ("Kurs sprzedazy: "+ str (r))
    return r

#funkcja przyjmująca  nazwe waluty, a zwracająca kurs kupna tej waluty
def reading_rate_buy(waluta):

    res = requests.get('https://www.nbp.pl/kursy/xml/LastC.xml')
    res.raise_for_status() # check if is positive response
    hej = res.text
    lista_nbp=[]
    lista_nbp=hej.splitlines()
    #print(lista_nbp)
    m = "      <nazwa_waluty>"+(waluta)+"</nazwa_waluty>"
    k=lista_nbp.index(m)
    #print("miejsce tej waluty na liscie nbp to: " + str(k))
    w=lista_nbp[k+3]
    t=lista_nbp[k+4]

    l= w[18:22].replace(",",".")
    #print ("Kurs kupna: "+ str (l))

    return l