from konto import Konto

def f(lista=[], konto=Konto('Ala', 'Kowalska')):
    konto.wplata(200)
    lista.append(konto._saldo)
    print(konto,lista)

k1 = Konto(1,'Ola',5000)
f([1,2,5], k1)

