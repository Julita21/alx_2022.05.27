# chcemy utworzyć klasę Konto. W obiektach te klasy będą trzymały informacje o numerze, właścicielu i o aktulanym stanie konta(saldo)

class Konto:
    def __init__(self,numer, wlasciciel,saldo=0):
        self._numer = numer
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    def __str__(self):
        return f'Konto nr {self._numer}, właściciel {self._wlasciciel}, saldo:{self._saldo}'

    def wplata(self, kwota):
        self._saldo += kwota

    def wyplata(self, kwota):
        self._saldo -= kwota

class Osoba:
    def __init__(self,imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko



