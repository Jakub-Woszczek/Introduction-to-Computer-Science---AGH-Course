import math

liczba_do_rozkładu = int(input("Podaj liczbe: "))
x = liczba_do_rozkładu
ostatni_podzielnik = 0

for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
        ostatni_podzielnik = i

if ostatni_podzielnik == 0:
    print(f'Liczba {liczba_do_rozkładu} jest pierwsza')
else:
    if liczba_do_rozkładu / ostatni_podzielnik == ostatni_podzielnik:
        print(ostatni_podzielnik, ostatni_podzielnik)
    else:
        print(ostatni_podzielnik, int(liczba_do_rozkładu / ostatni_podzielnik))




