# Nieskończony generator liczb parzystych

def parzyste():
    liczba = 0
    while True:
        yield liczba
        liczba += 2

# Samo wywołanie nie wykonuje tej pętli. Tworzony jest generator.
g = parzyste()
# print (g)

# Dopiero umieszczenie w pętli for, albo wielokrotne wywołanie next, albo konwersja na listę/ zbiorze / itp.
# spowoduje wykonanie tej pętli i dostarczenie kolejnych wartości.
for x in parzyste():
    print(x)

# to będzie szło w nieskończoność. Trzeba zatrzymać pętlę, bo inaczej nam zamuli komputer.