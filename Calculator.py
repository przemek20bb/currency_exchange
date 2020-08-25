import datetime

czas=datetime.datetime.now()
actual_date=czas.strftime("%I:%M %d.%m.%Y %A")
print ("DATA: " + actual_date)
print("Hej, podaj aktualny kurs euro:")
euro=input()
#funt=input()
#dolar=input()
#frank=input()

print("Aktualny kurs euro wynosi:" + euro)
#print("Aktualny kurs euro wynosi:" + dolar)
#print("Aktualny kurs euro wynosi:" + frank)
#print("Aktualny kurs euro wynosi:" + funt)

print("Podaj Ile masz pieniążków: [zł]")
oszczednosci=input()
oszczednosci_w_euro=int (oszczednosci)/int (euro)
print("Za swoje oszczednosci mozesz kupic " + str(int (oszczednosci_w_euro)) + " euro")

