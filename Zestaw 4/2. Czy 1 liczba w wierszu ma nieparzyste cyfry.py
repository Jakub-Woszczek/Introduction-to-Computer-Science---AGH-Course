def liczba_ma_wszystkie_nieparzyste(num):

    while num != 0:
        cyfra = num%2

        if cyfra == 0:
            return False

        num //=10

    return True



def czy_każdy_wiersz_ma_przynajmniej_jedną_cyfrę(N):
    import random
    tablica = [[random.randint(1,100) for _ in range(N)] for _ in range(N)]

    wiersz = 0
    kolumna = 0

    for wiersz in range(N):
        cunt = N
        for kolumna in range(N):
            print(wiersz,kolumna)
            if liczba_ma_wszystkie_nieparzyste(tablica[wiersz][kolumna]) == False and cunt ==1:
                print(tablica[wiersz][kolumna])
                for bruh in tablica:
                    print(bruh)

                return False
            cunt -=1

    for bruh in tablica:
        print(bruh)

    return True

print(czy_każdy_wiersz_ma_przynajmniej_jedną_cyfrę(10))