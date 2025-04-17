def lista_cyfr(num):
    if num == -1:
        lista = [-1 for i in range(11)]
        return lista

    else:
        lista = [1 if i == 0 else 0 for i in range(10)]

        while num != 0:
            cyfra = num % 10
            lista[cyfra] = cyfra

            num //= 10

        return lista


def transef_na_liste_cyfr_całęj_tablicy(T):


    for wiersz in range(len(T)):
        for kolumna in range(len(T)):
            for bruh in T:
                print(bruh)
            print(wiersz,kolumna)


            T[wiersz][kolumna] = lista_cyfr(T[wiersz][kolumna])

    return T

def dodanie_True(table):
    for i in range(columns):
        table[i] = [-1] + table[i] + [-1]

    # table_insert = [[-1 for _ in range(rows + 2)]]
    # table_insert_2 = table_insert.copy()
    # table_insert_3 = table_insert_2.copy()
    # table = table_insert_2 + table
    # table = table + table_insert_3
    table = [[-1 for _ in range(rows + 2)]] + table
    table = table + [[-1 for _ in range(rows + 2)]]
    print('tablica',table)


    return table

def szukanie_przyjaciółek(T):


    T = dodanie_True(T)

    T = transef_na_liste_cyfr_całęj_tablicy(T)
    lista_współżędnych = []
    count_ogólny = 0
    for wiersz in range(len(T)-2):
        for kolumna in range(len(T)-2):


            count_wysoki = 0
            for height in range(0,10):
                liczba = T[wiersz][kolumna][height]
                if liczba == -1:
                    liczba = T[wiersz+1][kolumna+1][height]
                count_płaski = 0
                for iter_1 in range(3):
                    for iter_2 in range(3):
                        if liczba == T[wiersz+iter_1][wiersz+iter_2][height] or T[wiersz+iter_1][wiersz+iter_2][height] == -1:
                            count_płaski +=1
                if count_płaski == 9:
                    count_wysoki +=1

            if count_wysoki == 10:
                współrzędna = [wiersz, kolumna]
                lista_współżędnych.append(współrzędna)
                count_ogólny +=1

    return count_ogólny,lista_współżędnych


import random

rows = 4
columns = 4


table = [[random.randint(1, 2) for _ in range(columns)] for _ in range(rows)]
kopia = table.copy()




print(szukanie_przyjaciółek(table))

for mech in kopia:
    print(mech)


