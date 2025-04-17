def cionk_z_pierwszą_liczpą(T):
    licznik_q = T[1]
    mianownik_q = T[0]
    i = 2
    while licznik_q >1 and (licznik_q >= i or mianownik_q >= i):

        if (licznik_q%i == 0 or mianownik_q%i == 0) and licznik_q%i == mianownik_q %i:
            licznik_q /=i
            mianownik_q /=i
            i -=1
        i += 1

    # print(licznik_q,mianownik_q)
    a = 1
    b = 2
    cunt = 2
    for _ in range(len(T)-2):
        if (T[a]*licznik_q)/mianownik_q == T[b]:
            cunt +=1
            a +=1
            b +=1

    if cunt>2:
        return cunt


    return False

# print(cionk_z_pierwszą_liczpą([27,9,3,1]))
# print(cionk_z_pierwszą_liczpą([25,10,4]))

def szukanie_ciągów(T):

    T = [[2, 6, 18, 54, 162], [6, 18, 54, 162, 486], [18, 54, 162, 486, 1458], [54, 162, 486, 1458, 4374], [162, 486, 1458, 4374, 13122]]

    max_cunt = 0
    for wiersz in range(len(T)-3):
        for kolumna in range(len(T)-3):
            tablica_tymczasowa = [T[wiersz][kolumna]]
            for itereator in range(len(T)-kolumna):
                if wiersz<(len(T)-1) and kolumna<(len(T)-1):
                    wiersz += 1
                    kolumna += 1
                    tablica_tymczasowa.append(T[wiersz][kolumna])
                    wynik = cionk_z_pierwszą_liczpą(tablica_tymczasowa)
                    if wynik != False and wynik > max_cunt:
                        max_cunt = wynik



    return max_cunt

print(szukanie_ciągów(2))