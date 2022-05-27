from sprzedaz import wczytaj_plik

lista = wczytaj_plik('sprzedaz.csv')
print('wczytano listę:', len(lista))

for rekord in lista:
    print(rekord)