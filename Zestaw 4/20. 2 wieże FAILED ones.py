def dodanie_piętra_do_tablicy(T):



    for wiersz in range(len(T)):
        for kolumna in range(len(T)):
            lvl = [[0 for _ in range(len(T))] for _ in range(len(T))]

            T[wiersz][kolumna] = piętro(T[wiersz][kolumna])
    return T

def piętro(num):
    list = [num,0]
    return list



def szukanie_max_ustawień_wież(N):


    współżędne = []
    suma_max = 0
    import random
    T = [[random.randint(1, 9) for _ in range(8)] for _ in range(8)]
    T = dodanie_piętra_do_tablicy(T)
    for wiersz_1 in range(N):
        for kolumna_1 in range(N):

            for wiersz_2 in range(N):
                for kolumna_2 in range(N):


                    for bruh in T:
                        print(bruh)
                    print('\n')

                    if wiersz_1 != wiersz_2 or kolumna_1 != kolumna_2:

                        for a in range(N):
                            T[a][kolumna_1][1] = 1
                        for b in range(N):
                            T[wiersz_1][b][1] = 1
                        for x in range(N):
                            T[x][kolumna_2][1] = 1
                        for y in range(N):
                            T[wiersz_2][y][1] = 1


                        T[wiersz_1][kolumna_1][1] = True
                        T[wiersz_2][kolumna_2][1] = True

                        suma = 0
                        for a in range(N):
                            for b in range(N):
                                if T[a][b][1] == 1:
                                    suma += T[a][b][0]

                        if suma>suma_max:
                            suma_max = suma
                            współżędne = [[wiersz_1,kolumna_1],[wiersz_2,kolumna_2]]

                        for bruh in T:
                            print(bruh)
                        print(f'suma={suma}\n')

                    for i in range(len(T)):
                        for j in range(len(T)):
                            T[i][j][1] = 0

    return suma_max,współżędne


print(szukanie_max_ustawień_wież(8))
