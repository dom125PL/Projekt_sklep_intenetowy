produkty_baza = [
    {"nazwa": "Laptop", "cena_netto": 3000.00, "kategoria": "Elektronika"},
    {"nazwa": "Myszka", "cena_netto": 100.00, "kategoria": "Elektronika"},
    {"nazwa": "Koszulka", "cena_netto": 50.00, "kategoria": "Odziez"},
    {"nazwa": "Spodnie", "cena_netto": 120.00, "kategoria": "Odziez"}
]

#Wpisanie jakom ilosciom kwoty chcemy wydac do zmiennej portfel (wazne puzniej)
portfel = float(input("Uzupelnij portfel od danom kwote"))




#Wypisanie listy produktuw po podaniu kategori
kategoria_inp = input("Wpisz z jakiej kategori chcesz wyswietlic produkty(Elektronika, Odziez):")

def wyswietli(kategoria_inp):
    for produkty in produkty_baza:
        if kategoria_inp == produkty["kategoria"]:
            print(produkty["nazwa"], produkty["cena_netto"])


wyswietli(kategoria_inp)




#Wybranie 1 produktu ktury chcemy kupic i zwrucenie jego ceny
zakupy_inp = input("Co chcesz kupic wypisz z wczesniej podanej listy produktuw: ")

def koszyk(zakupy_inp):
    for produkty in produkty_baza:
        if zakupy_inp == produkty["nazwa"]:
            return produkty["cena_netto"]
        

def brutto(cena_netto, vat=0.23):
    return ((cena_netto*vat)+cena_netto)



      
cena_brutto = (brutto(koszyk(zakupy_inp)))


print("Reszta bedzie wynosila:", portfel-cena_brutto)
zgoda = input("Czy podtwierdzasz tranzakcje (tak/nie):")

if zgoda == "tak":
    if portfel >= cena_brutto:
        print("Dzekujemy za zakup")
    else:
        print("Niewystarczajaco pieniedzy")
else:
    print("Anulowanie tranzakcji")

