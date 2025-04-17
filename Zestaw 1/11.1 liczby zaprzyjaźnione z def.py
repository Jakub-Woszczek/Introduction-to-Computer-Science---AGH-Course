def suma_podzielników(liczba):
    sum = 1
    root = int(liczba ** (1 / 2)) + 1
    for i in range(2, root):
        if liczba % i == 0:
            sum += i
            sum += int(liczba / i)
            if i == int(liczba / i):
                sum -= i

    return sum
liczba_1 = None
liczba_2 = None
lista = []
m = None
for m in range(2,1000000+1):
    liczba_1 = suma_podzielników(m)
    liczba_2 = suma_podzielników(liczba_1)
    if m == liczba_2 and liczba_1 != liczba_2 and sorted([liczba_1,liczba_2]) not in lista:

        lista.append(sorted([liczba_1,liczba_2]))

print(lista)



