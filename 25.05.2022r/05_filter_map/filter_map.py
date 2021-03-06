from random import randint

liczby = [randint(1,100) for i in range(20)]
print(liczby)

#Aby wypisać tylko liczby spełniające warunek,np tylko podzielne przez 2,
#można:

for liczba in liczby:
    if liczba % 2 == 0:
        print(liczba, end=' ')
print()
print('#' * 40)

# Można uzyskać listę parzystych za pomocą list comprehension ("wyrażenie listotwórcze")

parzyste = [x for x in liczby if x % 2 == 0]
print(parzyste)

# istnieje też funkcja filter, która zwraca zestaw tych elementów listy (lub innej kolekcji),
# które spełniają podany warunek.
# Warunek podaje się w formie funkcji, która dostahe wartość i zwraca True/False.

parzyste2 = filter(lambda x: x%2 == 0, liczby)
print(parzyste2)
for p in parzyste2:
    print(p, end=', ')
print()

# Wyjaśnienie dlaczego dodatkowa pętla:
# Filter zwraca w wyniku "generator", czyli obiekt, który zwraca wartości dopiero, gdy jest o to proszony,np.
# w pętli for


# Można też od razu to rzutować to na listę
print(list(filter(lambda x: x%2 == 0, liczby)))


# Zastosowanie funkcji, np. podnoszenie do kwadratu dla każdego elementu listy, np. w klasycznej pętli

for liczba in liczby:
    print(liczba**2, end=', ')
    print()


# Możemy użyć list comprehension
kwadraty = [ x**2 for x in liczby]
print(kwadraty)

#albo użyć map
kwadraty2 = map(lambda x: x**2, liczby)
print(kwadraty2)
for k in kwadraty2:
    print(k, end=', ')
print()

print(list(map(lambda x: x**2, liczby)))

#połączenie obu technik
for liczba in liczby:
    if liczba % 2 == 0:
        print(liczba**2, end=' ')
print()

parzyste_kwadraty = [x**2 for x in liczby if x % 2 == 0]
print(parzyste_kwadraty)

pk2 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, liczby)))
print(pk2)


# To staje się łądniejsze w zapisie, gdy mamy funkcję, której chcemy użyć
def jest_parzysta(liczba):
   return liczba % 2 == 0

def kwadrat(x):
   return x**2

pk3 = list(map(kwadrat, filter(jest_parzysta, liczby)))
print(pk3)

print()

miasta = ['Warszawa', 'Kraków', 'Gdańsk']

for m in map(str.upper, miasta):
   print(m)


print('Poznań'.upper())
print(str.upper('Łódź')) # Łódź jest parametrem self







