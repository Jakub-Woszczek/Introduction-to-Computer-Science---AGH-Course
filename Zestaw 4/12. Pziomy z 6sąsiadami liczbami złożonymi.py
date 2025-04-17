import math

def zamiana_liczb_na_pierwsze_złożone(T):

    for wiersz in range(len(T)):
        for kolumna in range(len(T)):
            for height in range(len(T)):
                liczba = T[wiersz][kolumna][height]
                T[wiersz][kolumna][height] = 1
                for dzielnik in range(2, int(math.sqrt(liczba)) + 1):
                    if liczba % dzielnik == 0:
                        T[wiersz][kolumna][height] = 0
                        break




    return T

tablica = [[[23,23,23],[23,23,23],[23,23,23]],[[4,4,4],[4,4,4],[4,4,4]],[[7,17,47],[7,17,47],[7,17,47]]]
tablica_kopia = tablica.copy()
def szukanie_sąsiadów_złożonych(T):

    T = zamiana_liczb_na_pierwsze_złożone(T)

    count_podstawa =0
    for height in range(len(T)):

        count_poziomu = 0
        for wiersz in range(1,len(T)-1):
            for kolumna in range(1,len(T)-1):

                print(f'poziom: {height}, wiersz: {wiersz}, kolumna: {kolumna}, ')

                tablica_tymnczasowa = [0 for _ in range(9)]
                count = 0
                for i in range(wiersz - 1, wiersz + 2):
                    for j in range(kolumna - 1, kolumna + 2):
                        print(f'(przed warunem) poziom: {height}, i: {i}, j: {j}, tablica: {T[i][j][height]}')
                        if (i != wiersz or j != kolumna) and T[i][j][height] == 1:
                            print(f'dodało')
                            count_poziomu +=1

                if count == 9:
                    count_poziomu +=1

        if count_podstawa == 0:
            count_podstawa = count_poziomu

        else:
            if count_podstawa != count_poziomu:
                return False
    return True


for bruh in tablica:
    print(bruh)

print(szukanie_sąsiadów_złożonych(tablica))












