def dodanie_piętra_do_tablicy(N):
    import random
    T = [[random.randint(1, 9) for _ in range(8)] for _ in range(8)]
    for bruh in T:
        print(bruh)

    for wiersz in range(len(T)):
        for kolumna in range(len(T)):
            lvl = [[0 for _ in range(N)] for _ in range(N)]

            T[wiersz][kolumna] = piętro(T[wiersz][kolumna])
    return T

def piętro(num):
    list = [num,0]
    return list

