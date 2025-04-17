def silnia(num):
    if num == 1:
         return 1
    wynik = num*silnia(num-1)

    return wynik

def tablica_dzielenia_pisemnego(licznik,mianownik):

    wielokrotności = [licznik//mianownik]
    po_przecinku = []
    licznik = licznik%mianownik
    for _ in range(10000):
        licznik *=10
        po_przecinku.append(licznik//mianownik)
        licznik =licznik%mianownik

    return wielokrotności,po_przecinku

def długość_liczby(num):
    długość = 0
    while num!=0:
        num//=10
        długość+=1
    return długość

def stała_e_z_dikładnością(p):
    i = 1
    wielokrotnosci_e = [1]
    po_rzecinku_e = [0 for _ in range(10000)]
    while 1/silnia(i) > 0:
        wielokrotność,po_przeinku = tablica_dzielenia_pisemnego(1,silnia(i))
        wielokrotnosci_e[0] += wielokrotność[0]
        for m in range(10000):
            po_rzecinku_e[m] += po_przeinku[m]

        mech,tablica_test = tablica_dzielenia_pisemnego(1,silnia(i+1))
        i +=1

    for n in range(len(po_rzecinku_e)-1,0,-1):
        długość_indexu = długość_liczby(po_rzecinku_e[n])
        iterator = 1
        liczba = po_rzecinku_e[n]
        po_rzecinku_e[n] = liczba%10
        liczba //=10
        for k in range(długość_indexu):
            po_rzecinku_e[n - iterator] += liczba % 10
            liczba //=10
            iterator+=1

    return wielokrotnosci_e,po_rzecinku_e





print(stała_e_z_dikładnością(1))


