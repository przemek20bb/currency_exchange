#to ma byc funkcja przyjmująca sciezke do plku .txt i zwracająca kursy euro
def reading_rate(sciezka,waluta):
    f = open(sciezka,mode="r+")
    lista1=f.readlines()
    #print(lista1)
    f.close()
    y=waluta
    m="<nazwa_waluty>"+(y)+"</nazwa_waluty>\n"
    #print(m)
    k=lista1.index(m)

    w=lista1[k+3]
    t=lista1[k+4]
    #print(w)
    #print(t)

    l= w[12:16].replace(",",".")
    #print ("Kurs kupna: "+ str (l))

    r= t[16:20].replace(",",".")
    #print ("Kurs sprzedazy: "+ str (r))
    return r
#reading_rate("kursy_walut.txt","frank szwajcarski")
#frank=reading_rate("kursy_walut.txt","frank szwajcarski")
#print(frank)
# jak wczytac zmienna zwracana przez funkcje?