def lista_cyfr(num):
    lista = [1 if i == 0 else 0 for i in range(10)]
    while num != 0:
        cyfra = num % 10
        lista[cyfra] = cyfra

        num //=10

    return lista

print(lista_cyfr(123489))

def transef_na_liste_cyfr_całęj_tablicy(T):

    for wiersz in range(len(T)):
        for kolumna in range(len(T)):
            T[wiersz][kolumna] = lista_cyfr(T[wiersz][kolumna])

    return T



def czy_z_boku_przyjaciólki(T):

    T = transef_na_liste_cyfr_całęj_tablicy(T)
    lista_współżędnych = []
    cunt_cały = 0

    for wiersz in range(len(T)):
        for kolumna in range(len(T)):

            if (wiersz > 0 and wiersz < (len(T) - 1)) and (kolumna > 0 and kolumna < (len(T) - 1)):
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz+1][kolumna]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz][kolumna+1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz][kolumna-1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna+1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna-1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna-1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna+1]:
                    cunt +=1
                if cunt ==8:
                    cunt_cały += 1
                    współżędna = [wiersz,kolumna]
                    lista_współżędnych.append(współżędna)

            # Rogi

            if wiersz == 0 and kolumna == 0:
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz][kolumna+1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna+1]:
                    cunt +=1
                if cunt ==3:
                    cunt_cały += 1
                    współżędna = [wiersz,kolumna]
                    lista_współżędnych.append(współżędna)

            if wiersz == (len(T)-1) and kolumna == (len(T)-1):
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz][kolumna-1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna-1]:
                    cunt +=1
                if cunt ==3:
                    cunt_cały += 1
                    współżędna = [wiersz,kolumna]
                    lista_współżędnych.append(współżędna)

            if wiersz == 0 and kolumna == (len(T)-1):
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz][kolumna-1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna-1]:
                    cunt +=1
                if cunt ==3:
                    cunt_cały += 1
                    współżędna = [wiersz,kolumna]
                    lista_współżędnych.append(współżędna)

            if wiersz == (len(T)-1) and kolumna == 0:
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz][kolumna+1]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna]:
                    cunt +=1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna+1]:
                    cunt +=1
                if cunt ==3:
                    cunt_cały += 1
                    współżędna = [wiersz,kolumna]
                    lista_współżędnych.append(współżędna)

            # Boki pionowe

            if (wiersz>0 and wiersz<(len(T)-1)) and  kolumna ==0:
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz-1][kolumna]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna+1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz][kolumna + 1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna + 1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna]:
                    cunt += 1
                if cunt == 5:
                    cunt_cały += 1
                    współżędna = [wiersz, kolumna]
                    lista_współżędnych.append(współżędna)

            if (wiersz>0 and wiersz<(len(T)-1)) and  kolumna ==(len(T)-1):
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz-1][kolumna]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna-1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz][kolumna - 1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna - 1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna]:
                    cunt += 1
                if cunt == 5:
                    cunt_cały += 1
                    współżędna = [wiersz, kolumna]
                    lista_współżędnych.append(współżędna)

            # Boki poziome

            if (kolumna>0 and kolumna<(len(T)-1)) and  wiersz ==0:
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz][kolumna+1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna+1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz+1][kolumna - 1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz][kolumna-1]:
                    cunt += 1
                if cunt == 5:
                    cunt_cały += 1
                    współżędna = [wiersz, kolumna]
                    lista_współżędnych.append(współżędna)

            if (kolumna>0 and kolumna<(len(T)-1)) and  wiersz ==(len(T)-1):
                cunt = 0
                if T[wiersz][kolumna] == T[wiersz][kolumna-1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna-1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz-1][kolumna+1]:
                    cunt += 1
                if T[wiersz][kolumna] == T[wiersz][kolumna+1]:
                    cunt += 1
                if cunt == 5:
                    cunt_cały += 1
                    współżędna = [wiersz, kolumna]
                    lista_współżędnych.append(współżędna)




    return lista_współżędnych,cunt_cały


import random

rows = 4
columns = 4


table = [[random.randint(0, 1) for _ in range(columns)] for _ in range(rows)]


for row in table:
    print(row)



print(czy_z_boku_przyjaciólki(table))







