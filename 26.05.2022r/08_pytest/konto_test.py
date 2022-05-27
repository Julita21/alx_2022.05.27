import pytest

from konto import Konto, BrakSrodkow

def test_init():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    assert konto.numer == 1
    assert konto.wlasciciel == 'Ala'
    assert konto.saldo == 1000

def test1_init():
    konto = Konto(numer=2, wlasciciel='Julita')
    assert konto.numer == 2
    assert konto.wlasciciel == 'Julita'
    assert konto.saldo == 0

def test_wplata():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    konto.wplata(300)
    assert konto.saldo == 1300

def test_wplata_ujemna():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    with pytest.raises(ValueError):
        konto.wplata(-100)
    assert konto.saldo == 1000


def test_wyplata():
    konto = Konto(numer=1, wlasciciel='Ala',saldo=1000)
    konto.wyplata(400)
    assert konto.saldo == 600

def test_wyplata_ujemna():
    konto = Konto(numer=1, wlasciciel='Ala', saldo=1000)
    with pytest.raises(ValueError):
        konto.wplata(-100)
    assert konto.saldo == 1000

