#liczba_dosk = int(input('Podaj liczbę do sprawdzenia: '))
liczba_dosk = 0
sum = 1

while liczba_dosk <=1000000:
    root = liczba_dosk ** (1 / 2)
    sum = 1
    for i in range(2, int(root + 2)):

        if liczba_dosk % i == 0:
            sum += int(i)
            sum += int(liczba_dosk / i)

    if sum == liczba_dosk:
        print('Jest doskonała: ', liczba_dosk)
    liczba_dosk += 1
