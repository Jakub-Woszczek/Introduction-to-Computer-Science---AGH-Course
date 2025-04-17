def suma_iloarzu_krzyżowego(N):
    import random
    tablica = [[random.randint(1,10) for _ in range (N)] for _ in range(N)]


    sumy_kolumn = [0 for _ in range(N)]
    for kolumna in range(N):
        suma = 0
        for wiersz in range(N):
            suma += tablica[wiersz][kolumna]
        sumy_kolumn[kolumna] = suma


    sumy_wierszy = [0 for _ in range(N)]
    for wiersz in range(N):
        suma = 0
        for kolumna in range(N):
            suma += tablica[wiersz][kolumna]
        sumy_wierszy[wiersz] = suma

    print(sumy_kolumn)
    print(sumy_wierszy)

    max_iloczyn = 0
    iloczyn = 0

    for s_kolumna in sumy_kolumn:
        for s_wiersz in sumy_wierszy:
            iloczyn = s_kolumna*s_wiersz
            print(iloczyn)
            if iloczyn>max_iloczyn:
                max_iloczyn = iloczyn





    for bruh in tablica:
        print(bruh)

    return max_iloczyn

print(suma_iloarzu_krzyżowego(7))