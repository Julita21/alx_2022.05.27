# Gdy mam krotkę
krotka = ('Ala', 5, 'kotów')

# Gdy mam listę
lista = ['Ola', 5, 'psów']

osoba, ile, zwierze = krotka
print(f'{osoba} ma {ile} {zwierze}')

osoba, ile, zwierze = lista
print(f'{osoba} ma {ile} {zwierze}')

# Gdy wpisujemy wartość do tupli, to zwykle nie trzeba brać tego w nawiasy

krotka = 'Ala', 5, 'kotów'
print(type(krotka))
osoba,ile,zwierze = krotka
print(f'{osoba} ma {ile} {zwierze}')
print()

#stąd możliwe są takie zapisy:
x,y,z = 10,20,30
print('x=', x,'y=',y )

x,y = y,x
print('x=',x, 'y=',y)

def dzielenie_z_reszta(x, y):
   return x // y, x % y

iloraz, reszta = dzielenie_z_reszta(10, 3)
print(f'10 podzielić na 3 daje wynik {iloraz} i {reszta} reszty.')

tupla = dzielenie_z_reszta(10, 3)
print(f'10 podzielić na 3 daje wynik {tupla[0]} i {tupla[1]} reszty.')

iloraz, reszta = dzielenie_z_reszta(28, 5)
print(f'10 podzielić na 3 daje wynik {iloraz} i {reszta} reszty.')


