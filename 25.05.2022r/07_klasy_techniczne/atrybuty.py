class A:
    pass


a = A()
print(a)
#print(a.imie)


# Do obiektu można dodać atrybut, nawet gdy nie o nim mowy w treści klasy.
a.imie = 'Ala'
a.wiek = 30
print(a.imie)

class Osoba:
    def __init__(self,imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

o = Osoba('Jan', 'Kowalski', 40)
o.numer_buta = 44

slownik = o.__dict__ # tym zapisem można dostać się do słownika
print(slownik)

# słownik jest wciąż powiązany z tym obiektem
# zmiany w obiekcie są widocznie w słowniku i są widoczne w obiekcie i vicewersa
o.wiek += 1
print(slownik)

slownik['wiek'] += 10
slownik['telefon'] = '123456789'
print(o.wiek)
print(o.telefon)
print()

# Przykład zastosowania: wypisywanie wszystkich pól obiektu jako linii tekstu "a la CSV"
# Nie wiedząc, jakie pola ma obiekt, mogę napisać unowersalną funkcję
def wypisz(obiekt, sep=';'):
   print(*obiekt.__dict__.values(), sep=sep)

wypisz(o)

# dostanie się do klasy z pól prywatnych
class Klasa:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b # konwencja 'pseudo pola prywatne'
        self.__c = c # name mangling

k = Klasa('Ala', 'Basia', 'Celina')
print(k.__dict__)

print(k.a)
print(k._b)

k._Klasa__c = 'Cezary'
print(k._Klasa__c)
