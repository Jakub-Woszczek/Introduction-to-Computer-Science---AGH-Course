def suma_podzielników(liczba):
    total = 1
    root = int(liczba ** 0.5) + 1
    for i in range(2, root):
        if liczba % i == 0:
            total += i
            if i != liczba // i:
                total += liczba // i
    return total

for m in range(2, 1000000 + 1):
    liczba_1 = suma_podzielników(m)
    liczba_2 = suma_podzielników(liczba_1)

    if liczba_2 == m and liczba_1 != m:
        print(f"Amicable pair found: ({m}, {liczba_1})")
