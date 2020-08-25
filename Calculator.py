import datetime
from Currency_rate import reading_rate

czas=datetime.datetime.now()
actual_date=czas.strftime("%I:%M %d.%m.%Y %A")
print ("DATA: " + actual_date)
print ("Podaj nazwy walut dla ktorych chcesz sprawdzic kurs:")
waluta=[]
#aluta[0]=str(input())
waluta1=input()
waluta2=input()
euro=reading_rate("kursy_walut.txt",waluta1)
dolar=reading_rate("kursy_walut.txt",waluta2)

print("Aktualny kurs euro wynosi:" + euro + "(sprzedaz)")
print("Aktualny kurs dolara wynosi:" + dolar + "(sprzedaz)")


print("Podaj Ile masz pieniążków: [zł]")
oszczednosci=input()
#oszczednosci_w_euro=(oszczednosci)/(euro)
#print("Za swoje oszczednosci mozesz kupic " + str(int (oszczednosci_w_euro)) + " euro")

