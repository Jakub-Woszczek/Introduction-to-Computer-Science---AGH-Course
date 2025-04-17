def czy_przynajmniej_jedna_parzysta(num):

    while num !=0:
        cyfra = num % 2
        if cyfra == 0:
            return True

        num //=10

    return False


def T(N):
    import random
    tablica = [[random.randint(1,100) for _ in range(N)] for _ in range(N)]


    wiersz = 0
    kolumna = 0

    istnieje = False

    while wiersz <N:
        cunt = 0
        while kolumna <N:
            if czy_przynajmniej_jedna_parzysta(tablica[wiersz][kolumna]) == True:
                cunt +=1

            kolumna +=1
        if cunt ==N:
            for bruh in tablica:
                print(bruh)
            return True
        wiersz +=1
        kolumna = 0


    print(tablica)

    return False

print(T(3))






