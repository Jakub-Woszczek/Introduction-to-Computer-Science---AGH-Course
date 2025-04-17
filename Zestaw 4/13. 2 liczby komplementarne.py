def cz_są_komplementarne(a,b):
    import math
    sum = a+b
    factor = 2
    for factor in range(2,int(math.sqrt(sum))+1):
        if sum%factor ==0:
            return False

    return True

def zerowanie_nie_komplementarnych(T):
    for bruh in T:
        print(bruh)
    T_kopia = [[e for e in t]for t in T]


    for wiersz in range(len(T)):
        for kolumna in range(len(T)):
            komplementarna = 0
            for i in range(len(T)):
                for j in range(len(T)):

                    if (wiersz != i or kolumna != j) and cz_są_komplementarne(T[wiersz][kolumna],T[i][j]) == True:
                        komplementarna +=1

            if komplementarna<1:
                print(T[wiersz][kolumna])
                T_kopia[wiersz][kolumna] = 0

    return T_kopia


def generowanie_tablicy(N):
    import random

    tablica = [[random.randint(3,3) for _ in range(N)] for _ in range(N)]

    return tablica

tablica = generowanie_tablicy(5)

wyzerowana = zerowanie_nie_komplementarnych(tablica)
print('')
for bru in wyzerowana:
    print(bru)







